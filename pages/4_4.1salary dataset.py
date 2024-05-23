import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# 页面标题
st.title("数据处理与可视化应用")
st.write("""
本章我们会处理一个数据样本表格，后续运用这里的数据使用决策树回归进行薪资预测。

""")

st.write("""
## 用于预测的数据样本展示
#### 数据源于Stack Overflow在2020年调查的开发者薪水情况\n
##### [来源](https://survey.stackoverflow.co/)
          
 
""")
st.write("""
由于数据量庞大，无法直接用于薪资预测，我们需要使用pandas修剪并保留主要国家与中位数附近的样本.
""")
def display_code_and_result(code, result=None, caption=""):
    st.code(code, language='python')
    if result is not None:
        st.write(f"**{caption}:**")
        st.write(result)

uploaded_file = pd.read_csv("data/survey_results_public.csv")

if uploaded_file is not None:

    df = uploaded_file
    # 展示DataFrame的前几行数据
    code = "df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedComp']]"
    st.code(code, language='python')
    if st.button("显示数据预览"):
        st.write(df.head())

    # 选择感兴趣的列
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)

    

    # 删除Salary列中包含缺失值的行
    st.write("删除Salary列中包含缺失值的行:")
    code= "df = df[df[\"Salary\"].notnull()]"
    st.code(code, language='python')
    df = df[df["Salary"].notnull()]

    # 删除所有包含缺失值的行
    st.write("删除所有包含缺失值的行:")
    df = df.dropna()
    st.code("df = df.dropna()", language='python')

    # 仅保留“Employed full-time”行
    st.write("仅保留“Employed full-time”行:")
    code="""
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)
    """
    st.code(code, language='python')
    st.write("\n\n\n\n")
    # 显示国家数量
    st.write("显示国家数量")
    code="df['Country'].value_counts()"
    st.code(code, language='python')    
    if st.button("查看国家数量分布"):
        st.write(df['Country'].value_counts())

    # 简化国家类别
    st.write("简化国家类别:")
    code="""
    def shorten_categories(categories, cutoff):
        categorical_map = {k: ('Other' if v < cutoff else k) for k, v in categories.items()}
        return categorical_map
    """
    st.code(code, language='python')
    def shorten_categories(categories, cutoff):
        categorical_map = {k: ('Other' if v < cutoff else k) for k, v in categories.items()}
        return categorical_map

    country_map = shorten_categories(dict(df['Country'].value_counts()), 400)
    df['Country'] = df['Country'].map(country_map)

    # 更新后的国家数量分布
    if st.button("查看简化后的国家数量分布"):
        st.write(df.Country.value_counts())

    # 创建箱线图
    if st.button("绘制薪资与国家关系箱线图"):
        fig, ax = plt.subplots(figsize=(12, 7))
        df.boxplot('Salary', 'Country', ax=ax)
        plt.suptitle('relationship between wages and countries')
        plt.ylabel('Salary')
        plt.xticks(rotation=90)
        st.pyplot(fig)

    # 进一步数据清洗
    st.write("进一步数据清洗")
    code="""
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']
    """
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']

    # 清洗YearsCodePro列
    st.write("清洗YearsCodePro列")
    code="""
    def clean_experience(x):
        if x == 'More than 50 years':
            return 50
        if x == 'Less than 1 year':
            return 0.5
        return float(x)

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    """
    st.code(code, language='python')  
    def clean_experience(x):
        if x == 'More than 50 years':
            return 50
        if x == 'Less than 1 year':
            return 0.5
        return float(x)

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)

    # 清洗EdLevel列
    st.write("清洗EdLevel列")
    code="""
    def clean_education(x):
        if 'Bachelor’s degree' in x:
            return '学士学位'
        if 'Master’s degree' in x:
            return '硕士学位'
        if 'Professional degree' in x or 'Other doctoral' in x:
            return '研究生以上'
        return '学士以下'

    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    """
    st.code(code, language='python')  
    def clean_education(x):
        if 'Bachelor’s degree' in x:
            return '学士学位'
        if 'Master’s degree' in x:
            return '硕士学位'
        if 'Professional degree' in x or 'Other doctoral' in x:
            return '研究生以上'
        return '学士以下'

    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    # 将类别转换为数值
    st.write("将类别转换为数值")
    code="""
    le_country = LabelEncoder()
    le_education = LabelEncoder()
    df['Country'] = le_country.fit_transform(df['Country'])
    df['EdLevel'] = le_education.fit_transform(df['EdLevel'])
    """
    st.code(code, language='python')  
    le_country = LabelEncoder()
    le_education = LabelEncoder()
    df['Country'] = le_country.fit_transform(df['Country'])
    df['EdLevel'] = le_education.fit_transform(df['EdLevel'])

    # 显示最终处理后的数据信息
    if st.button("查看最终数据信息"):
        st.write(df)

