import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int dp[][] = new int[n+1][k+1];
        int things[][] = new int[n+1][2];

        for (int i = 1; i < n+1; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            things[i][0] = w;
            things[i][1] = v;
        }

        for (int i = 1; i < n+1; i++) {
            int w = things[i][0];
            int v = things[i][1];

            for (int j = 1; j < k+1; j++) {
                if (j < w)
                    dp[i][j] = dp[i-1][j];
                else if(j == w)
                    dp[i][j] = Math.max(dp[i-1][j], v);
                else
                    dp[i][j] = Math.max(dp[i-1][j], v + dp[i-1][j-w]);
            }
        }
        System.out.println(dp[n][k]);
    }
}