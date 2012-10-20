#!/usr/bin/env python
# encoding: utf-8

# An Artificial Neural Network
# Scott Young - CSC 578 - Oct. 2012

import sys
from optparse import OptionParser

class NeuralNet(object):
    """ An artificial neural network """

    def __init__(self, eta, error_margin, max_epochs, weight):
        """ Constructor """

        self.eta = eta                      # learning rate
        self.error_margin = error_margin    
        self.max_epochs = max_epochs        
        self.max_weight = weight
        self.min_weight = -weight

    def train(self):

        # dictionary for output
        data = {}
        data[epoch] = 1
        data[max_RMSE] = .5
        data[ave_RMSE] = .5
        data[correct] = 80

        output(data)

# Helper Function
def output(data):
    """ Output the information for each epoch to the screen. """

    print ("***** Epoch " + data[epoch] + " *****")
    print ("Maximum RMSE: " + data[max_RMSE])
    print ("Average RMSE: " + data[ave_RMSE])
    print ("Percent Correct: " + data[correct] + "%")

def main():
    """ Run program from the command line. """

    # hard code initial values for testing
    eta = 0.1
    error_margin = .05
    max_epochs = 100
    weight = 5;

    # initialize network based upon parameters
    ann = NeuralNet(eta, error_margin, max_epochs, weight)
    ann.train


if __name__ == "__main__":
    """ enable command line execution """
    sys.exit(main())
