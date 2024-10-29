import numpy as np
import pandas as pd
import json

def load_data(file_path):
    """Carga los datos desde un archivo CSV."""
    return pd.read_csv(file_path)

def normalize_features(X):
    """Normaliza las características."""
    return (X - X.mean()) / X.std()

def add_intercept(X):
    """Agrega una columna de unos a la matriz de características para el término independiente."""
    return np.column_stack((np.ones(X.shape[0]), X))

def gradient_descent(X, y, theta, learning_rate, iterations):
    """Ejecuta el algoritmo de descenso del gradiente."""
    m = len(y)
    for _ in range(iterations):
        h = np.dot(X, theta)
        gradient = np.dot(X.T, (h - y)) / m
        theta -= learning_rate * gradient
    return theta

def save_theta_to_json(theta, file_path):
    """Guarda los parámetros en un archivo JSON."""
    with open(file_path, 'w') as f:
        json.dump({"theta0": float(theta[0]), "theta1": float(theta[1])}, f, indent=4)

if __name__ == '__main__':
    # Cargar los datos
    data = load_data('data/data.csv')

    # Extraer características (X) y variable objetivo (y)
    X = data['km'].values
    y = data['price'].values

    # Normalizar las características
    X_normalized = normalize_features(X)

    # Agregar una columna de unos para el término independiente
    X_with_intercept = add_intercept(X_normalized)

    # Inicializar parámetros
    theta = np.zeros(2)
    learning_rate = 0.01
    iterations = 1000

    # Ejecutar descenso del gradiente
    theta = gradient_descent(X_with_intercept, y, theta, learning_rate, iterations)

    # Desnormalizar theta[1] (pendiente)
    theta[1] = theta[1] * y.std() / X_normalized.std()

    # Ajustar theta[0] (intercepto) para desnormalización
    theta[0] = y.mean() - theta[1] * X_normalized.mean()

    # Guardar los resultados en theta.json
    save_theta_to_json(theta, 'src/theta.json')

    print("Los coeficientes de la regresión lineal han sido guardados en src/theta.json")