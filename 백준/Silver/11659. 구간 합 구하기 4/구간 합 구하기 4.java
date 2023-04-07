import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int numbers[] = new int[n];
        int sum[] = new int[n];
        for (int i = 0;i<n;i++){
            numbers[i] = sc.nextInt();
            if (i == 0)
                sum[i] = numbers[i];
            else{
                sum[i] = sum[i-1] + numbers[i];
            }
        }

        for (int t=0;t<m;t++){
            int s = sc.nextInt();
            int e = sc.nextInt();
            if (s == 1)
                System.out.println(sum[e-1]);
            else
                System.out.println(sum[e-1]-sum[s-2]);
        }


    }
}
