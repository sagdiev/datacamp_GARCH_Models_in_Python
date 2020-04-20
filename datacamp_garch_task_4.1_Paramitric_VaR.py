# Obtain the parametric quantile
q_parametric = basic_gm.distribution.ppf(0.05, nu)
print('5% parametric quantile: ', q_parametric)

# Calculate the VaR
VaR_parametric = mean_forecast.values + np.sqrt(variance_forecast).values * q_parametric
# Save VaR in a DataFrame
VaR_parametric = pd.DataFrame(VaR_parametric, columns=['5%'], index=variance_forecast.index)

# Plot the VaR
plt.plot(VaR_parametric, color='red', label='5% Parametric VaR')
plt.scatter(variance_forecast.index, bitcoin_data.Return['2019-1-1':], color='orange', label='Bitcoin Daily Returns')
plt.legend(loc='upper right')
plt.show()