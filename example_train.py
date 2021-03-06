import os
import tensorflow as tf
form tensorflow.examples.tutorials.mnist import input_data

import mnist_inference
#配置神经网络的参数
BATCH_SIZE=100
LEARNING_RATE_BASE=0.8
LEARNING_RATE_DECAY=0.99
REGULARAZTION_RATE=0.0001
TRAING_STEPS=30000
MOVING_AVERAGE_DECAY=0.99
#模型保存的路径和文件名
MODEL_SAVER_PATH="..."
MODEL_NAME="model.ckpt"

def train(mnist):
	#定义输入输出placeholder
	x=tf.placeholder(tf.float32,[None,mnist_inference.INPUT_NODE],name='x-input')
	y_=tf.placeholder(tf.float32,[Npne,mnist_inference.OUTPUT_NODE],name='y-input')
	regularizer=tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)
	y=mnist_inference.inference(x,regularizer)
	global_step=tf.Variable(0,trainable=False)
	
	variable_averages=tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
	variable_averages_op=variable_averages.apply(tf.trainable_variables())
	cross_entropy_mean=tf.nn.sparse_softmax_cross_entropy_with_logits(y,tf.argmax(y_,1))
	cross_entropy_mean=tf.reduce_mean(cross_entropy)
	loss=cross_entropy_mean+tf.add_n(tf.get_collection('losses'))
	learning_rate=tf.train.exponential_decay(LEARNING_RATE_BASE,global-step,mnist.train.num_examples/BATCH_SEZE,LEARNING_RATE_DECAY)
	train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)
	with tf.control_dependencies([train_step,variables_averages_op]):
		train_op=tf.no_op(name='train')
	#初始化Tensorflow持久化类
	saver=tf.train.Saver()
	with tf.Session() as sess:
		init=tf.global_variables_initializer()
		sess.run(init)
		for i in range(TRAINING_STEPS):
			xs,ys=mnist.train.next_batch(BATCH_SIZE)
			_,loss_value,step=sess.run([train_op,loss,global_step],feed_dict={x:xs,y_ys})
			#每1000轮保存一次模型
			if i %1000==0:
				#输出当前的训练情况。这里只输出了模型在当前训练batch上的损失函数
				#的大小。通过损失函数的大小可以大概了解训练的情况。在验证数据集上
				#的正确率信息会有个一单独的程序来生成。
				print("after {} training steps,loss on traing batch is {}").format(step,loss_value)
				#保存当前的模型。注意这里给出了global_step参数，这样可以让每个被保存模型的文件名末尾加上训练的
				#轮数，比如“model.ckpt-1000”
				saver.save(sess,os.path.join(MODEL_SAVE_PATH,MODEL_NAME),global_step=global_step)
def main(argb=None):
	mnist=input_data.read_data_sets("/tem/data",one_hot=True)
	train(mnist)
if __name__=='__main__':
	tf.app.run()
