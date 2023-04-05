import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class Info{
        int y, x, time;
        char value;

        public Info(int y, int x, char value, int time) {
            this.y = y;
            this.x = x;
            this.value = value;
            this.time = time;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[][] offset = {{0,1},{0,-1},{1,0},{-1,0}};

        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        Point hedge, beaver;
        ArrayList<Point> waters = new ArrayList<>();
        hedge = null;
        beaver = null;
        char[][] arr = new char[r][c];
        for (int i = 0; i < r; i++) {
            String str = br.readLine();
            for (int j = 0; j < c; j++) {
                arr[i][j] = str.charAt(j);
                if (arr[i][j] == 'D')
                    beaver = new Point(j, i);
                else if(arr[i][j] == '*')
                    waters.add(new Point(j, i));
                else if(arr[i][j] == 'S'){
                    hedge = new Point(j, i);
                    arr[i][j] = '.';
                }
            }
        }
        Queue<Info> queue= new ArrayDeque<>();
        for (Point water : waters) {
            queue.offer(new Info(water.y, water.x, '*', 0));
        }
        queue.offer(new Info(hedge.y, hedge.x, 'S', 0));

        int[][] chk = new int[r][c];
        chk[hedge.y][hedge.x] = 1;
        int ans = -1;
        while(!queue.isEmpty() && ans == -1){
            Info now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int dx = now.x + offset[i][1];
                int dy = now.y + offset[i][0];

                if (dx < 0 || dx >= c || dy < 0 || dy >= r || arr[dy][dx] == 'X')
                    continue;

                //물일 때
                if (now.value=='*'){
                    if (arr[dy][dx] != '.')
                        continue;
                    arr[dy][dx] = '*';
                    queue.offer(new Info(dy, dx, '*', now.time+1));
                }
                // 고슴도치일 때
                else{
                    if (arr[dy][dx] == 'D'){
                        ans = now.time+1;
                        break;
                    }
                    if (arr[dy][dx] != '.' || chk[dy][dx] == 1)
                        continue;
                    chk[dy][dx] = 1;
                    queue.offer(new Info(dy, dx, 'S', now.time+1));
                }
            }
        }
        System.out.println(ans != -1? ans : "KAKTUS");
    }
}