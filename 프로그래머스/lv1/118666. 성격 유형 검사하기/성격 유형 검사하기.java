class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int arr[] = new int[26];
        String personality[] = {"RT", "CF", "JM", "AN"};
        for (int i = 0; i<survey.length; i++){
            String s = survey[i];
            int choice = choices[i];
            int idx = 0;
            
            if (choice < 4){
                idx = (int)s.charAt(0) - ((int)'A');
                arr[idx] += 3 - choice + 1;
            }
            else if (choice > 4){
                idx = (int)s.charAt(1) - ((int)'A');
                arr[idx] += choice - (3 + 1);
            }
            else{
                continue;
            }
        }
        for (String p : personality){
            int idx1 = (int)p.charAt(0) - ((int)'A');
            int idx2 = (int)p.charAt(1) - ((int)'A');
            if (arr[idx1] > arr[idx2]){
                answer += p.charAt(0);
            }
            else if (arr[idx1] < arr[idx2]){
                answer += p.charAt(1);
            }
            else{
                if (idx1 < idx2){
                    answer += p.charAt(0);
                }
                else{
                    answer += p.charAt(1);
                }
            }
        }
        return answer;
    }
}