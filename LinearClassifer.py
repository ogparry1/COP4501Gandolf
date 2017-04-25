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
    trainingSet=trainingSet.drop('class',1)
    weightMatrix=np.linalg.inv(np.transpose(trainingSet).dot(trainingSet)-error).dot(np.transpose(trainingSet)).dot(trainingValidationSet)
    return weightMatrix
def test(weightMatrix,testSet,testValidation):
    testingSet=testingSet.drop('class',1)
    predictionSet=testingSet.dot(weightMatrix)
    predictionOutputSet=np.zeros((1,len(testingSet)))
    trueOutputSet=np.zeros((1,len(testingSet)))
    i=0
    for index, row in predictionSet.iterrows():
        predictionOutputSet[0][i]=row.idxmax(1)
        i=i+1
    i=0
    for index, row in testingValidationSet.iterrows():
        j=0
        for columns in row:
            if(columns==1):
                trueOutputSet[0][i]=j
            j=j+1
        i=i+1
    return predictionOutputSet,trueOutputSet
def crossValidation(weightMatrix,testSet,testValidation):
    return 0

trainingSet,testingSet=createTrainingTestSets('IrisInfo.txt',50)
trainingValidationSet=createTrainingValidationSet(trainingSet,['Iris-setosa','Iris-versicolor','Iris-virginica'])
testingValidationSet=createTestValidationSet(testingSet,['Iris-setosa','Iris-versicolor','Iris-virginica'])
weightMatrix=train(trainingSet,trainingValidationSet,0)
predictionOutputSet,trueOutputSet=test(weightMatrix,testingSet,testingValidationSet)
print(predictionOutputSet)
print(trueOutputSet)
