import pandas as pd
import numpy as np
import random
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score

def createTrainingTestSets(fileName, numberOfEntriesForTrainingSet,seed):
    np.random.seed(seed)
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

def train(trainingSet,trainingValidationSet,error):
    trainingSet=trainingSet.drop('class',1)
    weightMatrix=np.linalg.inv(np.transpose(trainingSet).dot(trainingSet)-error).dot(np.transpose(trainingSet)).dot(trainingValidationSet)
    return weightMatrix

def test(weightMatrix,testingSet,testingValidationSet):
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
    return trueOutputSet,predictionOutputSet
def findError(trueOutputSet,predictedOutputSet):
    error=0
    for i in range(0,len(trueOutputSet[0])):
        if(trueOutputSet[0][i]!=predictedOutputSet[0][i]):
            error=error+1
    return error/len(trueOutputSet[0])
def confuseMatrix(true, predict):
   confused = confusion_matrix(true[0, :], predict[0, :])
   precision = precision_score(true[0, :], predict[0, :], average = None)
   return confused, precision

def findOptimumTrainingSet(fileName,classIdentifiers,numberOfEntriesForTrainingSet,numberOfIterations):
    minimumErrorTrainingSet=0
    minimumErrorTestSet=0
    minimumError=1
    confusionMatrix=0
    precision_score=0
    freeParameter=0
    for i in range(0,numberOfIterations):
        print('Iteration '+str(i)+' of '+str(numberOfIterations))
        trainingSet,testingSet=createTrainingTestSets(fileName,numberOfEntriesForTrainingSet,random.randint(0,numberOfIterations*numberOfIterations))
        trainingValidationSet=createTrainingValidationSet(trainingSet,classIdentifiers)
        testingValidationSet=createTestValidationSet(testingSet,classIdentifiers)
        for j in range(0,100,2):
            weightMatrix=train(trainingSet,trainingValidationSet,j/100)
            trueOutputSet, predictionOutputSet = test(weightMatrix, testingSet, testingValidationSet)
            currentError=findError(trueOutputSet,predictionOutputSet)
            if(currentError<minimumError):
                minimumError = currentError
                minimumErrorTrainingSet=trainingSet
                minimumErrorTestSet=testingSet
                freeParameter=i
                confusionMatrix,precision_score=confuseMatrix(trueOutputSet,predictionOutputSet)
    return minimumErrorTrainingSet,minimumErrorTestSet,freeParameter,confusionMatrix,precision_score

dataText='IrisInfo'
classesToIdentify=['Iris-setosa','Iris-versicolor','Iris-virginica']
sampleSize=20
numberOfIterations=50
trainingSet,testSet,freeParameter,confusionMatrix,precision_score=findOptimumTrainingSet(dataText,classesToIdentify,sampleSize,numberOfIterations)
trainingSet.to_csv(dataText+'_trainingSet',sep='\t')
testSet.to_csv(dataText+'_testSet',sep='\t')
np.savetxt(dataText+'_confusionMatrix',confusionMatrix,delimiter=',')
np.savetxt(dataText+'_precision_score',precision_score,delimiter=',')
print('FreeParameter: '+str(freeParameter/100))
