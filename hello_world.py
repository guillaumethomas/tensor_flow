import tensorflow as tf

# Hello World from GPU

if __name__ == "__main__":
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))