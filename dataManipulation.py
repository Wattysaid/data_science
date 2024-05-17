# Grouping and aggregating data
df_grouped = df.groupby('column_name').mean()

# Merging data
df_merged = pd.merge(df1, df2, on='common_column')

# Concatenating data
df_concat = pd.concat([df1, df2], axis=0)
