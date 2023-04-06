dataset<-rbind(acr,ah,bo,congestion,hcv,NASH)

dataset_full_imputed$diagnosis<-dataset$diagnosis

##change based on the category you are looking at if !=NASH then all except nash are 1 category
dataset_full_imputed$diagnosis<-replace(dataset_full_imputed$diagnosis, dataset_full_imputed$diagnosis!="hcv", 0)
dataset_full_imputed$diagnosis<-factor(dataset_full_imputed$diagnosis)
table(dataset_full_imputed$diagnosis)

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
write.csv(dataset,"dataset.csv")