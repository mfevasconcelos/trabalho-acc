public class QuickUnionPonderado implements UnionFind {
    int count, acessosId = 0;
    int[] id, size;

    public QuickUnionPonderado(int n) {
        count = n;
        id = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
            size[i] = 1;
        }
    }

    @Override
    public int find(int p) {
        acessosId++;
        while (p != id[p]) {
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
        if (pRoot == qRoot) return;

        if(size[qRoot] > size[pRoot]) {
            id[pRoot] = qRoot;
            acessosId++;
            size[qRoot] += size[pRoot];
        }
        else {
            id[qRoot] = pRoot;
            acessosId++;
            size[pRoot] += size[qRoot];
        }
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
