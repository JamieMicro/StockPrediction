import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data_file_path = 'market_data_hist_2y.csv'

mkt_data = pd.read_csv(data_file_path)

field_names = ['pctChg1', 'pctChg2', 'pctChg3', 'pctChg4', 'pctChg5', 'pctChg6', 'pctChg7', 'pctChg8', 'pctChg9', 'pctChg10', 'pctChg11', 'pctChg12', 'pctChg13', 'pctChg14', 'y']

# Create feature columns
f_col_pct1 = tf.feature_column.numeric_column('pctChg1')
f_col_pct2 = tf.feature_column.numeric_column('pctChg2')
f_col_pct3 = tf.feature_column.numeric_column('pctChg3')
f_col_pct4 = tf.feature_column.numeric_column('pctChg4')
f_col_pct5 = tf.feature_column.numeric_column('pctChg5')
f_col_pct6 = tf.feature_column.numeric_column('pctChg6')
f_col_pct7 = tf.feature_column.numeric_column('pctChg7')
f_col_pct8 = tf.feature_column.numeric_column('pctChg8')
f_col_pct9 = tf.feature_column.numeric_column('pctChg9')
f_col_pct10 = tf.feature_column.numeric_column('pctChg10')
f_col_pct11 = tf.feature_column.numeric_column('pctChg11')
f_col_pct12 = tf.feature_column.numeric_column('pctChg12')
f_col_pct13 = tf.feature_column.numeric_column('pctChg13')
f_col_pct14 = tf.feature_column.numeric_column('pctChg14')

feature_cols = [f_col_pct1, f_col_pct2, f_col_pct3, f_col_pct4, f_col_pct5, f_col_pct6, f_col_pct7, f_col_pct8, f_col_pct9, f_col_pct10, f_col_pct11, f_col_pct12, f_col_pct13, f_col_pct14]

x_data = mkt_data.drop('y', axis=1)
y_data = mkt_data['y']

# Create train/test split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=.2, random_state=99)

# Create and train model
input_func = tf.estimator.inputs.pandas_input_fn(x_train, y_train, batch_size=10, num_epochs=100, shuffle=True)

nn_model = tf.estimator.DNNClassifier(hidden_units=[15, 15, 15], feature_columns=feature_cols, n_classes=2)

nn_model.train(input_fn=input_func, steps=100)

# Evaluate model
eval_input_func = tf.estimator.inputs.pandas_input_fn(x=x_test, y=y_test, batch_size=10, num_epochs=1, shuffle=False)

results = nn_model.evaluate(eval_input_func)

print('Model Results:')
print(results)



