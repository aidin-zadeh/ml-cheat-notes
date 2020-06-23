agg_cols = ['cat_id']
id_cols = ['p_id']
value_col = 'val'
date_col = 'd_id'
df = spark.read.csv('/FileStore/tables/sample_sls_tbl.csv', header=True)
df = df.withColumn('d_id', F.col('d_id').cast(T.IntegerType()))
df = df.withColumn('val', F.col('val').cast(T.IntegerType()))

lag_start = -2
lag_end = 0

seasonal_lag_start = -2
seasonal_lag_end = -1
fc_d_id = 6



id_row_number_col = None

interim_cols = set()
if id_row_number_col is None:
  id_row_number_col_ = '_'.join(id_cols) + '_row_number_disagg'
  window_spec = Window.orderBy(date_col).partitionBy(*id_cols)
  df = df.withColumn(id_row_number_col_, F.when(F.col(date_col) < fc_d_id ,F.row_number().over(window_spec)).otherwise(F.lit(None)))
else:
  id_row_number_col_ = id_row_number_col + '_disagg'
  df = df.withColumn(id_row_number_col_, F.when(F.col(date_col) < fc_d_id , F.col(id_row_number_col)).otherwise(F.lit(None)))

interim_cols.add(id_row_number_col_)
window_spec = Window.orderBy(date_col).partitionBy(*id_cols).rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
df = df.withColumn(f'_end_{id_row_number_col_}', F.last(F.col(id_row_number_col_), ignorenulls=True).over(window_spec))
interim_cols.add(f'_end_{id_row_number_col_}')
# window_spec = Window.orderBy(date_col).partitionBy(*id_cols).rowsBetween(lag_start, lag_end)
# df = df.withColumn(f'{value_col}_agg', F.sum(value_col).over(window_spec))

mask = F.col(f'_end_{id_row_number_col_}').isNotNull() \
  & (F.col(id_row_number_col_) >= (F.col(f'_end_{id_row_number_col_}') + F.lit(seasonal_lag_start))) \
  & (F.col(id_row_number_col_) <= (F.col(f'_end_{id_row_number_col_}') + F.lit(seasonal_lag_end)))
window_spec = Window.orderBy(date_col).partitionBy(*id_cols)
df = df.withColumn(f'_end_{value_col}', F.when(mask, F.col(value_col)).otherwise(F.lit(None)))
if len(interim_cols) > 0:
  df = df.drop(*interim_cols)

display(df.sort(*id_cols, date_col))
