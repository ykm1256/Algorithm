import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[][] board = new int[9][9];
    static int[][] horizontal = new int[9][9];
    static int[][] vertical = new int[9][9];
    static int[][] square = new int[9][9];

    static int recur(int i, int j){
        if (i == 9 && j == 0)
            return 1;

        int num = board[i][j];
        int s = 3 * (i/3) + (j/3);
        int ans = 0;

        int di = i;
        int dj = j;
        if (j == 8){
            di += 1;
            dj = 0;
        }
        else
            dj += 1;

        if (num != 0){
            vertical[i][num-1] = 1;
            horizontal[j][num-1] = 1;
            square[s][num-1] = 1;
            return recur(di, dj);
        }
        else{
            for (int k = 0; k < 9; k++) {
                if (vertical[i][k] == 0 && horizontal[j][k] == 0 && square[s][k] == 0){
                    board[i][j] = k+1;
                    vertical[i][k] = 1;
                    horizontal[j][k] = 1;
                    square[s][k] = 1;

                    if (recur(di,dj) == 0){
                        vertical[i][k] = 0;
                        horizontal[j][k] = 0;
                        square[s][k] = 0;
                    }
                    else
                        return 1;
                }
            }
        }
        board[i][j] = 0;
        return 0;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) {
            String str = br.readLine();
            for (int j = 0; j < 9; j++) {
                board[i][j] = str.charAt(j) - '0';
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int s = 3 * (i / 3) + (j / 3);
                int num = board[i][j];
                if (num != 0){
                    vertical[i][num-1] = 1;
                    horizontal[j][num-1] = 1;
                    square[s][num-1] = 1;
                }
            }
        }
        recur(0,0);
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(board[i][j]);
            }
            System.out.println();
        }
    }
}