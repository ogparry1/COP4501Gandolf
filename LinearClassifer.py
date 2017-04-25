import pandas as pd
import numpy as np
def createTrainingTestSets(fileName, numberOfEntriesForTrainingSet):
    np.random.seed(42)
    dataSet = pd.read_csv(fileName)
    train_ix = np.random.choice(dataSet.index, numberOfEntriesForTrainingSet, replace=False)
    dataSet_training = dataSet.ix[train_ix]
    dataSet_test = dataSet.drop(train_ix)
    return dataSet_training,dataSet_test

def createTrainingValidationSet(dataSet,classIdentifiers):
    trainingValidationSet=pd.DataFrame(np.zeros((len(dataSet),len(classIdentifiers))))
    i=0
    for index, row in dataSet.iterrows():
        for j in range(0,len(classIdentifiers)):
            if(row['class']==classIdentifiers[j]):
                trainingValidationSet.xs(i)[j]=1
        i=i+1
    return trainingValidationSet

def createTestValidationSet(dataSet,classIdentifiers):
    testValidationSet = pd.DataFrame(np.zeros((len(dataSet), len(classIdentifiers))))
    i = 0
    for index, row in dataSet.iterrows():
        for j in range(0, len(classIdentifiers)):
            if (row['class'] == classIdentifiers[j]):
                testValidationSet.xs(i)[j] = 1
        i=i+1
    return testValidationSet

def train(trainingSet,trainingValidation):
    return 0
def test(weightMatrix,testSet,testValidation):
    return 0
def crossValidation(weightMatrix,testSet,testValidation):
    return 0

trainSet,testingSet=createTrainingTestSets('IrisInfo.txt',10)
trainingValidationSet=createTrainingValidationSet(trainSet,['Iris-setosa','Iris-versicolor','Iris-virginica'])
testingValidationSet=createTestValidationSet(testingSet,['Iris-setosa','Iris-versicolor','Iris-virginica'])
print(trainingValidationSet)
print(testingValidationSet)