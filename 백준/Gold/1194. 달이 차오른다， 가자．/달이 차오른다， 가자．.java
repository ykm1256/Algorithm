import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class Minsik{
        int x, y, cnt, flag;

        public Minsik(int x, int y, int cnt, int flag) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.flag = flag;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int x = 0;
        int y = 0;

        char arr[][] = new char[N][M];
        int dp[][][] = new int[N][M][1<<6];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);
            }
        }
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = str.charAt(j);
                if (arr[i][j] == '0'){
                    x = j;
                    y = i;
                }
            }
        }
        int offset[][] = {{0,1},{0,-1},{1,0},{-1,0}};
        Queue<Minsik> queue = new ArrayDeque<>();
        dp[y][x][0] = 0;
        queue.offer(new Minsik(x,y, 0,0));
        int ans = -1;
        while (!queue.isEmpty()){
            Minsik now = queue.poll();
            if (ans != -1 && now.cnt >= ans)
                continue;

            for (int i = 0; i < 4; i++) {
                int dx = now.x + offset[i][1];
                int dy = now.y + offset[i][0];

                if (dx < 0 || dx >= M || dy < 0 || dy >= N || arr[dy][dx] == '#')
                    continue;

                int f = now.flag;
                if (Character.isUpperCase(arr[dy][dx])){
                    int tmp = Character.toLowerCase(arr[dy][dx]) - 'a';
                    if ((now.flag & (1 << tmp)) == 0)
                        continue;
                }
                else if(Character.isLowerCase(arr[dy][dx])){
                    f = arr[dy][dx] - 'a';
                    f = now.flag | (1 << f);
                }
                if (dp[dy][dx][f] <= now.cnt+1)
                    continue;

                dp[dy][dx][f] = now.cnt+1;
                if (arr[dy][dx] == '1'){
                    if (ans == -1)
                        ans = now.cnt+1;
                    else
                        ans = Math.min(ans, now.cnt+1);
                    continue;
                }
                queue.offer(new Minsik(dx, dy, now.cnt+1, f));

            }
        }
        System.out.println(ans);

    }
}