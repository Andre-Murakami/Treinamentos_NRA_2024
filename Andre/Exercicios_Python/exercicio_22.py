import numpy as np
import matplotlib.pyplot as plt

# Gerar dados aleatórios usando numpy
x = np.linspace(0, 10, 100)  
y = np.random.randn(100)  

# Criar um gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Dados Aleatórios')

# Adicionar título e rótulos
plt.title('Gráfico de Dados Aleatórios')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar uma legenda
plt.legend()

# Mostrar o gráfico
plt.show()
