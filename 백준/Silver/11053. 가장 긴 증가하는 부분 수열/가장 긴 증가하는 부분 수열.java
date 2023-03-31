import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int arr[] = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int dp[] = new int[n];

        int ans = 0;
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]){
                    if (cnt < dp[j])
                        cnt = dp[j];
                }
            }
            dp[i] = cnt + 1;
            ans = Math.max(ans, dp[i]);
        }
        System.out.println(ans);
    }
}