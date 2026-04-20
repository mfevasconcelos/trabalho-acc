# Trabalho Prático 01 – Algoritmos Union–Find e Conectividade Dinâmica

Este é um projeto Java criado no VSCode destinado à análise de desempenho de diferentes abordagens do problema de Conectividade Dinâmica (Union-Find). O projeto também inclui scripts Python para geração de instâncias de teste e visualização de resultados em gráficos.

## Estrutura do Projeto

### Pastas

`src/`: código-fonte Java (algoritmos e classe principal).

`instancias/`: pasta destinada aos arquivos de entrada (.txt).

`csv/`: resultados das métricas gerados após a execução do Java.

`visualizacoes/`: gráficos gerados pelos scripts de plotagem.

### Scripts Python

`gerar_instancia.py`: cria novos cenários de teste.

`plotagem.py` / `plot_resultados.py`: scripts para geração de gráficos comparativos.

## Instruções de Uso

### Para os testes (Java)

De preferência no VSCode

1. Adicione a instância desejada para o teste na pasta `\instancias`
2. No topo do arquivo `src/App.java`, altere as seguintes variáveis:
    * A variável `file` deve receber o nome do arquivo da instância, **sem o `.txt`**.
    * Logo em seguida, a variável `algoritmo` recebe a opção de algoritmo para o teste em questão (ex: QuickFind, QuickUnion, QuickUnionPonderado).
    
    Exemplo em `App.java`:

    ```java
    // altere o nome do arquivo e o algoritmo a seguir:
   String file = "adv_10000"; // sem o .txt
   int algoritmo = QuickFind; // opções: quickfind, quickunion, quickUnionPonderado

3. Para executar, pressione `F5` ou clique em Run acima do método `main`, no arquivo `App.java`.

### Geração de dados e plotagem de gráficos

Os scripts Python foram utilizados para processar os arquivos CSV gerados pelo Java e transformá-los em visualizações. É recomendável utilizar um ambiente isolado para as dependências de plotagem (Matplotlib, Pandas).

1. Configuração do ambiente virtual (venv)

    1.1 Criar o ambiente virtual

        python -m venv venv
    
    1.2 Ativar o ambiente (Linux/macOS)

        source venv/bin/activate
    
    1.3 Ativar o ambiente (Windows)

        .\venv\Scripts\activate
    
    1.4 Instalar dependências

        pip install matplotlib pandas

2. Para gerar novas instâncias basta atribuir o tamanho da instância desejada na variável `n` no topo de `gerar_instancia.py`

    Exemplo em `gerar_instancia.py`:
    
      ```python
      # altere aqui o tamanho da instância
      n = 10000
      ```

3. Com o ambiente ativado, utilize o comando

        python gerar_instancia.py

4. Após executar os testes em Java e garantir que os arquivos .csv foram gerados na pasta csv/, utilize os scripts de plotagem

    4.1 Para gerar gráficos de custo de acessos específicos

        python plot_resultados.py
   
   obs.: lembre de alterar a variável instância com o nome do arquivo escolhido, **sem o `.txt`**.

     Exemplo em `gerar_instancia.py`:
  
      ```python
      # nome da instancia
      instancia = 'adv_500000'
      ```

   e caso não tenha executado para todos os três algoritmos, no dicionário `arquivos`, comente a(s) linha(s) do(s) algoritmo(s) que não usou.

     Exemplo em `gerar_instancia.py`:

      ```python
      arquivos = {
          'QuickFind': f'csv/resultados_acessos_{instancia}_quickfind.csv',
          'QuickUnion': f'csv/resultados_acessos_{instancia}_quickunion.csv',
          'QuickUnion Ponderado': f'csv/resultados_acessos_{instancia}_quickunionponderado.csv'
      }
      ```

    4.2 Para gerar o gráfico de crescimento/comparação final
        python plotagem.py

Os gráficos resultantes serão salvos na pasta `visualizacoes/`.

## Tecnologias Utilizadas

* Java 17+: Implementação dos algoritmos core.

* VS Code: IDE principal com extensões Java.

* Python 3: Automação e Ciência de Dados (Matplotlib/Pandas).
