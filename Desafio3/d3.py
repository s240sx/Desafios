import random
import numpy as np

def exercicios_matrizes():
    # --- EXERCÍCIO 1: Matriz 3x3 de zeros com aleatórios ---
    print("\n--- Ex 1: Matriz 3x3 Aleatória ---")
    
    # cria a matriz 3x3 só com zeros primeiro
    matriz_aleatoria = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # preenche com nums aleatórios usando for aninhado
    for i in range(3):
        for j in range(3):
            matriz_aleatoria[i][j] = random.randint(1, 20) # sorteia de 1 a 20
            
    for linha in matriz_aleatoria:
        print(linha)


    # --- EXERCÍCIO 2: Soma de duas matrizes de vendas ---
    print("\n--- Ex 2: Soma de Vendas ---")
    # ex: 2 filiais vendendo 2 produtos
    vendas_semana1 = [[10, 20], [30, 40]] 
    vendas_semana2 = [[15, 5], [10, 20]]
    
    # matriz vazia pra guardar o resultado
    soma_vendas = [[0, 0], [0, 0]]
    total_geral = 0

    for i in range(2):
        for j in range(2):
            soma_vendas[i][j] = vendas_semana1[i][j] + vendas_semana2[i][j]
            total_geral += soma_vendas[i][j] # já vai somando tudo

    print("Matriz final das vendas:", soma_vendas)
    print("Total de tudo: R$", total_geral)


    # --- EXERCÍCIO 3: Matriz de alunos e médias com NumPy ---
    print("\n--- Ex 3: Notas com NumPy ---")
    # linhas = alunos, colunas = notas
    notas = np.array([
        [7.5, 8.0, 9.0],  # Aluno 1
        [5.0, 6.5, 7.0],  # Aluno 2
        [9.0, 9.5, 10.0]  # Aluno 3
    ])
    
    # passando linha por linha pra calcular a média, bem estilo C/Java
    for i in range(len(notas)):
        media = np.mean(notas[i]) # calcula a média só da linha da vez
        print(f"Média do Aluno {i+1}: {media:.2f}")


    # --- EXERCÍCIO 4: Determinante de Matriz 3x3 ---
    print("\n--- Ex 4: Determinante e Sistema Linear ---")
    # coeficientes inventados pra um sistema 3x3
    coeficientes = np.array([
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ])
    
    # calcula o det direto
    det = np.linalg.det(coeficientes)
    print(f"Determinante: {det:.