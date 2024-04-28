import streamlit as st
import numpy as np

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

st.title('Streamlit 示例 - 探索分类器性能')

st.write("""
# 探索不同的分类器和数据集
看看哪个分类器对于特定数据集表现最佳。
""")

### 选择数据集
dataset_name = st.selectbox(
    '选择数据集',
    ('鸢尾花', '乳腺癌', '葡萄酒'),
    help="请选择一个数据集，我们将用不同的分类器对其进行分类。"
)

st.write(f"您选择了 {dataset_name} 数据集。")

### 选择分类器
classifier_name = st.selectbox(
    '选择分类器',
    ('KNN', 'SVM', '随机森林'),
    help="请选择一个分类器。不同的分类器将直接影响模型的性能。"
)

def get_dataset(name):
    if name == '鸢尾花':
        data = datasets.load_iris()
    elif name == '葡萄酒':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    X = data.data
    y = data.target
    return X, y

X, y = get_dataset(dataset_name)
st.write(f'数据集形状: {X.shape}')
st.write(f'类别数: {len(np.unique(y))}')

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'SVM':
        C = st.slider('C (SVM正则化参数)', 0.01, 10.0, help="C参数控制错误项的惩罚程度。较大的C给予错误分类更大的惩罚，寻求通过最大化边界来优化分类器。")
        params['C'] = C
    elif clf_name == 'KNN':
        K = st.slider('K (邻居数)', 1, 15, help="K代表考虑的最近邻居的数量。较小的K意味着噪声将对结果有更大影响，而较大的K使其更加稳定，但可能导致分类边界不够清晰。")
        params['K'] = K
    else: # 随机森林
        max_depth = st.slider('最大深度', 2, 15, help="树的最大深度。更深的树可以捕捉更复杂的模式，但也更容易过拟合。")
        params['max_depth'] = max_depth
        n_estimators = st.slider('树的数量', 1, 100, help="森林中树的数量。更多的树可以提高模型的性能，但会增加计算成本。")
        params['n_estimators'] = n_estimators
    return params

params = add_parameter_ui(classifier_name)

def get_classifier(clf_name, params):
    if clf_name == 'SVM':
        clf = SVC(C=params['C'])
    elif clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'], 
                                     max_depth=params['max_depth'], random_state=1234)
    return clf

clf = get_classifier(classifier_name, params)

### 分类与性能评估
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)

st.write(f'分类器: {classifier_name}')
st.write(f'准确度: {acc}')

### 数据集可视化
pca = PCA(2)
X_projected = pca.fit_transform(X)
x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')
plt.xlabel('主成分 1')
plt.ylabel('主成分 2')
plt.colorbar()
st.pyplot(fig)