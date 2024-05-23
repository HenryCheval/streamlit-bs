import streamlit as st
import pickle
import numpy as np

@st.cache_data
def load_model():
    with open('data/saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("使用决策树回归预测薪水")

    st.write("""#### 现在，我们可以利用得到的数据预测薪水""")
    st.write("""#### 输入信息进行预测""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "学士学位以下",
        "学士学位",
        "硕士学位",
        "博士及以上",
    )
    
    def convert(chinese_education):
     if chinese_education == "学士学位以下":
        return "Less than a Bachelors"
     elif chinese_education == "学士学位":
        return "Bachelor’s degree"
     elif chinese_education == "硕士学位":
        return "Master’s degree"
     elif chinese_education == "博士及以上":
        return "Post grad"
     else:
        return None

    country = st.selectbox("国家", countries)
    education = st.selectbox("教育水平", education)
    education_en = convert(education)
    expericence = st.slider("工作经验年限", 0, 50, 3)

    X = np.array([[country, education_en, expericence ]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X = X.astype(float)

    salary = regressor.predict(X)
    st.info(f"预计薪水为 ${salary[0]:.2f}")


show_predict_page()
st.write("""
\n\n决策树是一种流行的机器学习算法，它既可以用于分类也可以用于回归任务。在回归问题中，决策树的目标是预测一个连续的数值输出，比如薪资预测。

决策树通过递归地将数据集分割成子集（节点），直到满足某个停止条件，比如节点中的样本足够纯（相似）或者达到预设的树的最大深度。每个内部节点表示一个特征上的测试，分支代表测试结果，而叶节点则代表预测的输出值。
在薪资预测场景中，决策树回归模型可以分析诸如工作经验、教育水平、国家、行业等多种特征，然后根据这些特征的重要性做出决策，最终预测个人的薪资水平。它能够识别哪些特征对薪资的影响最大，从而帮助我们理解薪资分布的驱动因素。
\n**关键概念包括：**\n
- **分裂准则**：常见的分裂标准有均方差减少（MSE）、信息增益等。
- **剪枝**：避免过拟合，包括预剪枝和后剪枝。
- **特征选择**：根据信息增益或其他指标选择最有区分度的特征进行分裂。
""")

st.image('data/decision tree.png', caption='决策树回归模型', use_column_width=True)