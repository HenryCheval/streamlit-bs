#import streamlit as st

#st.set_page_config(
#    page_title="Learn AI more easily",
#    page_icon="👋",
#)

#st.title("An interactive and visual Machine Learning book")
#st.sidebar.success("Select a page above.")
import importlib
import streamlit as st
def main():
 st.sidebar.title('Navigation')
 st.title("An interactive and visual Machine Learning book")

markdown_text = """
# 课程大纲
## 一简介 (Introduction)
- 1.1 什么是Streamlit
- 1.2 Streamlit的主要优势
- 1.3 Streamlit环境的搭建与基本使用
## 二 数据分析可视化 (Data Analysis Visualization)
- 2.1 导入数据及Streamlit展示
- 2.2 数据维度和描述性统计展示
- 2.3 数据分布及相关性分析
- 2.4 交互式数据筛选和展示
## 三 机器学习概述 (Overview of Machine Learning)
- 3.1 什么是机器学习
- 3.2 机器学习主要类型：监督学习、无监督学习、半监督学习及强化学习
- 3.3 机器学习模型的训练与评估
## 四 监督学习及可视化 (Supervised Learning and Visualization)
- 4.1 分类问题的模型选择及训练
- 4.2 回归问题的模型选择及训练
- 4.3 实时显示模型训练进程和效果
- 4.4 结果的交互式展示
## 五 无监督学习及可视化 (Unsupervised Learning and Visualization)
- 5.1 聚类问题的模型选择及训练
- 5.2 降维问题的模型选择及训练
- 5.3 实时显示模型训练进程和效果
- 5.4 结果的交互式展示
## 六 深度学习的可视化 (Deep Learning Visualization)
- 6.1 深度学习模型的构建和训练
- 6.2 实时显示训练过程和指标变化
- 6.3 对CNN模型的显示，如显示卷积核或在训练过程中显示图片的特征图
- 6.4 结果的交互式展示
## 七 模型优化的可视化 (Model Optimization Visualization)
- 7.1 超参数选择和调整的可视化
- 7.2 交叉验证策略
- 7.3 调优结果的交互式展示
"""
# 用streamlit展示markdown文本
st.markdown(markdown_text)

if __name__ == "__main__":
 #st.set_page_config(page_title="Learn AI more easily", page_icon="👋")
 main()