import pandas as pd
import matplotlib.pyplot as plt

caminho_csv = 'csv/metricas_finais.csv' 
df = pd.read_csv(caminho_csv)

df = df.sort_values(by='Tamanho_N')

# df['tempo_medio_ms'] = df['TempoMedio_ns'] / 1_000_000.0  
# df['desvio_padrao_ms'] = df['DesvioPadrao_ns'] / 1_000_000.0

algoritmos = df['Algoritmo'].unique()

algoritmos_formatados = {
    'quickfind': 'QuickFind',
    'quickunion': 'QuickUnion',
    'quickunionponderado': 'QuickUnion Ponderado'
}

fig, axes = plt.subplots(1, len(algoritmos), figsize=(18, 6))

for i, algoritmo in enumerate(algoritmos):
    ax = axes[i]
    
    dados_alg = df[df['Algoritmo'] == algoritmo]
    
    ax.errorbar(
        x=dados_alg['Tamanho_N'], 
        y=dados_alg['TempoMedio_ns'], 
        yerr=dados_alg['DesvioPadrao_ns'], 
        fmt='-o',          
        capsize=5,         
        label='Média ± Desvio Padrão',
        color="#744ebb"    
    )

    nome_exibicao = algoritmos_formatados.get(algoritmo, algoritmo)
    
    ax.set_title(f'{nome_exibicao}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Tamanho da Entrada (N)', fontsize=12)
    ax.set_ylabel('Tempo (ns)', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

fig.suptitle('Curva de Crescimento: Tamanho x Tempo', fontsize=16)
plt.tight_layout()
plt.savefig('visualizacoes/grafico_crescimento.png', dpi=300, bbox_inches='tight')
plt.show()