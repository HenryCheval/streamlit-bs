BOT：
是的，你完全可以仅使用 Streamlit 来可视化你的机器学习训练过程，而无需依赖 TensorBoard。Streamlit 本身提供了非常丰富的方式来呈现数据和训练过程的进度。以下是一种简单的方式，通过修改你的代码来使用 Streamlit 直接显示训练过程中的一些关键指标（如损失和准确度）：

1. **安装 Streamlit（如果还未安装）**
   
   ```bash
   pip install streamlit
   ```
2. **修改代码以使用 Streamlit**
   我们将使用一个自定义的回调函数来在每个 epoch 结束时更新 Streamlit 界面，而不是使用TensorBoard。
   这里有一个修改后的示例：
   
   ```python
   import numpy as np
   import tensorflow as tf
   from sklearn.model_selection import train_test_split
   from tensorflow.keras.datasets import mnist
   from tensorflow.keras.models import Sequential
   from tensorflow.keras.layers import Dense
   from tensorflow.keras.utils import to_categorical
   import streamlit as st
   # 加载 MNIST 数据集
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
   model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
   # 自定义 Streamlit 回调
   class StreamlitCallback(tf.keras.callbacks.Callback):
   def on_epoch_end(self, epoch, logs=None):
   st.write(f"Epoch: {epoch + 1}, Loss: {logs['loss']}, Acc: {logs['accuracy']}, Val Loss: {logs['val_loss']}, Val Acc: {logs['val_accuracy']}")
   # 在 Streamlit 应用中运行
   def run_app():
   st.title('模型训练')
   if st.button('开始训练模型'):
   # 训练模型
   model.fit(x_train, y_train, epochs=5, validation_split=0.2, callbacks=[StreamlitCallback()])
   if __name__ == '__main__':
   run_app()
   ```
   
   在这段代码中，我们首先引入了 Streamlit，然后创建了一个 `StreamlitCallback` 类，该类继承自 TensorFlow 的 `Callback` 类。在每个 epoch 结束时，它通过 Streamlit 的 `st.write()` 方法输出训练进度。
   通过这种方式，你可以直接在 Streamlit 应用中查看训练过程和结果，而无需额外使用 TensorBoard。此外，Streamlit 允许你创建非常丰富和交互式的应用界面，包括图表和其他可视化元素，从而提供一种强大的方式来展示你的机器学习模型和数据。
   要运行这个 Streamlit 应用，请确保将上述代码保存到一个 Python 文件中，然后在命令行中使用 Streamlit 命令运行该文件，比如：
   
   ```bash
   streamlit run your_script_name.py
   ```
   
   替换 `your_script_name.py` 为你的实际 Python 脚本文件名。这样，你就可以在 Streamlit 应用中看到模型训练过程的实时信息了。

----------------------------------------------------------------------------------------------------
