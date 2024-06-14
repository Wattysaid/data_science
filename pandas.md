# Useful Pandas Functions for Data Cleaning

## Data Inspection

### Description
Data inspection involves examining your dataset to understand its structure, contents, and summary statistics. This process helps in identifying data types, missing values, and basic trends, which are crucial for data cleaning and analysis.

### Functions and Examples

- **`.head(n)`**: Displays the first `n` rows of the DataFrame.
  - *Example*: `df.head(5)` shows the first 5 rows of `df`.
  - *Example*: `df.head(10)` shows the first 10 rows of `df`.
- **`.tail(n)`**: Displays the last `n` rows of the DataFrame.
  - *Example*: `df.tail(5)` shows the last 5 rows of `df`.
  - *Example*: `df.tail(10)` shows the last 10 rows of `df`.
- **`.info()`**: Provides a concise summary of the DataFrame, including the number of non-null entries.
  - *Example*: `df.info()` provides a summary of `df`.
  - *Example*: `df[['column1', 'column2']].info()` provides a summary of specific columns.
- **`.describe()`**: Generates descriptive statistics for numerical columns.
  - *Example*: `df.describe()` gives statistics like mean, median, and standard deviation.
  - *Example*: `df[['column1', 'column2']].describe()` gives statistics for specific columns.
- **`.shape`**: Returns the dimensions of the DataFrame (rows, columns).
  - *Example*: `df.shape` returns the shape of `df`.
  - *Example*: `df[['column1', 'column2']].shape` returns the shape of specific columns.
- **`.dtypes`**: Displays the data types of each column.
  - *Example*: `df.dtypes` shows data types of all columns.
  - *Example*: `df['column1'].dtypes` shows the data type of a specific column.

## Handling Missing Data

### Description
Handling missing data is critical in data cleaning to ensure the dataset's completeness and reliability. Different techniques are used to either remove or fill in missing values based on the analysis requirements.

### Functions and Examples

- **`.isnull()`**: Detects missing values, returning a DataFrame of the same shape with boolean values.
  - *Example*: `df.isnull()` returns a DataFrame indicating missing values.
  - *Example*: `df['column1'].isnull()` checks for missing values in a specific column.
- **`.notnull()`**: Detects non-missing values, returning a DataFrame of the same shape with boolean values.
  - *Example*: `df.notnull()` returns a DataFrame indicating non-missing values.
  - *Example*: `df['column1'].notnull()` checks for non-missing values in a specific column.
- **`.dropna(axis, how, thresh, subset)`**: Removes missing values.
  - *Example*: `df.dropna(axis=0, how='any')` removes rows with any null values.
  - *Example*: `df.dropna(axis=1, how='all')` removes columns with all null values.
- **`.fillna(value, method)`**: Fills missing values.
  - *Example*: `df.fillna(0)` fills all missing values with 0.
  - *Example*: `df.fillna(method='ffill')` fills missing values with the previous value.

## Data Transformation

### Description
Data transformation involves modifying data to make it suitable for analysis. This can include applying functions, mapping values, replacing values, and changing data types.

### Functions and Examples

- **`.apply(function)`**: Applies a function along an axis of the DataFrame.
  - *Example*: `df.apply(np.sqrt)` applies the square root function to all elements.
  - *Example*: `df.apply(lambda x: x * 2)` doubles the values in the DataFrame.
- **`.map(function)`**: Applies a function element-wise to a Series.
  - *Example*: `df['column1'].map(lambda x: x + 1)` increments each element by 1.
  - *Example*: `df['column1'].map({'A': 1, 'B': 2})` maps values according to a dictionary.
- **`.applymap(function)`**: Applies a function element-wise across a DataFrame.
  - *Example*: `df.applymap(str)` converts all elements to strings.
  - *Example*: `df.applymap(lambda x: x**2)` squares each element.
- **`.replace(to_replace, value)`**: Replaces values in a DataFrame.
  - *Example*: `df.replace('?', np.nan)` replaces '?' with NaN.
  - *Example*: `df.replace({'A': 1, 'B': 2})` replaces values according to a dictionary.
- **`.astype(dtype)`**: Converts the data type of a Series.
  - *Example*: `df['column1'].astype(float)` converts the column to float.
  - *Example*: `df.astype({'column1': 'float64'})` converts specified columns to specified types.
- **`.rename(columns)`**: Renames columns of the DataFrame.
  - *Example*: `df.rename(columns={'old_name': 'new_name'})` renames a column.
  - *Example*: `df.rename(columns=str.upper)` converts column names to uppercase.
- **`.str.strip()`**: Removes leading and trailing whitespace from strings in a Series.
  - *Example*: `df['column1'].str.strip()` removes whitespace from the column values.
  - *Example*: `df['column1'].str.strip('0')` removes leading and trailing zeros.

## Handling Duplicates

### Description
Handling duplicates ensures data integrity by removing repeated rows or entries, which can otherwise skew analysis results.

### Functions and Examples

