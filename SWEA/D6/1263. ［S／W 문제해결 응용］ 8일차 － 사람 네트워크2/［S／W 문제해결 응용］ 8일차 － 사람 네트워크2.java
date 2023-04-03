import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int[][] offset = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int[][] arr = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            int[][] dist = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (arr[i][j] == 0 && i != j)
                        dist[i][j] = N*N;
                    else
                        dist[i][j] = arr[i][j];
                }
            }

            for (int k = 0; k < N; k++) {
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if (dist[i][k] + dist[k][j] < dist[i][j]){
                            dist[i][j] = dist[i][k] + dist[k][j];
                        }
                    }
                }
            }


            int ans = Integer.MAX_VALUE;
            for (int i = 0; i < N; i++) {
                int res = 0;
                for (int d : dist[i]) {
                    res += d;
                }
                ans = Math.min(res, ans);
            }
            System.out.println("#" + tc + " " + ans);

        }
    }

    static class Pos {
        int node, cnt;

        public Pos(int node, int cnt) {
            this.node = node;
            this.cnt = cnt;
        }
    }
}