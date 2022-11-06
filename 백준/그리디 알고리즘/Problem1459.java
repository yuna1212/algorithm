/*
 * 시작 시간: 2022년 11월 7일 9:19 PM
 * 소요 시간: 2시간 30분
 * 풀이 방법: 분기문 여럿 쓰는 것보다 모든 경우의 수를 살펴보는게 이득이다.
 */
import java.io.*;
import java.util.StringTokenizer;


public class Problem1459 {
    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long x = Long.parseLong(st.nextToken());
        long y = Long.parseLong(st.nextToken());
        long w = Long.parseLong(st.nextToken());
        long s = Long.parseLong(st.nextToken());
        if (x < y){
            // 무조건 세로가 더 길다
            long tmp = x;
            x = y; y = tmp;
        }

        // 풀이
        
        // 축으로만 이동하는 경우
        long ans = (x+y)*w;
        long diagonalCounting = Math.max(x, y);
        long restDiagonal = (x+y)%2;
        ans = Math.min(ans, (diagonalCounting - restDiagonal)*s + restDiagonal*w);

        diagonalCounting = Math.min(x, y);
        long restX = x - diagonalCounting;
        long restY = y - diagonalCounting;
        ans = Math.min(ans, diagonalCounting*s + (restX + restY)*w);
        
        // 출력
        System.out.println(ans);
            
    }
}

