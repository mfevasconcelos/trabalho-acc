import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class App {
    public record Conexao(int p, int q) {}

    public record EstatisticasTempo(double mediaNs, double desvioPadraoNs) {}

    public static void main(String[] args) {
        // altere o nome do arquivo e o algoritmo a seguir:
        String file = "tinyUF"; // sem o .txt
        String algoritmo = "quickFind";

        try {
            System.out.println("Lendo arquivo...");
            String filePath = "instancias/"+file+".txt";
            List<Conexao> conexoes = lerArquivo(filePath);
            int n = conexoes.remove(0).p(); 

            System.out.println("Iniciando testes de tempo para " + algoritmo + "...");
            EstatisticasTempo statsQF = medirTempoExecucao(n, conexoes, algoritmo);
            System.out.printf("Tempo Médio: %.2f ns | Desvio Padrão: %.2f ns%n", statsQF.mediaNs(), statsQF.desvioPadraoNs());

            System.out.println("Gerando dados de acesso ao vetor para " + algoritmo + "...");
            gerarDadosAcessoVetor(n, conexoes, algoritmo, "csv/resultados_acessos_" + file + "_" + algoritmo + ".csv");

            System.out.println("Processo concluído!");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static List<Conexao> lerArquivo(String file) throws IOException {
        List<Conexao> lista = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String primeiraLinha = br.readLine();
            if (primeiraLinha != null) {
                lista.add(new Conexao(Integer.parseInt(primeiraLinha.trim()), 0));
            }

            String linha;
            while ((linha = br.readLine()) != null) {
                String[] elementos = linha.trim().split("\\s+");
                if (elementos.length == 2) {
                    lista.add(new Conexao(Integer.parseInt(elementos[0]), Integer.parseInt(elementos[1])));
                }
            }
        }
        return lista;
    }

    public static EstatisticasTempo medirTempoExecucao(int n, List<Conexao> conexoes, String tipoAlgoritmo) {
        int numExecucoes = 10;
        long[] tempos = new long[numExecucoes];

        for (int i = 0; i < numExecucoes; i++) {
            UnionFind uf = instanciarAlgoritmo(tipoAlgoritmo, n);

            long inicio = System.nanoTime();
            for (Conexao c : conexoes) {
                uf.union(c.p(), c.q());
            }
            long fim = System.nanoTime();
            
            tempos[i] = fim - inicio;
        }

        double soma = 0;
        for (long t : tempos) soma += t;
        double media = soma / numExecucoes;

        double somaDiferencasQuadrado = 0;
        for (long t : tempos) {
            somaDiferencasQuadrado += Math.pow(t - media, 2);
        }
        double desvioPadrao = Math.sqrt(somaDiferencasQuadrado / numExecucoes);

        return new EstatisticasTempo(media, desvioPadrao);
    }

    public static void gerarDadosAcessoVetor(int n, List<Conexao> conexoes, String tipoAlgoritmo, String arquivoSaida) throws IOException {
        UnionFind uf = instanciarAlgoritmo(tipoAlgoritmo, n);
        
        try (FileWriter csvWriter = new FileWriter(arquivoSaida)) {
            csvWriter.append("i,custo_i,total_i,custo_medio_i\n");

            long total_i = 0;
            int i = 1;

            for (Conexao c : conexoes) {
                int acessosAntes = uf.getAcessosId();
                uf.union(c.p(), c.q());
                int acessosDepois = uf.getAcessosId();

                long custo_i = acessosDepois - acessosAntes;
                total_i += custo_i;
                double custo_medio_i = (double) total_i / i;

                csvWriter.append(String.format("%d,%d,%d,%.2f\n", i, custo_i, total_i, custo_medio_i));
                i++;
            }
        }
    }

    private static UnionFind instanciarAlgoritmo(String tipo, int n) {
        switch (tipo.toLowerCase()) {
            case "quickfind":
                return new QuickFind(n);
            case "quickunion":
                return new QuickUnion(n);
            case "quickUnionponderado":
                return new QuickUnionPonderado(n);
            default:
                throw new IllegalArgumentException("Algoritmo desconhecido");
        }
    }
}