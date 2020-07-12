import tensorflow as tf 
import numpy as np
tf.reset_default_graph()
y_ = tf.get_collection_ref("fc2_output")[0]
saver = tf.train.import_meta_graph('../model/model.ckpt.meta')
#saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, "../model/model.ckpt")
    p_y = np.argmax(sess.run(y_,feed_dict={x: test_x,keep_prob: 1.0}),1)

