class Perceptron:

    def __init__(self):
        self.weights = [0.0, 0.0]
        self.bias = 0.0

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, price, score):
        z = (
            self.weights[0] * price +
            self.weights[1] * score +
            self.bias
        )
        return self.activation(z)

    def train(self, dataset, epochs=100, lr=0.01):
        for _ in range(epochs):
            for price, score, target in dataset:
                y_pred = self.predict(price, score)
                error = target - y_pred

               
                self.weights[0] += lr * error * price
                self.weights[1] += lr * error * score
                self.bias += lr * error