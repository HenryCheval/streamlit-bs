import streamlit as st
import subprocess
import os
# Streamlit界面
st.title('机器学习训练可视化')
st.write('这是一个展示如何利用Streamlit和TensorBoard可视化机器学习训练过程的教学文件。')
# TensorBoard启动
LOG_DIR = 'logs'
if st.button('启动TensorBoard'):
 # 清理旧的TensorBoard进程
 os.system('kill (ps aux | grep \'tensorboard\' | awk \'{print2}\')')

# 启动新的TensorBoard进程
 subprocess.Popen(['tensorboard', '--logdir', LOG_DIR, '--bind_all'])
 st.text('TensorBoard已启动！')
# 嵌入TensorBoard到Streamlit
tensorboard_url = 'http://localhost:6006/'
st.components.v1.iframe(tensorboard_url, width=800, height=600, scrolling=True)