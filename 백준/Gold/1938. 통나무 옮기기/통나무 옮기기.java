import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    // 큐에 넣을 클래스로 현재 위치 정보와 이동횟수, 상태정보가 담김
    static class Info{
        int x, y, status, cnt;

        public Info(int x, int y, int status, int cnt) {
            this.x = x;
            this.y = y;
            this.status = status;
            this.cnt = cnt;
        }
    }

    // 회전할 수 있는지 검사
    static boolean isPossible(int x, int y, int N, char[][] board){
        int sx = x-1;
        int sy = y-1;

        if (x + 1 >= N || y+1 >= N)
            return false;

        // 3*3을 탐색하여 회전할 수 있는지 검사
        for (int i = sy; i < sy+3; i++) {
            for (int j = sx; j < sx+3; j++) {
                if (i < 0 || i >= N || j < 0 || j >= N)
                    return false;
                if (board[i][j] == '1')
                    return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        char[][] board = new char[N][N];
        // 방문배열 마지막 인덱스 0이 세로, 1이 가로
        boolean[][][] chk = new boolean[N][N][2];
        // B들의 위치
        int[][] posB = new int[3][2];
        // E들의 위치
        int[][] posE = new int[3][2];


        int cntB = 0;
        int cntE = 0;
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                char c = s.charAt(j);
                if (c == 'B'){
                    // B일 때 board에는 '0'을 넣고 posB에 B의 위치 저장
                    board[i][j] = '0';
                    posB[cntB][0] = i;
                    posB[cntB][1] = j;
                    cntB += 1;
                }
                else if (c == 'E'){
                    // E일 때 board에는 '0'을 넣고 posE에 E의 위치 저장
                    board[i][j] = '0';
                    posE[cntE][0] = i;
                    posE[cntE][1] = j;
                    cntE += 1;
                }
                else
                    board[i][j] = c;
            }
        }

        int status = 0;
        // 세로이면
        if (posB[0][0] != posB[1][0])
            chk[posB[1][0]][posB[1][1]][0] = true;
        // 가로이면
        else{
            chk[posB[1][0]][posB[1][1]][1] = true;
            status = 1;
        }

        // ansStatus에 목적지 상태값 저장 디폴트로 0(세로)
        int ansStatus = 0;
        // 가로이면 1로 저장
        if (posE[0][0] == posE[1][0])
            ansStatus = 1;



        int ans = 0;
        int[][] offset = {{0,1},{0,-1},{1,0},{-1,0}};
        Queue<Info> queue = new ArrayDeque<>();
        // 큐에는 현재 B의 위치 중 중간 위치와, 이동 횟수, 가로/세로를 판별하는 status 변수가 있는 Info 객체를 담음
        // 초기 위치 정보 큐에 담아주기
        queue.offer(new Info(posB[1][1], posB[1][0], status, 0));
        while (!queue.isEmpty()){
            Info now = queue.poll();

            //4 방향 이동
            for (int i = 0; i < 4; i++) {
                int dx = now.x + offset[i][1];
                int dy = now.y + offset[i][0];

                // 세로일 때 배열 범위 벗어나면 continue
                if (now.status == 0 && (dy - 1 < 0 || dy + 1 >= N || dx < 0 || dx >= N))
                    continue;
                // 가로일 때 배열 범위 벗어나면 continue
                else if(now.status == 1 && (dx - 1 < 0 || dx + 1 >= N || dy < 0 || dy >= N))
                    continue;
                // 이미 방문한 곳이면 continue
                if (chk[dy][dx][now.status])
                    continue;
                boolean flag = true;
                // 세로일 때 세 점의 위치를 탐색하여 기둥이 있으면 continue
                if (now.status == 0){
                    for (int j = 0; j < 3; j++) {
                        if (board[dy-1+j][dx] == '1'){
                            flag = false;
                            break;
                        }
                    }
                }
                // 가로일 때 세 점의 위치를 탐색하여 기둥이 있으면 continue
                else{
                    for (int j = 0; j < 3; j++) {
                        if (board[dy][dx-1+j] == '1'){
                            flag = false;
                            break;
                        }
                    }
                }
                if(!flag)
                    continue;

                // 목적지의 중간 좌표이고, 목적지의 상태와 같으면 멈춤
                if (ansStatus == now.status && posE[1][0] == dy && posE[1][1] == dx){
                    ans = now.cnt + 1;
                    queue.clear();
                    break;
                }

                chk[dy][dx][now.status] = true;
                queue.offer(new Info(dx, dy, now.status, now.cnt + 1));
            }
            // 세로일 때 회전이 가능하면 회전
            if (!queue.isEmpty() && now.status == 0 && isPossible(now.x, now.y, N, board)){
                // 방문하지 않은 위치이면 회전시킴
                if (!chk[now.y][now.x][1]){
                    // 회전 후 목적지이면 break
                    if (now.x == posE[1][1] && now.y == posE[1][0] && ansStatus == 1){
                        ans = now.cnt + 1;
                        break;
                    }
                    // 아니라면 큐에 담음
                    else{
                        chk[now.y][now.x][1] = true;
                        queue.offer(new Info(now.x, now.y, 1, now.cnt+1));
                    }
                }
            }
            // 가로일 때 회전이 가능하면 회전
            else if(!queue.isEmpty() && now.status == 1 && isPossible(now.x, now.y, N, board)){
                // 방문하지 않은 위치이면 회전시킴
                if (!chk[now.y][now.x][0]){
                    // 회전 후 목적지이면 break
                    if (now.x == posE[1][1] && now.y == posE[1][0] && ansStatus == 0){
                        ans = now.cnt + 1;
                        break;
                    }
                    // 아니라면 큐에 담음
                    else{
                        chk[now.y][now.x][0] = true;
                        queue.offer(new Info(now.x, now.y, 0, now.cnt+1));
                    }
                }
            }
        }
        System.out.println(ans);
    }
}