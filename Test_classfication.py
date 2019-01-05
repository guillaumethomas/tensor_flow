# Based on this tutorial https://www.tensorflow.org/tutorials/keras/basic_text_classification
import tensorflow as tf
from tensorflow import keras

import numpy as np


def main():

    version = tf.__version__
    print('\nTensor Flow version {}\n'.format(version))

    # DataSet
    imdb = keras.datasets.imdb
    (train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

    #Data Exploration
    print("Training entries: {}, labels: {}".format(len(train_data), len(train_labels)))


if __name__ == "__main__":
    main()


