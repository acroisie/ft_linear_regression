# ft_linear_regression

This project aims to implement a simple linear regression using the gradient descent method. Here's an overview of key concepts:

## Fundamental Concepts

- **Target Variable (\(y\)):** Represents the value we aim to predict.

- **Input Variables (\(x, x_1, x_2, \ldots\)):** These are the data we use for prediction, forming our dataset.

- **\(m\):** The number of examples in our dataset.

- **\(n\):** The number of features or input variables.

## Linear Regression Model

Our linear regression model aims to predict \(y\) using the following equation:

\[ F(x) = \theta_1 x + \theta_0 \]

Where \(\theta_1\) is the slope of the regression line, and \(\theta_0\) is the y-intercept.

## Cost Function (Mean Squared Error)

The cost function measures the performance of our model. For linear regression, we use Mean Squared Error (MSE), calculated as follows:

\[ \text{MSE} = \frac{1}{m} \sum_{i=1}^{m} (F(x_i) - y_i)^2 \]

It represents the average of the squared errors between our model predictions (\(F(x_i)\)) and the actual values (\(y_i\)).

## Gradient Descent

Gradient descent is an optimization algorithm used to minimize the cost function. It iteratively adjusts the parameters (\(\theta_1\) and \(\theta_0\)) using the partial derivatives of the cost function with respect to these parameters.

The algorithm is iterative and uses the following formula to update the parameters (\(\theta_1\) and \(\theta_0\)):

\[ \theta_{1_{\text{new}}} = \theta_{1_{\text{old}}} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (F(x_i) - y_i) \cdot x_i \]

\[ \theta_{0_{\text{new}}} = \theta_{0_{\text{old}}} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (F(x_i) - y_i) \]

Where \(\alpha\) is the learning rate, a parameter controlling the step size during gradient descent.

## Running the Project

1. **Install Python:** Ensure you have Python installed on your machine.

2. **Install Dependencies:** Run the following command in your project's terminal to install the necessary dependencies:
   ```bash
   pip install numpy matplotlib
   ```

3. **Run the Program:** Execute the `ft_linear_regression.py` script to initiate the model training process.
   ```bash
   python ft_linear_regression.py
   ```

4. **Customization:** You can customize the `data.csv` file with your own training data and adjust hyperparameters in the script as needed.