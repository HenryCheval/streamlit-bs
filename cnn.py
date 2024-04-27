import streamlit as st
import streamlit.components.v1 as components

# 定义HTML内容
html_content = """
<p style="text-align: center;">
<iframe src="https://static-1300131294.cos.ap-shanghai.myqcloud.com/html/cnn-vis-3/index.html" width="100%" height="600px;"
style="border:none;" scrolling="auto"></iframe>
A demo of CNN. <a
href="https://poloclub.github.io/cnn-explainer/"> [source]</a>
</p>
"""

# 使用 Streamlit 的 HTML 组件来展示内容
components.html(html_content, height=620)