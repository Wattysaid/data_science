from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Standard scaling
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Min-Max scaling
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
