import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re
import os

def gerar_graficos_por_instancia():
    pasta_dados = 'csv'
    arquivos = glob.glob(os.path.join(pasta_dados, 'resultados_acessos_adv_*.csv'))
    
    if not arquivos:
        print(f"Erro: Nenhum arquivo encontrado em '{pasta_dados}/'.")
        return

    # 1. Organizar arquivos por valor de N
    instancias = {}
    for f in arquivos:
        match = re.search(r'adv_(\d+)_(\w+)\.csv', f)
        if match:
            n_valor = match.group(1)
            algo_nome = match.group(2)
            if n_valor not in instancias:
                instancias[n_valor] = []
            instancias[n_valor].append((f, algo_nome))

    # 2. Gerar um gráfico para cada N
    sns.set_theme(style="whitegrid")
    
    for n_valor, arquivos_algo in instancias.items():
        print(f"Gerando gráfico para N = {n_valor}...")
        plt.figure(figsize=(10, 6))
        
        for caminho, algo in arquivos_algo:
            df = pd.read_csv(caminho)
            
            # Amostragem inteligente: mantém o gráfico leve
            passo = max(1, len(df) // 1000)
            df_resumo = df.iloc[::passo, :]
            
            plt.plot(df_resumo['i'], df_resumo['custo_medio_i'], label=algo.upper(), linewidth=2)

        plt.yscale('log')
        plt.title(f'Comparativo Union-Find: Custo de Acessos (N = {n_valor})', fontsize=14)
        plt.xlabel('Iteração (i)')
        plt.ylabel('Custo Médio Acumulado (Log)')
        plt.legend(title="Algoritmos")
        plt.grid(True, which="both", ls="-", alpha=0.5)
        
        # Salva cada gráfico com o nome do N correspondente
        nome_arquivo = f'grafico_N_{n_valor}.png'
        plt.savefig(nome_arquivo, dpi=300)
        print(f" -> Salvo como: {nome_arquivo}")
        plt.close() # Fecha para não sobrecarregar a memória

    print("\nProcesso finalizado! Verifique os arquivos .png na pasta.")

if __name__ == "__main__":
    gerar_graficos_por_instancia()