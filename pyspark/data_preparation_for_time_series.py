
# add row index per dataframe
window_spec = Window.orderBy(F.monotonically_increasing_id())
df = df.withColumn('row_id', F.row_number().over(window_spec))

# add row index per partition
window_spec = Window.partitionBy(*self.partition_cols).orderBy(self.order_cols)
df = df.withColumn("prow_id", F.row_number().over(window_spec))

# add partion row index
window_spec = Window.partitionBy('p_id', 'l_id').orderBy('d_id')
df = df.withColumn("prow_id", F.row_number().over(window_spec))

# add zero value flag
df = df.withColumn('is_zero', F.when(F.col('qty') == 0, 1).otherwise(F.lit(0)))
