import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold


seed = 123
numpy.random.seed(seed)
# load dataset
dataframe = pandas.read_csv(“dataset.csv”, header=None)
dataset = dataframe.values
X = dataset[:,0:36].astype(float)
Y = dataset[:,36]
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

#  one hot encoding
one_hot = np_utils.to_categorical(encoded_Y)

train_x, test_x, train_y, test_y = train_test_split(X,Y, test_size = 0.3, random_state = 0)
train_x.shape, train_y.shape, test_x.shape, test_y.shape

# define baseline model
def baseline_model():
# create model
in_dim = len(dataset.columns)-1

model = Sequential()
model.add(Dense(8, input_dim = in_dim, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(train_x, train_y, epochs = 400, batch_size = 5)
scores = model.evaluate(test_x, test_y)

for i, m in enumerate(model.metrics_names):
    print("\n%s: %.3f"% (m, scores[i]))
# Compile model
model.compile(loss=’categorical_crossentropy’, optimizer=’adam’, metrics=[‘accuracy’])
return model


kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(estimator, X, one_hot, cv=kfold)
print(“Baseline: %.2f%% (%.2f%%)” % (results.mean()*100, results.std()*100))

X_train, X_test, Y_train, Y_test = train_test_split(X, one_hot, test_size=0.55, random_state=seed)
estimator.fit(X_train, Y_train)
predictions = estimator.predict(X_test)

print(predictions)