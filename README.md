# Data Science Workflow 📊

This guide outlines the key steps in a typical data science workflow, along with common Python commands used at each stage. 

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

