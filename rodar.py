import os
import subprocess
import re
import csv

ARQUIVO_JAVA = "src/App.java"
DIRETORIO_BIN = "bin"
ALGORITMOS = ["quickunionponderado"]
PASTAS_TESTE = ["instancias"]

def rodar_experimentos():
    raiz = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(raiz, "csv"), exist_ok=True)

    with open(ARQUIVO_JAVA, "r", encoding="utf-8") as f:
        codigo_original = f.read()

    try:
        with open("metricas_finais.csv", "w", newline="", encoding="utf-8") as f_csv:
            escritor = csv.writer(f_csv)
            escritor.writerow(["Algoritmo", "Tamanho_N", "Arquivo", "TempoMedio_ns", "DesvioPadrao_ns"])

            for alg in ALGORITMOS:
                for pasta in PASTAS_TESTE:
                    if not os.path.exists(pasta):
                        continue
                    for arq in sorted(os.listdir(pasta)):
                        if not arq.endswith(".txt"):
                            continue

                        caminho_real = os.path.join(pasta, arq)
                        with open(caminho_real, "r") as f_txt:
                            try:
                                tamanho_n = int(f_txt.readline().strip())
                            except ValueError:
                                tamanho_n = "Erro_Leitura"

                        nome_para_java = arq.replace(".txt", "")

                        print(f">>> Algoritmo: {alg} | Arquivo: {arq} | N: {tamanho_n}")

                        novo_codigo = re.sub(r'String file = ".*?";', f'String file = "{nome_para_java}";', codigo_original)
                        novo_codigo = re.sub(r'String algoritmo = ".*?";', f'String algoritmo = "{alg}";', novo_codigo)

                        with open(ARQUIVO_JAVA, "w", encoding="utf-8") as f:
                            f.write(novo_codigo)

                        compile_result = subprocess.run(
                            f"javac -d {DIRETORIO_BIN} src/*.java",
                            shell=True, capture_output=True, text=True, cwd=raiz
                        )
                        if compile_result.returncode != 0:
                            print(f"    [ERRO DE COMPILAÇÃO]\n{compile_result.stderr}")
                            continue

                        resultado = subprocess.run(
                            f"java -cp {DIRETORIO_BIN} App",
                            shell=True, capture_output=True, text=True, cwd=raiz
                        )

                        if resultado.returncode != 0:
                            print(f"    [ERRO DE EXECUÇÃO]\n{resultado.stderr}")
                            continue

                        match = re.search(
                            r"Tempo Médio:\s*([\d.]+).*?Desvio Padrão:\s*([\d.]+)",
                            resultado.stdout
                        )
                        if match:
                            media, desvio = match.group(1), match.group(2)
                            escritor.writerow([alg, tamanho_n, arq, media, desvio])
                            print(f"    [OK] {alg} | {arq} | média: {media} ns")
                        else:
                            print(f"    [AVISO] Saída inesperada:\n{resultado.stdout}\n{resultado.stderr}")

    finally:
        with open(ARQUIVO_JAVA, "w", encoding="utf-8") as f:
            f.write(codigo_original)
        print("\n--- Processo concluído e App.java restaurado! ---")

if __name__ == "__main__":
    rodar_experimentos()