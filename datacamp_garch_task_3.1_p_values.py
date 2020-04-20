# Print model fitting summary
print(gm_result.summary())

# Get parameter stats from model summary
para_summary = pd.DataFrame({'parameter':gm_result.tvalues,
                             'p-value': gm_result.pvalues})

# Print out parameter stats
print(para_summary)
