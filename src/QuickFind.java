public class QuickFind implements UnionFind {
    private int count, acessosId = 0;
    private int[] id;

    public QuickFind(int n) {
        this.count = n;
        id = new int[n];
        for(int i=0; i<n; i++) {
            id[i] = i;
        }
    }

    @Override
    public int find(int p) {
        acessosId++;
        return id[p];
    }

    @Override
    public void union(int p, int q) {
        int pID = find(p);
        int qID = find(q);

        if(pID == qID) return;

        for(int i=0; i<id.length; i++) {
            if(id[i] == pID) {
                id[i] = qID;
                acessosId++;
            }
        }
        count--;
    }

    @Override
    public boolean connected(int p, int q) {
        return find(p)==find(q);
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
