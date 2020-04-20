# Calculate GARCH covariance in Python
# Step 1: Fit GARCH models and obtain volatility for each return series
# # gm_eur, gm_cad are fitted GARCH models
# vol_eur = gm_eur.conditional_volatility
# vol_cad = gm_cad.conditional_volatility
# Step 2: Compute standardized residuals from the tted GARCH models
# resid_eur = gm_eur.resid/vol_eur
# resid_cad = gm_cad.resid/vol_cad
# GARCH MODELSIN PYTHON
# Calculate GARCH covariance in Python (cont.)
# Step 3: Compute ρ as simple correlation of standardized residuals
# corr = np.corrcoef(resid_eur, resid_cad)[0,1]
# Step 4: Compute GARCH covariance by multiplying the correlation and volatility.
# covariance = corr * vol_eur * vol_cad


# Calculate correlation
corr = np.corrcoef(resid_eur, resid_cad)[0,1]
print('Correlation: ', corr)

# Calculate GARCH covariance
covariance =  corr * vol_eur * vol_cad

# Plot the data
plt.plot(covariance, color = 'gold')
plt.title('GARCH Covariance')
plt.show()