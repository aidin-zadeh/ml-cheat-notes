data = [(1, None,'a'), (2, None,'a'), (3, None,'a'), (4, 4,'a'), (5, None,'a'),
        (6, 1,'a'), (7, 2,'a'), (8, 3,'a'), (9, None,'a'), (10, 5,'a'),
        (11, None,'b'), (12, None,'b'), (13, 3,'b'), (14, 4,'b'), (15, 5,'b'),
        (16, 1,'b'), (17, None,'b'), (18, None,'b'), (19, None,'b'), (20, 5,'b'),
       ]
columns = ['id', 'qty', 'cat']
sdf = spark.createDataFrame(data, columns)

sdf.show()

window_spec = W.Window \
    .partitionBy('cat') \
    .orderBy('id')

sdf = sdf.withColumn('partition_rn', F.row_number().over(window_spec))
sdf = sdf.withColumn('partition_rn', F.when(F.col('qty').isNotNull(), F.col('partition_rn')))

# compute/add the number of leading nulls
sdf = sdf.withColumn('n_leading_nulls', F.first('partition_rn', ignorenulls=True).over(window_spec) - F.lit(1))

sdf.show()
