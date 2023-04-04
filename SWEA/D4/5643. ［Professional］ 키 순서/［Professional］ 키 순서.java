import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    static int[][] shorter, taller;

    static int[] chkS, chkT;
    static int n, m;

    static int dirShort(int node){
        int ret = 1;
        for (int i = 0; i < n; i++) {
            if (chkS[i] == 0 && shorter[node][i] == 1){
                chkS[i] = 1;
                ret += dirShort(i);
            }
        }
        return ret;
    }

    static int dirTall(int node){
        int ret = 1;

        for (int i = 0; i < n; i++) {
            if (chkT[i] == 0 && taller[node][i] == 1){
                chkT[i] = 1;
                ret += dirTall(i);
            }
        }
        return ret;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            shorter = new int[n][n];
            taller = new int[n][n];
            chkS = new int[n];
            chkT = new int[n];
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken()) - 1;
                int b = Integer.parseInt(st.nextToken()) - 1;
                shorter[b][a] = 1;
                taller[a][b] = 1;
            }


            int ans = 0;
            for (int i = 0; i < n; i++) {
                chkS = new int[n];
                chkT = new int[n];
                chkS[i] = 1;
                chkT[i] = 1;
                int s = dirShort(i);
                int t = dirTall(i);
                if (s+t-2 == n-1)
                    ans += 1;
            }
            System.out.println("#" + tc + " " + ans);
//            sb.append("#" + tc + " " + ans + "\n");
        }

    }
}