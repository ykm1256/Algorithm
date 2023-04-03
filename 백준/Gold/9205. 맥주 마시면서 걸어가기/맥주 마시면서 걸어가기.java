import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int distance(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());


            int[][] pos = new int[n + 2][2];
            int[][] arr = new int[n+2][n+2];
            for (int i = 0; i < n + 2; i++) {
                st = new StringTokenizer(br.readLine());
                pos[i][0] = Integer.parseInt(st.nextToken());
                pos[i][1] = Integer.parseInt(st.nextToken());
            }
            for (int i = 0; i < n + 2; i++) {
                for (int j = 0; j < n + 2; j++) {
                    if (i==j)
                        continue;
                    if (distance(pos[i][0], pos[i][1], pos[j][0], pos[j][1]) <= 1000)
                        arr[i][j] = 1;
                }
            }
            int[] chk = new int[n+2];
            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(0);
            String ans = "sad";
            while (!queue.isEmpty() && ans.equals("sad")){
                int now = queue.poll();

                for (int i = 0; i < n+2; i++) {
                    if (arr[now][i] == 1 && chk[i] == 0){
                        if (i == n+1){
                            ans = "happy";
                            break;
                        }
                        chk[i] = 1;
                        queue.offer(i);
                    }
                }
            }
            System.out.println(ans);
        }
    }
}