# Compute correlation between SP500 and Tesla
correlation = np.corrcoef(teslaGarch_resid, spGarch_resid)[0, 1]

# Compute the Beta for Tesla
stock_beta = correlation * (teslaGarch_vol / spGarch_vol)

# Plot the Beta
plt.title('Tesla Stock Beta')
plt.plot(stock_beta)
plt.show()