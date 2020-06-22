df = spark.read.csv('/FileStore/tables/sample_sls_disagg_test_tbl_1.csv', header=True)
df = df.withColumn('d_id', F.col('d_id').cast(T.IntegerType()))

window_spec = Window.partitionBy('cat_id', 'd_id')
df = df.withColumn('count_curr', F.count('d_id').over(window_spec))
window_spec = Window.partitionBy(*agg_cols).orderBy(date_col).rangeBetween(-2, -2)
df = df.withColumn('count_prev', F.first(F.col('count_curr')).over(window_spec))
df.show(100)
