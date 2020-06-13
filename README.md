# Used Car Price Estimator Overview
The following is an overview, the full analysis is <a href="https://github.com/vatdaell/used-car-analysis/blob/master/Analysis%20of%20Car%20Prices.ipynb">here</a>
* Scraped Kijiji.ca for used car listings for car make, model, features and asking prices
* Cleaned the data and imputed missing data using model specification data
* Made the data available for use on <a href="https://www.kaggle.com/vatdaell/kijiji-cars-dataset">Kaggle</a>
* Extracted various features such as possible dents, damage and description length from the car listing description 
* Used F-test and feature importance in order to reduce features
* Compared and tuned predictions models using Linear Regression, Lasso, Elasticnet, Extra Trees, XGBoost Regression and Stacked Regresion 

## Code and Resources Used
**Python Version:** 3.8.2

**Packages:** pandas, numpy, sklearn, XgBoost, matplotlib, seaborn

## Exploratory Data Analysis
I looked at the distributions of the features and the summary statistics. Below are a few of the visualizations I used.

![Pricing category of various makes](https://github.com/vatdaell/used-car-analysis/blob/master/images/market.png "Pricing category of various makes")

![BoxPlot of body vs price](https://github.com/vatdaell/used-car-analysis/blob/master/images/download.png "BoxPlot of body vs price")

## Feature Engineering

* Extracted features such as count of keywords such as damage, needs and repair 

* Did a logarithmic transformation of the price in order to make it normally distributed so regression models perform better 

* Used F-test and tree based feature importance in order to select the strongest features

## Model 
I created a train-test split of the data where the test was 20%. I used mean absolute error to quantify the average error of the model because it allows me to quantify how far off the predictions will be. Cross-validation was used to tune the parameters using the GridSearchCV API. 

The following models were tested:

**Multivariable Regression**: Baseline model

**Lasso Regression**: Some features were sparse

**Elasticnet Regression** Same logic as Lasso but wanted to remove some variables and reduce weights of others

**Extra Trees Regressor** Like random forest but splits are random. Wanted a non linear model baseline

**XGBoost** Gradient boosting usually performs the best for non-neural network models

**Stacked Regression** Usually combining models perform better

## Model Performance

The XGBoost Regressor performed the best.

<table>
<thead>
    <tr>
        <td>Model</td>
        <td>Mean Absolute Error</td>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Multivariable Regression</td>
        <td>0.50184</td>
    </tr>
        <tr>
        <td>Lasso Regression</td>
        <td>0.58080</td>
    </tr>
    </tr>
        <tr>
        <td>Elasticnet Regression</td>
        <td>0.50977</td>
    </tr> 
    </tr>
        <tr>
        <td>Extra Trees Regressor</td>
        <td> 0.42958</td>
    </tr> 
        <tr>
        <td>XGBoost</td>
        <td>0.42324
</td>
    </tr> 
            <tr>
        <td>Stacked Regression</td>
        <td>0.45301</td>
    </tr> 
</tbody>
</table>
The following error metrics can be interpreted as the average test error 
<table>
<thead>
    <tr>
        <td>Model</td>
        <td>Average Pricing Error</td>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Multivariable Regression</td>
        <td>$1.65</td>
    </tr>
        <tr>
        <td>Lasso Regression</td>
        <td>$1.79</td>
    </tr>
    </tr>
        <tr>
        <td>Elasticnet Regression</td>
        <td>$1.66</td>
    </tr> 
    </tr>
        <tr>
        <td>Extra Trees Regressor</td>
        <td>$1.54</td>
    </tr> 
        <tr>
        <td>XGBoost</td>
        <td>$1.53</td>
    </tr> 
            <tr>
        <td>Stacked Regression</td>
        <td>$1.57</td>
    </tr> 
</tbody>
</table>