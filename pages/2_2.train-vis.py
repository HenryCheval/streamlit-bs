import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import streamlit as st
import matplotlib.pyplot as plt

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

# 自定义Streamlit回调，收集训练数据
class StreamlitCallback(tf.keras.callbacks.Callback):
    def __init__(self):
        super(StreamlitCallback, self).__init__()
        self.loss = []
        self.accuracy = []
        self.val_loss = []
        self.val_accuracy = []

    def on_epoch_end(self, epoch, logs=None):
        self.loss.append(logs['loss'])
        self.accuracy.append(logs['accuracy'])
        self.val_loss.append(logs['val_loss'])
        self.val_accuracy.append(logs['val_accuracy'])
        st.write(f"Epoch: {epoch + 1}, Loss: {logs['loss']}, Acc: {logs['accuracy']}, Val Loss: {logs['val_loss']}, Val Acc: {logs['val_accuracy']}")

        # 绘图
        fig, ax = plt.subplots(1, 2, figsize=(10, 4))
        ax[0].plot(self.loss, label='train_loss')
        ax[0].plot(self.val_loss, label='val_loss')
        ax[0].set_xlabel('Epoch')
        ax[0].set_ylabel('Loss')
        ax[0].legend()
        
        ax[1].plot(self.accuracy, label='train_accuracy')
        ax[1].plot(self.val_accuracy, label='val_accuracy')
        ax[1].set_xlabel('Epoch')
        ax[1].set_ylabel('Accuracy')
        ax[1].legend()
        
        st.pyplot(fig)

# 在Streamlit中运行
def run_app():
    st.title('模型训练可视化')

    if st.button('开始训练模型'):
        callback = StreamlitCallback()
        model.fit(x_train, y_train, epochs=5, validation_split=0.2, callbacks=[callback])

if __name__ == '__main__':
    run_app()