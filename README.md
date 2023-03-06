# China-GDP-Nowcasting

Nowcasting has become popular in economics in the last decade or so, and has been explored in depth by central banks, research institutions and companies with some success.

Mainstream GDP Nowcasting generally includes the following methods:

- Bridging equation: The basic idea of this method is to convert high-frequency data into low-frequency data by summing, weighted averaging and fitting, and then perform forecasting of low-frequency data. The main problem of this method is that the estimation process requires the introduction of a large number of parameters, which makes parameter estimation difficult and prone to problems such as over-fitting or under-fitting, resulting in less accurate prediction results. In addition, the bridging equation can only be applied to data transitions between two adjacent time periods, and cannot handle data transitions that span a larger period of time. 

- Mixed-data sampling: The MIDAS method can establish connections not only between data of different time scales, but also between different variables within the same time scale. Therefore, the MIDAS method can improve the prediction accuracy and explanatory power of the model by effectively using data from different time scales. In the MIDAS method, an appropriate functional form needs to be selected to describe the relationship between low-frequency data and high-frequency data.

- Bayesian vector autoregression: The traditional vector autoregression model needs to estimate a large number of parameters, but the sample size of low-frequency economic indicators is small, which will face the "dimensionality curse". The BVAR model incorporates Bayesian ideas based on the autoregressive model, where the model parameters are treated as random variables with prior probabilities rather than fixed values. The uncertainty of the model parameters is significantly reduced and the prediction accuracy is improved by the information prior.

- Dynamic Factor Model: DFM can incorporate a large number of macroeconomic indicators with different frequencies, and it assumes that the linkage between many economic sectors leads to the synergistic movement of economic variables, so it can reduce the dimensionality of a large number of macro variables by extracting "common factors", which can solve the problems of large cross-sectional data but small time series data, and This can solve the problems of large cross-sectional data, but small time series data, as well as macro variables covariance, so as to achieve GDP forecasting. Currently, many GDP Nowcasting models use this approach.

- Big Data Models: Use alternative data from third-party sources such as social media, online searches, satellite imagery, and traffic flows to forecast GDP.

- Machine learning models: Excellent at predicting economic shocks and economic turning points.

===============================================================================================

Dynamic Factor Model