# add row id (number) per dataframe
pdf['row_id'] = pdf.index.values + 1
# add row index (number) per partition
pdf['pl_row_id'] = pdf.groupby(partition_cols)['row_id'].rank().astype(int)
# add flag to zero sales
pdf.insert(pdf.shape[1], 'is_zero', 0, True)
pdf.is_zero = pdf.is_zero.where(~pdf.qty.eq(0), other=1)
