import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
# 加载MNIST数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 数据预处理
x_train = x_train.reshape(-1, 784).astype("float32") / 255
x_test = x_test.reshape(-1, 784).astype("float32") / 255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
# 创建模型
model = Sequential([
 Dense(128, activation="relu"),
 Dense(10, activation="softmax")
])
model.compile(optimizer='adam',
 loss='categorical_crossentropy',
 metrics=['accuracy'])
# 准备TensorBoard
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=1)
# 训练模型
model.fit(x_train, y_train, epochs=5, validation_split=0.2, callbacks=[tensorboard_callback])