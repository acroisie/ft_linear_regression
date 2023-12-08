**Note:** This readme has been refactored and adapted based on my notes, with the assistance of chatGPT.

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

# ft_linear_regression

This project implements a simple linear regression using the gradient descent method. It has been refactored and adapted based on my notes, with the assistance of chatGPT.

## Running the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-project.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd your-project
   ```

3. **Create and Activate the Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Training Script:**
   ```bash
   python train.py
   ```

6. **Customization:**
   - You can customize the `data.csv` file with your own training data.
   - Adjust hyperparameters in the script (`train.py`) as needed.

**Making Predictions after Training:**

After training, use the `predict.py` script for interactive predictions. Run the following command:
```bash
python predict.py
```
Enter the mileage when prompted, and the script will provide the estimated price using the trained model.
