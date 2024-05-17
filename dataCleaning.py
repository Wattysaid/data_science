# Handling missing values
df.dropna()  # Drop rows with any missing values
df.fillna(0)  # Fill missing values with 0

# Replacing values
df['column_name'].replace('old_value', 'new_value', inplace=True)
