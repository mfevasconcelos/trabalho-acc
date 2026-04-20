import pandas as pd
import matplotlib.pyplot as plt

# nome da instancia
instancia = 'adv_500000'

arquivos = {
    'QuickFind': f'csv/resultados_acessos_{instancia}_quickfind.csv',
    'QuickUnion': f'csv/resultados_acessos_{instancia}_quickunion.csv',
    'QuickUnion Ponderado': f'csv/resultados_acessos_{instancia}_quickunionponderado.csv'
}

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for ax, (nome_alg, caminho) in zip(axes, arquivos.items()):
    df = pd.read_csv(caminho)
    
    ax.plot(df['i'], df['custo_i'], color='gray', label='Custo por Operação', alpha=0.7)
    
    ax.plot(df['i'], df['custo_medio_i'], color='red', label='Custo Médio', linewidth=2.5)
    
    ax.set_title(f'{nome_alg}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Número da Operação (i)', fontsize=12)
    ax.set_ylabel('Acessos ao Array', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper right')

fig.suptitle(f'Custo Amortizado: Operação Individual vs Média ({instancia}.txt)', fontsize=16)
plt.tight_layout()
plt.savefig(f'visualizacoes/grafico_custo_{instancia}.png', dpi=300, bbox_inches='tight')

plt.show()