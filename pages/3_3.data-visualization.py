# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# intro.py
import streamlit as st
def app():
 st.header('简介')
 st.write('这是简介页面的内容...')

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


# Change bins to 30
st.header('Histogram with Increased Bins')
st.markdown("""
As observed, most of the 400+ birds have a Max Body Mass under 2000. Let's gain deeper insight by increasing the `bins` parameter to 30.
""")
code_hist_bins_30 = """
birds['MaxBodyMass'].plot(kind='hist', bins=30, figsize=(12, 12))
plt.show()
"""
st.code(code_hist_bins_30, language='python')

# Plot with bins=30
fig, ax = plt.subplots(figsize=(12, 12))
birds['MaxBodyMass'].plot(kind='hist', bins=30, ax=ax)
plt.title('MaxBodyMass Distribution with 30 Bins')
st.pyplot(fig)

# Filter data and increase bins to 40
st.header('Filtered Data Histogram')
st.markdown("""
Filtering the data to get only those birds whose body mass is under 60, and showing the distribution with 40 `bins`.
""")
code_filtered_40_bins = """
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]
filteredBirds['MaxBodyMass'].plot(kind='hist', bins=40, figsize=(12, 12))
plt.show()
"""
st.code(code_filtered_40_bins, language='python')

# Apply filtering and plot
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]
fig, ax = plt.subplots(figsize=(12, 12))
filteredBirds['MaxBodyMass'].plot(kind='hist', bins=40, ax=ax)
plt.title('Filtered MaxBodyMass with 40 Bins')
st.pyplot(fig)

# 2D Histogram
st.header('2D Histogram')
st.markdown("""
Creating a 2D histogram to compare the relationship between `MaxBodyMass` vs. `MaxLength`. This visualization uses brighter colors to show points of higher convergence.
""")
code_hist2d = """
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
plt.show()
"""
st.code(code_hist2d, language='python')

# Plot 2D histogram
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
plt.title('2D Histogram of MaxBodyMass vs MaxLength')
st.pyplot(fig)