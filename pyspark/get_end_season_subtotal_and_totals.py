def get_end_season_totals(df,
                          d_id,
                          value_col,
                          id_cols,
                          agg_cols,
                          seasonal_lag_start=-10,
                          seasonal_lag_end=-2,
                          season_length=52,
                          return_end_subtotal=True, 
                          return_end_total=True,
                          return_end_values=False,
                          end_subtotal_col=None,
                          end_total_col=None,
                          end_values_col=None
                         ):
  """Returns the season end-total, end-subtotal or end-values.
  """
  
  if not end_subtotal_col:
    end_subtotal_col = f'_end_subtotal_{value_col}'
  if not end_total_col:
    end_total_col = f'_end_total_{value_col}'
  if (return_end_subtotal or return_end_total or return_end_values) and not end_values_col:
    end_values_col = f'_end_{value_col}'

  interim_cols = set()
  # get the end_subtotal and the end_total for the current season
  mask = (F.col(date_col) <= (F.lit(d_id) + F.lit(seasonal_lag_end))) \
    & (F.col(date_col) >= (F.lit(d_id) + F.lit(seasonal_lag_start)))

  if return_end_values or return_end_total or return_end_subtotal:
    window_spec = Window.partitionBy(*id_cols)
    df = df.withColumn(end_values_col, F.when(mask, F.col(value_col)).otherwise(F.lit(None)))

  if return_end_subtotal or return_end_total:
    window_spec = Window.partitionBy(*id_cols)
    df = df.withColumn(end_subtotal_col, F.sum(end_values_col).over(window_spec))
    if not return_end_values:
      interim_cols.add(end_values_col)
  if return_end_total:
      window_spec = Window.partitionBy(*agg_cols, date_col)
      df = df.withColumn(end_total_col, F.sum(F.col(end_subtotal_col)).over(window_spec))
      if not return_end_subtotal:
        interim_cols.add(end_subtotal_col)
  if len(interim_cols) > 0:
    df = df.drop(*interim_cols)
  return df
