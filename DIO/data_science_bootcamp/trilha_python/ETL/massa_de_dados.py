import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
# Gerando uma massa de dados
x, y = make_regression(n_samples=200, n_features=1, noise=30)


# Criacão do Modelo
modelo = LinearRegression()
modelo.fit(x, y)
modelo.predict(x)

# Tracando uma linha central na média dos valores da massa criada

plt.scatter(x, y)
plt.plot(x, modelo.predict(x), color='red', linewidth=3)
plt.show()

