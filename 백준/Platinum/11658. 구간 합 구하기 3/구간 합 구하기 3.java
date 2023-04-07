import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static long[][] tree;
    static int n;

    static long sum(int i, int j) {
        long ans = 0;
        while (i > 0){
            int idxJ = j;
            while (idxJ > 0) {
                ans += tree[i][idxJ];
                idxJ -= (idxJ & -idxJ);
            }
            i -= (i & -i);
        }
        return ans;
    }

    static void update(int i, int j, long num) {
        while (i <= n){
            int idxJ = j;
            while (idxJ <= n) {
                tree[i][idxJ] += num;
                idxJ += (idxJ & -idxJ);
            }
            i += (i & -i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        tree = new long[(n + 1)][(n + 1)];
        long[][] arr = new long[(n + 1)][(n + 1)];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                long value = Long.parseLong(st.nextToken());
                update(i, j, value);
                arr[i][j] = value;
            }
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());

            if (w == 0) {
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                update(x, y, arr[x][y] * (-1));
                update(x, y, c);
                arr[x][y] = c;
            } else {
                int x1 = Integer.parseInt(st.nextToken());
                int y1 = Integer.parseInt(st.nextToken());
                int x2 = Integer.parseInt(st.nextToken());
                int y2 = Integer.parseInt(st.nextToken());
                long ans = sum(x2,y2) - sum(x2,y1-1) - sum(x1-1,y2) + sum(x1 - 1 , y1 - 1);
                sb.append(ans + "\n");
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}