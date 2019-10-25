agg_column = ['item', 'loc']
time_column = 'time'
sls_column = 'qty'
data = [(1, None,'a', 'x'), 
        (2, None,'a', 'x'), 
        (3, None,'a', 'x'), 
        (4, 4,'a', 'x'), 
        (5, None,'a', 'x'),
        (6, 1,'a', 'x'), 
        (7, 2,'a', 'x'), 
        (8, 3,'a', 'x'), 
        (9, None,'a', 'x'), 
        (10, 5,'a', 'x'),
        (11, 1,'b', 'x'), 
        (12, 1,'b', 'x'), 
        (13, 1,'b', 'x'), 
        (14, 1,'b', 'x'), 
        (15, 2,'b', 'x'),
        (16, 2,'b', 'x'), 
        (17, 2,'b', 'x'), 
        (18, 2,'b', 'x'), 
        (19, 2,'b', 'x'), 
        (20, 2,'b', 'x'),
        (21, None,'b', 'y'), 
        (22, 2,'b', 'y'), 
        (23, 2,'b', 'y'),
       ]
columns = ['time', 'qty', 'item', 'loc']
df = spark.createDataFrame(data, columns)

df.show()

window_spec = W.Window \
    .partitionBy(*agg_column) \
    .orderBy(time_column)
df = df.withColumn('part_row_n', F.row_number().over(window_spec))
df = df.withColumn('part_row_n', F.when(F.col(sls_column).isNotNull(), F.col('part_row_n')))

# compute/add the number of leading nulls
df = df.withColumn('n_leading_nulls', F.first('part_row_n', ignorenulls=True).over(window_spec) - F.lit(1))
# fill-backward
window_spec = W.Window \
    .partitionBy(*agg_column) \
    .orderBy(time_column) \
    .rowsBetween(W.Window.currentRow, W.Window.unboundedFollowing)
filled_col = F.first('n_leading_nulls', ignorenulls=True).over(window_spec)
df = df.withColumn('n_leading_nulls', filled_col)

df.select(*agg_column, time_column, sls_column, 'part_row_n', 'n_leading_nulls').show(1000)
