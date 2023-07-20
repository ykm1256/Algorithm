import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Queue<Integer> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        long sum1 = 0;
        long sum2 = 0;
        for(int i = 0; i<queue1.length; i++){
            sum1 += queue1[i];
            sum2 += queue2[i];
            q1.offer(queue1[i]);
            q2.offer(queue2[i]);
        }
        
        int limit = queue1.length + 10;
        
        int p1 = 0;
        int p2 = 0;
        
        while (p1 < limit && p2 < limit){
            if (sum1 < sum2){
                int num = q2.poll();
                sum1 += num;
                sum2 -= num;
                q1.offer(num);
                p1++;
            }
            else if(sum1 > sum2){
                int num = q1.poll();
                sum1 -= num;
                sum2 += num;
                q2.offer(num);
                p2++;
            }
            else{
                return p1+p2;
            }
        }
        return -1;
        
    }
}