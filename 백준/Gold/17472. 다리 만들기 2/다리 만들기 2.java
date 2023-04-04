import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static int[][] offset = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    static int[][] arr, graph;
    static int[] parents;
    static ArrayList<Line> lines = new ArrayList<>();

    static void chkLand(int x, int y, int num) {
        for (int i = 0; i < 4; i++) {
            int dx = x + offset[i][1];
            int dy = y + offset[i][0];

            if (dx < 0 || dx >= m || dy < 0 || dy >= n || arr[dy][dx] != 1)
                continue;
            arr[dy][dx] = num;
            chkLand(dx, dy, num);
        }
    }

    static boolean isBoundary(int x, int y) {
        if (x < 0 || x >= m || y < 0 || y >= n)
            return false;
        return true;
    }

    static boolean connectBridge(int x, int y, int i, int cnt, int start) {
        int dx = x + offset[i][1];
        int dy = y + offset[i][0];
        boolean res = false;

        if (!isBoundary(dx, dy))
            return false;
        else if (arr[dy][dx] > 1) {
            if (start == arr[dy][dx] - 2 || cnt < 2 || (graph[start][arr[dy][dx] - 2] != 0 && graph[start][arr[dy][dx] - 2] < cnt))
                return false;
            graph[start][arr[dy][dx] - 2] = cnt;
            lines.add(new Line(cnt, start, arr[dy][dx] - 2));
            return true;
        } else if (arr[dy][dx] == -1) {
            res = connectBridge(dx, dy, i, cnt + 1, start);
        } else if (arr[dy][dx] == 0) {
            arr[dy][dx] = -1;
            res = connectBridge(dx, dy, i, cnt + 1, start);
            if (!res)
                arr[dy][dx] = 0;
        }
        return res;
    }

    static void make_bridge() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] > 0) {
                    for (int idx = 0; idx < 4; idx++) {
                        int di = i + offset[idx][0];
                        int dj = j + offset[idx][1];
                        if (isBoundary(dj, di) && (arr[di][dj] == 0 || arr[di][dj] == -1))
                            connectBridge(j, i, idx, 0, arr[i][j] - 2);
                    }
                }
            }
        }
    }

    static int find(int x) {
        if (x == parents[x])
            return x;
        parents[x] = find(parents[x]);
        return parents[x];
    }

    static void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa < pb)
            parents[pb] = pa;
        else
            parents[pa] = pb;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int cntLand = 0;
        int idx = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == 1) {
                    arr[i][j] = idx;
                    cntLand += 1;
                    chkLand(j, i, idx);
                    idx += 1;
                }
            }
        }
        parents = new int[cntLand];
        for (int i = 0; i < cntLand; i++) {
            parents[i] = i;
        }
        graph = new int[cntLand][cntLand];
        make_bridge();
        int[] chk = new int[cntLand];

        Collections.sort(lines);
        int ans = 0;
        for (Line line : lines) {
            if (find(line.start) != find(line.v)) {
                ans += line.cnt;
                union(line.start, line.v);
            }
        }

        for (int i = 0; i < cntLand; i++) {
            if (find(i) != 0) {
                ans = 0;
                break;
            }
        }
        System.out.println(ans > 0 ? ans : -1);
    }

    static class Line implements Comparable<Line> {
        int cnt, start, v;

        public Line(int cnt, int start, int v) {
            this.cnt = cnt;
            this.start = start;
            this.v = v;
        }

        @Override
        public int compareTo(Line o) {
            if (this.cnt == o.cnt){
                if (this.start == o.start)
                    return this.v - o.v;
                return this.start - o.start;
            }
            else
                return this.cnt - o.cnt;
        }
    }
}