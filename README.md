# ft_linear_regression

This project aims to implement a simple linear regression using the gradient descent method. Here's an overview of key concepts:

## Fundamental Concepts

- **Target Variable (y):** Represents the value we aim to predict.

- **Input Variables (x, x1, x2, ...):** These are the data we use for prediction, forming our dataset.

- **m:** The number of examples in our dataset.

- **n:** The number of features or input variables.

## Linear Regression Model

Our linear regression model aims to predict y using the following equation:

    F(x) = θ1 * x + θ0

Where θ1 is the slope of the regression line, and θ0 is the y-intercept.

## Cost Function (Mean Squared Error)

The cost function measures the performance of our model. For linear regression, we use Mean Squared Error (MSE), calculated as follows:

    MSE = (1/m) * Σ (F(xi) - yi)^2

It represents the average of the squared errors between our model predictions (F(xi)) and the actual values (yi).

## Gradient Descent

Gradient descent is an optimization algorithm used to minimize the cost function. It iteratively adjusts the parameters (θ1 and θ0) using the partial derivatives of the cost function with respect to these parameters.

The algorithm is iterative and uses the following formula to update the parameters (θ1 and θ0):

    θ1_new = θ1_old - α * (1/m) * Σ (F(xi) - yi) * xi
    θ0_new = θ0_old - α * (1/m) * Σ (F(xi) - yi)

Where α is the learning rate, a parameter controlling the step size during gradient descent.

## Running the Project

1. **Install Python:** Ensure you have Python installed on your machine.

2. **Install Dependencies:** Run the following command in your project's terminal to install the necessary dependencies:
   ```bash
   pip install matplotlib
   ```

3. **Run the Program:** Execute the `train.py` script to initiate the model training process.
   ```bash
   python train.py
   ```

4. **Customization:** You can customize the `data.csv` file with your own training data and adjust hyperparameters in the script as needed.

**Using predict.py after Training:**

Once the training is complete, you can use the `predict.py` script for interactive predictions. Run the following command:
```bash
python predict.py
```
Enter the mileage when prompted, and the script will provide the estimated price using the trained model.

**Note:** This readme has been simplified and adapted in accordance with the user's notes, with the assistance of chatGPT for formatting.