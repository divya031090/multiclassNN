
filenames <- list.files("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/NASH", pattern="*.csv", full.names=TRUE)

i=1
j=2

i=i+2
j=j+2

microbiomedata_1<-read.csv(filenames[i], header = TRUE, stringsAsFactors = FALSE,sep=",")
microbiomedata_2<-read.table(filenames[j], header = TRUE, stringsAsFactors = FALSE,sep=",")

microbiomedata_1<-microbiomedata_1[,c(-2,-3,-5,-8,-9,-10,-11)]
microbiomedata_2<-microbiomedata_2[,c(-2,-3,-5,-8,-9,-10,-11)]



#joined_data<-merge(x = microbiomedata_1, y = microbiomedata_2, by = c("DATE_OF_REPORT","subj"), all = TRUE)

joined_data<-merge(x = joined_data, y = microbiomedata_1, by = c("DATE_OF_REPORT","subj"), all = TRUE)

joined_data<-merge(x = joined_data, y = microbiomedata_2, by = c("DATE_OF_REPORT","subj"), all = TRUE)


write.csv(joined_data,"/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/NASH/joineddata_up.csv")

acr<-read.csv("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/acr/joineddata_up.csv")
acr$diagnosis<-rep("acr",length(rownames(acr)))
ah<-read.csv("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/ah/joineddata_up.csv")
ah$diagnosis<-rep("ah",length(rownames(ah)))
bo<-read.csv("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/bo/joineddata_up.csv")
bo$diagnosis<-rep("bo",length(rownames(bo)))
congestion<-read.csv("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/congestion/joineddata_up.csv")
congestion$diagnosis<-rep("congestion",length(rownames(congestion)))
hcv<-read.csv("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/hcv/joineddata_up.csv")
hcv$diagnosis<-rep("hcv",length(rownames(hcv)))
NASH<-read.csv("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/NASH/joineddata_up.csv")
NASH$diagnosis<-rep("NASH",length(rownames(NASH)))

dataset<-rbind(acr,ah,bo,congestion,hcv,NASH)
write.csv(dataset,"/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/main_dataset.csv")


dataset<-read.csv("/Users/divvi/Documents/Dr. Bhat/Neta project - multilabel/files/main_dataset.csv")
dataset_new<-dataset[,-c(1,2,3)]



suppressMessages(library(dplyr))
suppressMessages(library(caret))
suppressMessages(library(rpart.plot))
suppressMessages(library(rpart))
suppressMessages(library(rattle))
suppressMessages(library(randomForest))

library(mice)



initialize_data <- mice(dataset_new, maxit = 0)
outlist4 <- as.character(initialize_data$loggedEvents[, "out"])
dataset_new <-dataset_new[, !names(dataset_new) %in% outlist4]

dataset_full<- mice(dataset_new, m=1, maxit = 20, method = 'pmm')


dataset_full_imputed<-complete(dataset_full,1)

#take this form csv
dataset_full_imputed$donor.age<-dataset$donor.age
dataset_full_imputed$Recepient.age<-dataset$Recepient.age

## take this from rbind
dataset<-rbind(acr,ah,bo,congestion,hcv,NASH)

dataset_full_imputed$diagnosis<-dataset$diagnosis

##change based on the category you are looking at if !=NASH then all except nash are 1 category
dataset_full_imputed$diagnosis<-replace(dataset_full_imputed$diagnosis, dataset_full_imputed$diagnosis!="acr", 0)
dataset_full_imputed$diagnosis<-factor(dataset_full_imputed$diagnosis)

set.seed(123)

smp_size <- floor(0.7 * nrow(dataset_full_imputed))
train_ind <- sample(seq_len(nrow(dataset_full_imputed)), size = smp_size)


train <- dataset_full_imputed[train_ind, ]
test <- dataset_full_imputed[-train_ind, ]

train_diagnosis<-train$diagnosis
test_diagnosis<-test$diagnosis

train<- sapply( train[,1:16], as.numeric )
test<-sapply( test[,1:16], as.numeric )

train<-as.data.frame(train)
test<-as.data.frame(test)

train$diagnosis<-factor(train_diagnosis)
test$diagnosis<-factor(test_diagnosis)
modfit.rf <- randomForest(diagnosis ~. , data=train)

predictions2 <- predict(modfit.rf, test, type = "class")

# Accuracy and other metrics
(confusionMatrix(predictions2, test$diagnosis))

varImpPlot((modfit.rf))
##NN
require(neuralnet)
require(nnet)
require(ggplot2)
nn <- neuralnet(diagnosis ~.,
                data = train,
                hidden = c(13, 10, 3),
                act.fct = "logistic",
                linear.output = FALSE,
                lifesign = "minimal")


##train$Binary.Outcome<-factor(train$Binary.Outcome)
regressor = glm(formula = diagnosis ~ ., data=train,family=binomial)
OR1<-as.data.frame(exp(cbind(coef(regressor), confint(regressor)))  )
View(OR1)

pred<-predict(regressor, test)

g6 <- roc(test$Binary.Outcome,as.numeric(pred))
auc(g6)
ci.auc(g6)