from svmutil import *


def SVMTrain(trainLabel, trainFeatureVectors, modelFilename):
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model = svm_train(trainLabel, trainFeatureVectors, '-c 0.005 -h 0 -t 0')
    print "Model created. Saving..."

    """Save model"""
    svm_save_model(modelFilename, model)
    print "Model Saved. Proceed to test..."


def SVMTest(testLabel, testFeatureVectors, modelFilename):
    model = svm_load_model(modelFilename)
    print "Model loaded."

    predictedLabel, predictedAcc, predictedValue = \
        svm_predict(testLabel, testFeatureVectors, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]
    return predictedLabel