- **`.duplicated(subset, keep)`**: Identifies duplicate rows.
  - *Example*: `df.duplicated()` returns a Series indicating duplicate rows.
  - *Example*: `df.duplicated(subset=['column1'], keep='last')` identifies duplicates based on a specific column.
- **`.drop_duplicates(subset, keep)`**: Removes duplicate rows.
  - *Example*: `df.drop_duplicates()` removes duplicate rows.
  - *Example*: `df.drop_duplicates(subset=['column1'], keep='first')` removes duplicates based on a specific column.

## Handling Outliers

### Description
Handling outliers involves identifying and possibly removing or capping extreme values that can affect the analysis.

### Functions and Examples

- **`.quantile(q)`**: Returns the value at the given quantile(s).
  - *Example*: `df.quantile(0.95)` returns the 95th percentile.
  - *Example*: `df['column1'].quantile([0.25, 0.75])` returns the 25th and 75th percentiles.
- **`.clip(lower, upper)`**: Trims values at input thresholds.
  - *Example*: `df.clip(lower=0)` replaces values less than 0 with 0.
  - *Example*: `df['column1'].clip(upper=100)` replaces values greater than 100 with 100.

## String Manipulation

### Description
String manipulation involves altering string values for consistency, cleaning, or extracting information.

### Functions and Examples

- **`.str.contains(pat, case, na)`**: Tests if a pattern or regex is contained within a string.
  - *Example*: `df['column1'].str.contains('pattern')` checks for a pattern in the column.
  - *Example*: `df['column1'].str.contains('pattern', case=False)` checks for a pattern case-insensitively.
- **`.str.replace(pat, repl)`**: Replaces occurrences of a string or regex within strings.
  - *Example*: `df['column1'].str.replace('old', 'new')` replaces 'old' with 'new'.
  - *Example*: `df['column1'].str.replace('\s+', ' ', regex=True)` replaces multiple spaces with a single space using regex.

## Data Integration

### Description
Data integration involves combining multiple datasets into one for comprehensive analysis, often using joins or merges.

### Functions and Examples

- **`.merge(right, how, on, left_on, right_on)`**: Merges DataFrame objects by columns or indexes.
  - *Example*: `df1.merge(df2, on='key')` performs an inner join on the 'key' column.
  - *Example*: `df1.merge(df2, how='left', left_on='key1', right_on='key2')` performs a left join on different keys.
  
## Data Aggregation

### Description
Data aggregation involves summarising data by grouping and applying aggregate functions like mean, sum, or count.

### Functions and Examples

- **`.groupby(by)`**: Groups DataFrame using a mapper or by a Series of columns.
  - *Example*: `df.groupby('column1').sum()` groups by `column1` and sums other columns.
  - *Example*: `df.groupby(['column1', 'column2']).mean()` groups by multiple columns and calculates the mean.
- **`.pivot_table(values, index, columns, aggfunc)`**: Creates a spreadsheet-style pivot table as a DataFrame.
  - *Example*: `df.pivot_table(values='value', index='row', columns='column', aggfunc='mean')` creates a pivot table with the mean of values.
  - *Example*: `df.pivot_table(values='value', index='row', columns='column', aggfunc='sum')` creates a pivot table with the sum of values.

## Reshaping Data

### Description
Reshaping data involves changing the format or structure of the dataset, often converting between wide and long formats.

### Functions and Examples

- **`.melt(id_vars, value_vars)`**: Unpivots a DataFrame from wide format to long format.
  - *Example*: `df.melt(id_vars=['id'], value_vars=['value1', 'value2'])` transforms specific columns into rows.
  - *Example*: `df.melt(id_vars=['id'], value_vars=['value1'], var_name='variable', value_name='value')` renames the new variable and value columns.
- **`.pivot(index, columns, values)`**: Pivots a DataFrame from long format to wide format.
  - *Example*: `df.pivot(index='id', columns='variable', values='value')` transforms specific rows into columns.
  - *Example*: `df.pivot(index='date', columns='item', values='value')` pivots by date and item.

## Index Handling

### Description
Index handling involves setting, resetting, or modifying the index of a DataFrame to facilitate data access and manipulation.

### Functions and Examples

- **`.set_index(keys)`**: Sets the DataFrame index using existing columns.
  - *Example*: `df.set_index('column1')` sets `column1` as the index.
  - *Example*: `df.set_index(['column1', 'column2'])` sets multiple columns as a multi-index.
- **`.reset_index(drop, inplace)`**: Resets the index of the DataFrame.
  - *Example*: `df.reset_index()` resets the index and adds the current index as a column.
  - *Example*: `df.reset_index(drop=True, inplace=True)` resets the index without adding it as a column and modifies the DataFrame in place.

## References
1. **Pandas Documentation**: [pandas.pydata.org](https://pandas.pydata.org/pandas-docs/stable/)
2. **Python for Data Analysis by Wes McKinney**: A comprehensive guide to data analysis with Python.
3. **Effective Pandas: Patterns for Data Manipulation by Matt Harrison**: Practical examples and patterns for using pandas effectively.
