import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    static int n,m,k;
    static int order[][];
    static int ans = Integer.MAX_VALUE;
    static int path[], chk[];
    static int arr[][];


    public static void cal(int arr[][]){
        for (int idx =0;idx<k;idx++){
            int r = order[path[idx]][0];
            int c = order[path[idx]][1];
            int s = order[path[idx]][2];
            int e = (2*s+1)/2;

            for (int o=0;o<e;o++){
                int tmp = arr[o+r-s][o+c-s];
                for (int j=c-s+o+1; j<c+s+1-o;j++){
                    int tmp2 = arr[o+r-s][j];
                    arr[o+r-s][j] = tmp;
                    tmp = tmp2;
                }

                for (int i=r-s+o+1; i<r+s+1-o;i++){
                    int tmp2 = arr[i][c+s-o];
                    arr[i][c+s-o] = tmp;
                    tmp = tmp2;
                }

                for (int j=c+s+1-o-2; j>c-s+o-1;j--){
                    int tmp2 = arr[r+s-o][j];
                    arr[r+s-o][j] = tmp;
                    tmp = tmp2;
                }

                for (int i=r+s+1-o-2; i>r-s+o-1;i--){
                    int tmp2 = arr[i][c-s+o];
                    arr[i][c-s+o] = tmp;
                    tmp = tmp2;
                }
            }
        }
        for (int i=0;i<n;i++){
            ans = Math.min(ans, Arrays.stream(arr[i]).sum());
        }
    }

    public static int[][] deepCopy(){
        int res[][] = new int[n][m];
        for (int i=0;i<n;i++){
            System.arraycopy(arr[i], 0, res[i], 0, m);
        }
        return res;
    }

    public static void recur(int cnt){
        if (cnt == k){
            cal(deepCopy());
            return;
        }

        for (int i=0;i<k;i++){
            if (chk[i] == 1)
                continue;
            chk[i] = 1;
            path[cnt] = i;
            recur(cnt+1);
            chk[i] = 0;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        order = new int[k][3];
        path = new int[k];
        chk = new int[k];

        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0;i<k;i++){
            st = new StringTokenizer(br.readLine());
            order[i][0] = Integer.parseInt(st.nextToken()) - 1;
            order[i][1] = Integer.parseInt(st.nextToken()) - 1;
            order[i][2] = Integer.parseInt(st.nextToken());
        }

        recur(0);
        System.out.println(ans);
    }
}
