import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n,m, tmp[][], arr[][], ans;

    static int virus(int i, int j){
        int offset[][] = {{-1,0},{0,-1},{1,0},{0,1}};
        int res = 1;
        tmp[i][j] = 3;

        for (int idx = 0; idx < 4; idx++) {
            int di = i + offset[idx][0];
            int dj = j + offset[idx][1];
            if (di < 0 || di >= n || dj < 0 || dj >= m || (tmp[di][dj] != 0 && tmp[di][dj] != 2))
                continue;
            tmp[di][dj] = 3;
            res += virus(di, dj);
        }
        return res;
    }

    static void fence(int cnt, int y, int x){
        if (cnt == 3){
            for (int i = 0; i < n; i++) {
                tmp[i] = arr[i].clone();
            }
            int res = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (tmp[i][j] == 2)
                        virus(i, j);
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (tmp[i][j] == 0)
                        res += 1;
                }
            }
            ans = Math.max(res, ans);
            return;
        }

        for (int i = y; i < n; i++) {
            for (int j = x; j < m; j++) {
                if (arr[i][j] == 0){
                    arr[i][j] = 1;
                    int dj = j + 1;
                    int di = i;
                    if (dj >= m){
                        dj = 0;
                        di += 1;
                    }
                    fence(cnt+1, di, dj);
                    arr[i][j] = 0;
                }
            }
            x = 0;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        tmp = new int[n][m];
        int f = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        fence(0, 0, 0);
        System.out.println(ans);
    }
}