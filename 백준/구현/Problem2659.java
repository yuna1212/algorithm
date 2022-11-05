/* 
 * 시작 시간: 2022년 11월 5일 5:40 PM
 * 소요 시간: 2시간
 * 풀이 방법: 
 */
import java.io.*;
import java.util.*;

public class Problem2659 {
    public static int getClockNumber(int number) {
        int ret = number;
        for(int i = 0; i < 3; i++) {
            number = number/10 + number%10*1000;
            if(ret > number) ret = number;
        }
        return ret;
    }

    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int e = 3;
        int number = 0;
        while(st.hasMoreTokens()) {
            number += (int) Math.pow(10, e)*Integer.parseInt(st.nextToken());
            e--;
        }
        
        // 시계수 찾기
        int minClockNumber = getClockNumber(number);

        // 몇번째로 작은 시계수인지 구하기
        int ans = 0;
        for (int i = 1111; i < 10000; i++) {
            if (i != getClockNumber(i)) continue;
            if (i > minClockNumber) break;
            ans += 1;
        }
        
        System.out.println(ans);
    }
}

