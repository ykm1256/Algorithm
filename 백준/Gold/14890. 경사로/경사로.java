import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int arr[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int ans = 0;
        // 가로
        for (int i = 0; i < n; i++) {
            int now = arr[i][0];
            int cnt = 1;
            int flag = 1;

            for (int j = 1; j < n; j++) {
                // 높이가 2이상 차이나면
                if (Math.abs(arr[i][j] - now) >= 2){
                    flag = 0;
                    break;
                }
                // 내려올 때 : 내려왔었다는 걸 체크
                else if (now > arr[i][j]){
                    if (flag == 0)
                        break;
                    cnt = 1;
                    now = arr[i][j];
                    // 내려온 적이 있다는 것을 표시
                    flag = 0;
                }
                // 올라갈 때 : 현재 cnt가 x이상인지 체크
                else if (now < arr[i][j]){
                    if (flag == 0)
                        break;
                    if (cnt < x){
                        flag = 0;
                        break;
                    }
                    cnt = 1;
                    now = arr[i][j];

                }
                else
                    cnt += 1;

                // 내려온 적이 있고 cnt가 x 이상이면 경사로 건설
                if (flag == 0 && cnt >= x){
                    flag = 1;
                    cnt -= x;
                }
            }
            ans += flag;
        }

        // 세로
        for (int j = 0; j < n; j++) {
            int now = arr[0][j];
            int cnt = 1;
            int flag = 1;

            for (int i = 1; i < n; i++) {
                // 높이가 2이상 차이나면
                if (Math.abs(arr[i][j] - now) >= 2){
                    flag = 0;
                    break;
                }
                // 내려올 때 : 내려왔었다는 걸 체크
                else if (now > arr[i][j]){
                    if (flag == 0)
                        break;
                    cnt = 1;
                    now = arr[i][j];
                    // 내려온 적이 있다는 것을 표시
                    flag = 0;
                }
                // 올라갈 때 : 현재 cnt가 x이상인지 체크
                else if (now < arr[i][j]){
                    if (flag == 0)
                        break;
                    if (cnt < x){
                        flag = 0;
                        break;
                    }
                    cnt = 1;
                    now = arr[i][j];

                }
                else
                    cnt += 1;

                // 내려온 적이 있고 cnt가 x 이상이면 경사로 건설
                if (flag == 0 && cnt >= x){
                    flag = 1;
                    cnt -= x;
                }
            }
            ans += flag;
        }
        System.out.println(ans);
    }
}