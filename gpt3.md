要在Streamlit页面上同时显示代码及其说明，你可以使用Streamlit的`st.code`来展示代码块，以及使用markdown或`st.write`来提供文本说明。下面我调整了原有的代码示例，加入了代码展示和文本说明的部分。

```python
# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Streamlit page configuration
st.title('Bird Data Analysis')
# Introduction in markdown
st.markdown("""
This app provides a basic analysis of bird data, showcasing data loading, presenting a dataframe, and creating visualizations including a scatter plot and a histogram.
""")
# Code and Description for Loading Data
st.header('Load Data')
code_load_data = """
birds = pd.read_csv('https://static-1300131294.cos.ap-shanghai.myqcloud.com/data/birds.csv')
"""
st.code(code_load_data, language='python')
st.write('Loaded bird data from a CSV file available on an online URL. Below are the first few rows of the dataframe:')
# Load the data
birds = pd.read_csv('https://static-1300131294.cos.ap-shanghai.myqcloud.com/data/birds.csv')
# Display the first few rows of the dataframe
st.dataframe(birds.head())
# Display and code for scatter plot
st.header('Scatter Plot')
scatter_code = """
fig, ax = plt.subplots(figsize=(12, 8))
birds.plot(kind='scatter', x='MaxLength', y='Order', ax=ax)
plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')
st.pyplot(fig)
"""
st.code(scatter_code, language='python')
st.write('Displaying a scatter plot to show the general distribution of body length per bird order.')
# Plotting the scatter plot
fig, ax = plt.subplots(figsize=(12, 8))
birds.plot(kind='scatter', x='MaxLength', y='Order', ax=ax)
plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')
st.pyplot(fig)
# Display and code for histogram
st.header('Histogram')
histogram_code = """
fig, ax = plt.subplots(figsize=(12, 12))
birds['MaxBodyMass'].plot(kind='hist', bins=10, ax=ax)
plt.title('Distribution of MaxBodyMass')
st.pyplot(fig)
"""
st.code(histogram_code, language='python')
st.write('Showing a histogram to evaluate the distribution of MaxBodyMass across the dataset.')
# Creating the histogram
fig, ax = plt.subplots(figsize=(12, 12))
birds['MaxBodyMass'].plot(kind='hist', bins=10, ax=ax)
plt.title('Distribution of MaxBodyMass')
st.pyplot(fig)
```

这段代码分几个部分为你介绍了如何将数据加载、显示和可视化部分的代码与描述融合在一起，以便为Streamlit app用户提供更为直观和信息丰富的内容。使用`st.markdown`来介绍应用的总体目的，`st.header`来为每一部分设置标题，`st.code`来展示具体的代码片段，以及使用`st.write`或`st.markdown`来添加额外的文本描述。这样，你的Streamlit应用不仅能展示动态的数据分析结果，还能教授使用者背后的代码逻辑。
------------------------------------------------------------------------------





一，简介 (Introduction)

- 1.1 什么是Streamlit
- 1.2 Streamlit的主要优势
- 1.3 Streamlit环境的搭建与基本使用
  二，数据分析可视化 (Data Analysis Visualization)
- 2.1 导入数据及Streamlit展示
- 2.2 数据维度和描述性统计展示
- 2.3 数据分布及相关性分析
- 2.4 交互式数据筛选和展示
  三，机器学习概述 (Overview of Machine Learning)
- 3.1 什么是机器学习
- 3.2 机器学习主要类型：监督学习、无监督学习、半监督学习及强化学习
- 3.3 机器学习模型的训练与评估
  四，监督学习及可视化 (Supervised Learning and Visualization)
- 4.1 分类问题的模型选择及训练
- 4.2 回归问题的模型选择及训练
- 4.3 实时显示模型训练进程和效果
- 4.4 结果的交互式展示
  五，无监督学习及可视化 (Unsupervised Learning and Visualization)
- 5.1 聚类问题的模型选择及训练
- 5.2 降维问题的模型选择及训练
- 5.3 实时显示模型训练进程和效果
- 5.4 结果的交互式展示
  六，深度学习的可视化 (Deep Learning Visualization)
- 6.1 深度学习模型的构建和训练
- 6.2 实时显示训练过程和指标变化
- 6.3 对CNN模型的显示，如显示卷积核或在训练过程中显示图片的特征图
- 6.4 结果的交互式展示
  七，模型优化的可视化 (Model Optimization Visualization)
- 7.1 超参数选择和调整的可视化
- 7.2 交叉验证策略
- 7.3 调优结果的交互式展示
  八，Streamlit app的部署和分享 (Deployment and Sharing of Streamlit App)
- 8.1 如何将你的Streamlit应用部署到公网上
- 8.2 如何和他人分享你的Streamlit应用



----------------------------------------------------------------------------------------------------

BOT：
你的思路是对的，你可以利用Streamlit的侧边栏（sidebar）来添加页面导航，然后将每个页面对应的功能写到不同的页面文件（Python文件）中，然后根据用户在侧边栏的选择来调用不同的页面。以下是你在之前基础上完善的代码：

```python
import importlib
import streamlit as st
# 列出所有的页面
pages = {
 "简介": "intro",
 "数据分析可视化": "data_analysis",
 # 添加更多的页面
}
def main():
 st.set_page_config(page_title="Learn AI more easily", page_icon="👋")
 st.sidebar.title('Navigation')
 st.title("An interactive and visual Machine Learning book")
 # 侧边栏选择页面
 selection = st.sidebar.radio("Go to", list(pages.keys()))
 # 导入选中的页面模块并执行
 page = importlib.import_module(pages[selection])
 page.app()
if __name__ == "__main__":
 main()
```

为每个页面文件创建一个名为`app`的函数，包含改页面所有的代码：

```python
# intro.py
import streamlit as st
def app():
 st.header('简介')
 st.write('这是简介页面的内容...')
```

保存`intro.py`和其他页面文件到`pages`目录下，然后运行homepage.py即可。使用这种方式，所有的页面都有各自的命名空间，不会相互干扰，而且代码结构更清晰。
