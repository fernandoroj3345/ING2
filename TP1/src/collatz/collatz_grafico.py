import matplotlib.pyplot as plt
from collatz import collatz_sequence

def generate_collatz_plot():
    numbers = range(1, 10001)
    iterations = [collatz_sequence(n) for n in numbers]

    plt.figure(figsize=(10, 6))
    plt.scatter(iterations, numbers, color='blue', s=1)
    plt.title('Número de Collatz: Iteraciones vs Número Inicial')
    plt.xlabel('Número de Iteraciones')
    plt.ylabel('Número Inicial (n)')
    plt.grid(True)
    plt.savefig("collatz_plot.png")
    plt.show()

if __name__ == "__main__": 
    generate_collatz_plot()