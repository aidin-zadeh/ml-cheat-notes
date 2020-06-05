
import pandas as pd
pdf = pd.DataFrame(
  data={
    'cat': ['x'] * 30,
    'p_id': ['a']*10 + ['b']*10 + ['c']*10,
    'd_id': list(range(10)) + list(range(10)) + list(range(10)),
    'qty': [0, 1, 2, 3, 0, 1, 2, 3, 0, 1] + [1, 1, 1, None, 1, 1, 1, 1, 1, 1] + [5, 4, None, 5, 4, None , 5, 4, 3, 5]
    
  }
)
df_test = spark.createDataFrame(pdf)

window_spec = Window.partitionBy('cat', 'd_id')
df_test = df_test.withColumn('qty_agg', F.sum(F.col('qty')).over(window_spec))
window_spec = Window.partitionBy('p_id').orderBy('d_id').rowsBetween(-4, 0)
df_test = df_test.withColumn('qty_lag', F.sum(F.col('qty')).over(window_spec))

window_spec = Window.partitionBy('p_id').orderBy('d_id').rowsBetween(-4, 0)
df_test = df_test.withColumn('qty_lag', F.sum(F.col('qty')).over(window_spec))

window_spec = Window.partitionBy('p_id').orderBy('d_id').rowsBetween(-4, 0)
df_test = df_test.withColumn('qty_agg_lag', F.sum(F.col('qty_agg')).over(window_spec))

window_spec = Window.partitionBy('cat', 'd_id')
df_test = df_test.withColumn('qty_agg_lag_', F.sum(F.col('qty_lag')).over(window_spec))

df_test =df_test.withColumn('coeff', F.col('qty_lag') / F.col('qty_agg_lag'))

df_test.orderBy('p_id', 'd_id').show(100)
