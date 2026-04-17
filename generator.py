import os
import random
from enum import Enum

# Tamanhos exigidos pelo trabalho 
class TamanhoN(Enum):
    N1 = 10000
    N2 = 50000
    N3 = 100000
    N4 = 500000

def criar_pastas():
    if not os.path.exists('instancias_adversariais'):
        os.makedirs('instancias_adversariais')
    if not os.path.exists('instancias_aleatorias'):
        os.makedirs('instancias_aleatorias')

def gerar_arquivos():
    criar_pastas()
    
    for tamanho in TamanhoN:
        n = tamanho.value
        
        # 1. Gerando o arquivo ADVERSARIAL (Obrigatório para o relatório) 
        # Padrão: 0 1, 0 2, 0 3... [cite: 44, 45, 46]
        adv_nome = f"instancias_adversariais/adv_{n}.txt"
        with open(adv_nome, "w") as f:
            f.write(f"{n}\n") # N na primeira linha [cite: 48]
            for i in range(1, n):
                f.write(f"0 {i}\n")
        
        # 2. Gerando o arquivo ALEATÓRIO (Similar aos exemplos do professor)
        # Conexões aleatórias entre 0 e N-1
        ale_nome = f"instancias_aleatorias/ale_{n}.txt"
        with open(ale_nome, "w") as f:
            f.write(f"{n}\n") # N na primeira linha [cite: 48]
            for _ in range(n):
                p = random.randint(0, n - 1)
                q = random.randint(0, n - 1)
                f.write(f"{p} {q}\n")

    print("Todos os arquivos foram gerados com sucesso!")

if __name__ == "__main__":
    gerar_arquivos()