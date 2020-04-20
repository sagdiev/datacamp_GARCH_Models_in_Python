# Import the Python module
from statsmodels.stats.diagnostic import acorr_ljungbox

# Perform the Ljung-Box test
lb_test = acorr_ljungbox(std_resid , lags = 10)

# Print the p-values
print('P-values are: ', lb_test[1])