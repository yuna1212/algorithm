/*
 * 시작 시간: 2022년 11월 11일 1:51 PM
 * 소요 시간: 40분
 * 풀이 방법: stack, DFS, 인접행렬
 */

import java.io.*;
import java.util.*;

public class Problem2644{ 
    public static int getChonsu(boolean[][] ilchon, int from, int to){
        int n = ilchon.length;
        boolean[] visited = new boolean[n];
        Stack<List<Integer>> stack = new Stack<>();
        stack.push(Arrays.asList(from, 0));
        while(!stack.empty()){
            List<Integer> relative = stack.pop(); // [ 친척번호, 촌수 ]

            if(relative.get(0) == to) return relative.get(1); 
            if(visited[relative.get(0)]) continue;

            visited[relative.get(0)] = true;
            int nextChonsu = relative.get(1) + 1;
            for(int i = 0; i < n; i++)
                if(ilchon[relative.get(0)][i]) stack.push(Arrays.asList(i, nextChonsu));
        }
        return -1;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int from = Integer.parseInt(st.nextToken());
        int to = Integer.parseInt(st.nextToken());

        boolean[][] ilchon = new boolean[n+1][n+1];
        int m = Integer.parseInt(br.readLine());
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int child = Integer.parseInt(st.nextToken());
            int parent = Integer.parseInt(st.nextToken());
            ilchon[child][parent] = true;
            ilchon[parent][child] = true;
        }
        System.out.println(Problem2644.getChonsu(ilchon, from, to));
    }
}

