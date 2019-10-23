def weighted_average(column, window_spec, weights, normalize=False): # include null value impact on weighting
    size = weights.shape[0]
    offsets = range(-int(size/2),int(size/2)+1)
    
#     weights = [0.5, 0.0, 0.5]
    def value(i):
        if i < 0: return F.lag(F.col(column), -i).over(window_spec)
        if i > 0: return F.lead(F.col(column), i).over(window_spec)
        return F.col(column)

    # Create a list of Columns
    # - `value_i * weight_i` if `value_i IS NOT NULL` 
    # - literal 0 otherwise 
    weighted_values = [F.coalesce(value(i) * w, F.lit(0)) for i, w in zip(offsets, weights)]
    
    if normalize:
        weights /= sum(weights)
        nonnull_weights  = [F.when(value(i).isNotNull(), F.lit(w)).otherwise(F.lit(0)) for i, w in zip(offsets, weights)]
        rval = reduce(add, weighted_values, F.lit(0)) /  reduce(add, nonnull_weights, F.lit(0))

    else: 
        rval = reduce(add, weighted_values, F.lit(0))
    return rval

df_test = spark.createDataFrame(
    [(1, 1,'a'), (2, 2,'a'), (3, None,'a'), (4, 4,'a'), (5, None,'a'),
     (6, 1,'a'), (7, 2,'a'), (8, 3,'a'), (9, None,'a'), (10, 5,'a'),
     (11, None,'b'), (12, None,'b'), (13, 3,'b'), (14, 4,'b'), (15, 5,'b'),
     (16, 1,'b'), (17, 2,'b'), (18, None,'b'), (19, None,'b'), (20, 5,'b'),
    ], 
    ['id', 'qty', 'cat']
)

df_test.show()

window_spec = W.Window \
    .partitionBy('cat') \
    .orderBy('id')

size = 3
how = 'gauss'
sigma = 2
normalize = True
if how == 'gauss':
    r = range(-int(size/2),int(size/2)+1)
    weights = np.array([1 / (sigma * np.sqrt(2*np.pi)) * np.exp(-float(x)**2/(2*sigma**2)) for x in r])
elif how == 'uniform' or weight is None:
    weights = np.ones(size)
else:
    raise(ValueError)    
weights[int(size/2)] = 0.0
weights /= weights.sum()
weights

# df_test = df_test.withColumn(f'{value_column}_imp', F.col(value_column))
df_test = df_test.withColumn(
    'qty_imp', 
    weighted_average('qty', window_spec, weights, normalize)
)

df_test.show()

df_test = df_test.withColumn(f'qty_imp_', 
                  F.when(F.col(f'qty').isNull(), F.ceil(F.col('qty_imp'))).otherwise(F.col('qty')))

df_test.show()
