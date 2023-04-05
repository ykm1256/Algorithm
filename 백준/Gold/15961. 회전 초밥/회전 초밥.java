import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        ArrayList<Integer> sushi = new ArrayList<>();
        int[] chk = new int[3001];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            sushi.add(Integer.parseInt(st.nextToken()));
        }

        int cnt = 0;
        for (int i = 0; i < k; i++) {
            if (chk[sushi.get(i)] == 0)
                cnt += 1;
            chk[sushi.get(i)] += 1;
        }

        int ans = cnt;
        if (chk[c] == 0)
            ans++;

        for (int i = 1; i < n; i++) {
            int e = i + k - 1;

            if (e >= n)
                e %= n;

            chk[sushi.get(i-1)] -= 1;
            if (chk[sushi.get(i-1)] == 0)
                cnt -= 1;

            if (chk[sushi.get(e)] == 0)
                cnt += 1;
            chk[sushi.get(e)] += 1;

            if (cnt >= ans){
                if (chk[c] == 0)
                    ans = cnt + 1;
                else
                    ans = cnt;
            }
        }
        System.out.println(ans);
    }
}