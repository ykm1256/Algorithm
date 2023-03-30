import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class Link{
        int x, y, money;

        public Link(int x, int y, int money) {
            this.x = x;
            this.y = y;
            this.money = money;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int offset[][] = {{0,1},{1,0},{0,-1},{-1,0}};
        int tc = 0;
        while (true){
            tc += 1;
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            if (N == 0)
                break;
            int dp[][] = new int[N][N];
            int cave[][] = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                Arrays.fill(dp[i], Integer.MAX_VALUE);
                for (int j = 0; j < N; j++) {
                    cave[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            Queue<Link> queue = new ArrayDeque<>();
            queue.offer(new Link(0,0, cave[0][0]));
            dp[0][0] = cave[0][0];
            while (!queue.isEmpty()){
                Link now = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int dy = now.y + offset[i][0];
                    int dx = now.x + offset[i][1];

                    if (dy < 0 || dy >= N || dx < 0 || dx >= N)
                        continue;
                    if (now.money + cave[dy][dx] >= dp[dy][dx])
                        continue;
                    dp[dy][dx] = now.money + cave[dy][dx];
                    queue.offer(new Link(dx, dy, now.money+cave[dy][dx]));
                }
            }
            System.out.println("Problem " + tc + ": " + dp[N-1][N-1]);
        }
    }
}