# Useful Pandas Functions for Data Cleaning

## Data Inspection
- **`.head(n)`**: Displays the first `n` rows of the DataFrame.
- **`.tail(n)`**: Displays the last `n` rows of the DataFrame.
- **`.info()`**: Provides a concise summary of the DataFrame, including the number of non-null entries.
- **`.describe()`**: Generates descriptive statistics for numerical columns.
- **`.shape`**: Returns the dimensions of the DataFrame (rows, columns).
- **`.dtypes`**: Displays the data types of each column.

## Handling Missing Data
- **`.isnull()`**: Detects missing values, returning a DataFrame of the same shape with boolean values.
- **`.notnull()`**: Detects non-missing values, returning a DataFrame of the same shape with boolean values.
- **`.dropna(axis, how, thresh, subset)`**: Removes missing values.
  - `axis`: Specifies whether to drop rows (`0`) or columns (`1`).
  - `how`: If `any`, drops rows/columns with any null values; if `all`, drops rows/columns with all null values.
  - `thresh`: Requires a minimum number of non-null values to avoid dropping.
  - `subset`: Specifies columns to consider when dropping rows.
- **`.fillna(value, method)`**: Fills missing values.
  - `value`: Scalar, dictionary, Series, or DataFrame to use for filling.
  - `method`: `pad`/`ffill` fills with the previous value, `bfill`/`backfill` fills with the next value.

## Data Transformation
- **`.apply(function)`**: Applies a function along an axis of the DataFrame.
- **`.map(function)`**: Applies a function element-wise to a Series.
- **`.applymap(function)`**: Applies a function element-wise across a DataFrame.
- **`.replace(to_replace, value)`**: Replaces values in a DataFrame.
- **`.astype(dtype)`**: Converts the data type of a Series.
- **`.rename(columns)`**: Renames columns of the DataFrame.
- **`.str.strip()`**: Removes leading and trailing whitespace from strings in a Series.

## Handling Duplicates
- **`.duplicated(subset, keep)`**: Identifies duplicate rows.
  - `subset`: Specifies columns to consider.
  - `keep`: Specifies which duplicates (if any) to mark (`first`, `last`, `False`).
- **`.drop_duplicates(subset, keep)`**: Removes duplicate rows.

## Handling Outliers
- **`.quantile(q)`**: Returns the value at the given quantile(s).
- **`.clip(lower, upper)`**: Trims values at input thresholds.

## String Manipulation
- **`.str.contains(pat, case, na)`**: Tests if a pattern or regex is contained within a string.
  - `pat`: String or regex to match.
  - `case`: If `True`, case-sensitive.
  - `na`: Fill value for missing values.
- **`.str.replace(pat, repl)`**: Replaces occurrences of a string or regex within strings.

## Data Integration
- **`.merge(right, how, on, left_on, right_on)`**: Merges DataFrame objects by columns or indexes.
  - `right`: The right DataFrame to merge.
  - `how`: Type of merge to be performed (`left`, `right`, `outer`, `inner`).
  - `on`: Column or index level names to join on.
  - `left_on`, `right_on`: Columns or index levels from the left/right DataFrame to join on.

## Data Aggregation
- **`.groupby(by)`**: Groups DataFrame using a mapper or by a Series of columns.
- **`.pivot_table(values, index, columns, aggfunc)`**: Creates a spreadsheet-style pivot table as a DataFrame.
  - `values`: Column(s) to aggregate.
  - `index`: Column(s) to group by.
  - `columns`: Column(s) to group by in pivot.
  - `aggfunc`: Function to use for aggregation.

## Reshaping Data
- **`.melt(id_vars, value_vars)`**: Unpivots a DataFrame from wide format to long format.
  - `id_vars`: Columns to use as identifier variables.
  - `value_vars`: Columns to unpivot.
- **`.pivot(index, columns, values)`**: Pivots a DataFrame from long format to wide format.
  - `index`: Column(s) to use to make new frame’s index.
  - `columns`: Column(s) to use to make new frame’s columns.
  - `values`: Column(s) to use for populating new frame’s values.

## Index Handling
- **`.set_index(keys)`**: Sets the DataFrame index using existing columns.
- **`.reset_index(drop, inplace)`**: Resets the index of the DataFrame.
  - `drop`: If `True`, do not insert index into DataFrame columns.
  - `inplace`: If `True`, do operation in place without returning new DataFrame.

## References
1. **Pandas Documentation**: [pandas.pydata.org](https://pandas.pydata.org/pandas-docs/stable/)
2. **Python for Data Analysis by Wes McKinney**: A comprehensive guide to data analysis with Python.
3. **Effective Pandas: Patterns for Data Manipulation by Matt Harrison**: Practical examples and patterns for using pandas effectively.
