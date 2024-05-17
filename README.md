# Data Science Workflow 📊

This guide outlines the key steps in a typical data science workflow, along with common Python commands used at each stage. 

## Install all required libraries via this code

'''
pip install -r https://raw.githubusercontent.com/Wattysaid/data_science/main/requirements.txt
'''

## Steps in Data Science

1. **Data Collection 📥**
   - **Objective**: Gather relevant data from various sources such as databases, APIs, or web scraping.
   - **Commands/Tools**:
     - **APIs**: `requests`, `http.client`
     - **Databases**: `sqlite3`, `pandas.read_sql()`
     - **Web Scraping**: `BeautifulSoup`, `Selenium`

2. **Data Cleaning 🧹**
   - **Objective**: Detect and correct errors or inconsistencies in the data to improve its quality.
   - **Commands/Tools**:
     - **Pandas**: `dropna()`, `fillna()`, `replace()`
     - **Numpy**: `np.nan`, `np.where()`

3. **Data Normalisation ⚖️**
   - **Objective**: Adjust the data to a common scale without distorting differences in the range of values.
   - **Commands/Tools**:
     - **Scikit-learn**: `StandardScaler()`, `MinMaxScaler()`

4. **Data Manipulation 🔄**
   - **Objective**: Transform and prepare data for analysis through sorting, filtering, and aggregating.
   - **Commands/Tools**:
     - **Pandas**: `groupby()`, `pivot_table()`, `merge()`, `concat()`

5. **Data Analysis 🔍**
   - **Objective**: Apply statistical and machine learning techniques to extract insights and make predictions.
   - **Commands/Tools**:
     - **Pandas**: `describe()`, `corr()`
     - **Scikit-learn**: `train_test_split()`, `fit()`, `predict()`
     - **Matplotlib/Seaborn**: `plot()`, `hist()`, `heatmap()`

### Further Reading and Resources 📚

#### Data Manipulation and Analysis
1. **Python for Data Analysis** by Wes McKinney
   - A comprehensive guide on using Pandas for data manipulation.
   - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

#### Machine Learning
2. **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** by Aurélien Géron
   - A practical approach to machine learning with hands-on examples.
   - [Scikit-learn Documentation](https://scikit-learn.org/stable/)

#### Data Science Fundamentals
3. **Data Science from Scratch** by Joel Grus
   - Introduction to data science concepts and techniques for beginners.

#### Data Visualisation
4. **Matplotlib Documentation**
   - Official documentation for Matplotlib, a comprehensive library for creating static, animated, and interactive visualisations in Python.
   - [Matplotlib Documentation](https://matplotlib.org/stable/)
5. **Seaborn Documentation**
   - Official documentation for Seaborn, a Python data visualisation library based on Matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.
   - [Seaborn Documentation](https://seaborn.pydata.org/)

#### Advanced Topics
6. **Deep Learning with Python** by François Chollet
   - A comprehensive guide to deep learning using Python and Keras.

7. **The Elements of Statistical Learning** by Trevor Hastie, Robert Tibshirani, and Jerome Friedman
   - A detailed and technical guide on statistical learning and machine learning techniques.

8. **Pattern Recognition and Machine Learning** by Christopher M. Bishop
   - An in-depth textbook on pattern recognition and machine learning, providing both theoretical and practical perspectives.
