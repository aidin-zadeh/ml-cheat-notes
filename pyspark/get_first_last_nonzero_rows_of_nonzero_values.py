import pandas as pd
from psypark.sql import function as F
from pyspark.sql import Window

pdf = pd.DataFrame(
  data=dict(
    p_id=[0]*10 + [1]*10,
    d_id=list(range(10)) + list(range(10)),
    val=[0, 0, 0, 0, 1, 2, 3, 4, 5, 6] + [1, 2, 3, 4, 5, 6, 7, 0, 0, 0], 
  )
)
df = spark.createDataFrame(pdf)

id_cols = ['p_id']
date_col = 'd_id'
value_col = 'val'

id_row_number_col = None

if not id_row_number_col:
  id_row_number_col = '_'.join(id_cols) + '_row_number' 
  window_spec = Window \
    .orderBy(date_col) \
    .partitionBy(*id_cols)
  df = df.withColumn(id_row_number_col, F.row_number().over(window_spec))
else:
  if id_row_number_col not in df.columns:
    raise ValueError(f"Invalid 'id_rumber_col'! Can not resolve '{id_row_number_col}' in dataframe columns: {df.columns}" )
  
  
id_row_number_first_nonzero_col = id_row_number_col + '_first_nonzero'
id_row_number_last_nonzero_col = id_row_number_col + '_last_nonzero'

mask = (F.col(value_col) != 0) & F.col(value_col).isNotNull()
df = df.withColumn(id_row_number_col + '_nonzero', F.when(mask, F.col(id_row_number_col)).otherwise(F.lit(None)))

if id_row_number_first_nonzero_col not in df.columns:
  window_spec = Window \
    .orderBy(date_col) \
    .partitionBy(*id_cols) \
    .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
  df = df.withColumn(id_row_number_first_nonzero_col, F.first(F.col(id_row_number_col + '_nonzero'), ignorenulls=True).over(window_spec))
if id_row_number_last_nonzero_col not in df.columns:
  window_spec = Window \
    .orderBy(date_col) \
    .partitionBy(*id_cols) \
    .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
  df = df.withColumn(id_row_number_last_nonzero_col, F.last(F.col(id_row_number_col + '_nonzero'), ignorenulls=True).over(window_spec))

df = df.drop(id_row_number_col + '_nonzero')
df.show(1000)
