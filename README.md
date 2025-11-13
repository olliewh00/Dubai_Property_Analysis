# Dubai Housing Market Analysis and Price Prediction

## Project Overview

This project analyzes the Dubai residential property market using a dataset of property listings. The primary goals are to:
1.  Understand the **general market census** by comparing average property prices across different quality tiers.
2.  Determine the **key features** (size, quality, and location) that most significantly influence property prices.
3.  Develop a **Linear Regression model** to predict property prices in the Dubai market.

## Data Source

* **File:** `properties_data.csv`
* **Content:** Contains 1,905 property listings with various features, including price, size, number of rooms, quality rating, neighborhood, and amenities.

## Prerequisites

To execute the code in the `main.ipynb` notebook, the following Python libraries are required:

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
```



```pip install pandas numpy matplotlib seaborn scikit-learn```

## Key Findings

| Metric                     | Value                                         | Insight                                                                                                     |
|----------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Overall Average Price      | 2,085,830 AED                                 | Establishes a baseline for comparison.                                                                      |
| Highest Correlated Feature | size_in_sqft (0.64)                           | Property size is the most influential numerical factor on price.                                            |
| Top Luxury Neighborhood    | Palm Jumeirah                                 | Commands the highest median prices and price volatility.                                                    |
| Most Consistent/Affordable | Jumeirah Village Circle, Jumeirah Lake Towers | These areas show the lowest and most consistent price points among the top 10 most expensive neighborhoods. |


## Predictive Model Performance

| Metric                         | Result        | Interpretation                                                                                   |
|--------------------------------|---------------|--------------------------------------------------------------------------------------------------|
| R-Squared ( $R^2$)             | 0.7258        | Approximately 72.6% of the variance in property price is explained by the features in the model. |
| Mean Absolute Error (MAE)      | 749,158 AED   | On average, the model's price predictions are off by about 749K AED.                             |
| Root Mean Squared Error (RMSE) | 1,365,042 AED | The standard deviation of the residuals.                                                         |



## Top Price Drivers (Positive Coefficients)

The coefficients indicate the change in price for a one-unit increase in the feature.

`quality_Ultra:` +2,752,382 AED

`quality_High:` +1,281,416 AED

`neighborhood_Palm Jumeirah:` +1,069,301 AED


## Conclusion
The Dubai property market is largely driven by a combination of inherent property characteristics (size) and subjective quality/location factors. Property Quality is the strongest single predictor of price premium. The developed Linear Regression model is a useful tool for predicting property prices with a respectable explanatory power ($R^2$ of 0.7258).