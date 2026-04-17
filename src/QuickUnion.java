public class QuickUnion implements UnionFind {
    private int count, acessosId = 0;
    private int[] id;

    public QuickUnion(int n) {
        this.count = n;
        id = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
        }
    }

    @Override
    public int find(int p) {
        acessosId++;
        while(p!=id[p]) {
            acessosId++;
            p = id[p];

            acessosId++;
        }
        return p;
    }

    @Override
    public void union(int p, int q) {
        int pRoot = find(p);
        int qRoot = find(q);
        if(pRoot == qRoot) return;

        id[pRoot] = qRoot;
        acessosId++;

        count--;
    }


    @Override
    public boolean connected(int p, int q) {
        return find(p) == find(q);
    }

    @Override
    public int count() {
        return count;
    }

    @Override
    public int getAcessosId() {
        return acessosId;
    }

    @Override
    public void resetarAcessosId() {
        acessosId = 0;
    }
}
