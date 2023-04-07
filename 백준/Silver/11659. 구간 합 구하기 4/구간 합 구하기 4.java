import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[] tree;
    static int n;

    static int sum(int i) {
        int ans = 0;
        while (i > 0) {
            ans += tree[i];
            i -= (i & -i);
        }
        return ans;
    }

    static void update(int i, int num) {
        while (i <= n) {
            tree[i] += num;
            i += (i & -i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        tree = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            update(i, Integer.parseInt(st.nextToken()));
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(sum(e) - sum(s-1));
        }
    }
}