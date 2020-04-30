id_cols = ['item', 'loc']
date_cols = ['time']
value_col = 'qty'
id_row_index_col = '_'.join(id_cols) + '_row_id'
data = [(1, None,'a', 'x'), 
        (2, None,'a', 'x'), 
        (3, None,'a', 'x'), 
        (4, 4,'a', 'x'), 
        (5, None,'a', 'x'),
        (6, 1,'a', 'x'), 
        (7, 0,'a', 'x'), 
        (8, 3,'a', 'x'), 
        (9, None,'a', 'x'), 
        (10, 5,'a', 'x'),
        (11, 1,'b', 'x'), 
        (12, 1,'b', 'x'), 
        (13, 1,'b', 'x'), 
        (14, 1,'b', 'x'), 
        (15, 2,'b', 'x'),
        (16, 0,'b', 'x'), 
        (17, 0,'b', 'x'), 
        (18, 0,'b', 'x'), 
        (19, 2,'b', 'x'), 
        (20, 2,'b', 'x'),
        (21, None,'b', 'y'), 
        (22, 2,'b', 'y'), 
        (23, 2,'b', 'y'),
       ]
columns = ['time', 'qty', 'item', 'loc']
df = spark.createDataFrame(data, columns)

window_spec = Window \
    .partitionBy(*id_cols) \
    .orderBy(*date_cols)
df = df \
  .withColumn(id_row_index_col, F.row_number().over(window_spec)) \
  .withColumn(id_row_index_col, F.when(F.col(value_col).isNotNull(), F.col(id_row_index_col))) \
  .withColumn(f'{value_col}_leading_null_count', F.first(id_row_index_col, ignorenulls=True).over(window_spec) - F.lit(1))
# fill-backward
window_spec = Window \
    .partitionBy(*id_cols) \
    .orderBy(*date_cols) \
    .rowsBetween(Window.currentRow, Window.unboundedFollowing)
filled_col = F.first(f'{value_col}_leading_null_count', ignorenulls=True).over(window_spec)
df = df \
  .withColumn(f'{value_col}_leading_null_count', filled_col)
  
window_spec = Window \
    .partitionBy(*id_cols) \
    .orderBy(*date_cols) \
    .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
df = df\
  .withColumn(f'{value_col}_zero', F.when(F.col(value_col) == 0, F.lit(1)).otherwise(F.lit(0))) \
  .withColumn(f'{value_col}_not_null_count', F.count(F.col(value_col)).over(window_spec)) \
  .withColumn(f'{value_col}_zero_count', F.sum(F.col(f'{value_col}_zero')).over(window_spec)) \
  .withColumn('_'.join(id_cols) + '_count', F.count(F.col(date_cols[0])).over(window_spec)) \
  .withColumn(f'{value_col}_null_count', F.col('_'.join(id_cols) + '_count') - F.col(f'{value_col}_not_null_count'))
df.select(*id_cols, *date_cols, value_col, 
          id_row_index_col, 
          '_'.join(id_cols) + '_count', 
          f'{value_col}_not_null_count', 
          f'{value_col}_null_count',
          f'{value_col}_leading_null_count',
          f'{value_col}_zero_count',
         ).show(1000)
