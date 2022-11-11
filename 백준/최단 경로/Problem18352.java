/*
 * 시작 시간: 2022년 11월 11일 10:30 PM
 * 소요 시간: 30분
 * 풀이 방법: 평범한 다익스트라
 */
import java.util.*;
import java.io.*;

class City{
    List<List<Integer>> map;
    int start, target;

    public City(List<List<Integer>> map, int start, int target){
        this.map = map;
        this.start = start;
        this.target = target;
    }

    public List<Integer> dijk(){
        List<Integer> ret = new ArrayList<>();
        boolean[] visited = new boolean[map.size()];
        // (최단 거리, 노드)
        Queue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                if(o1[0] > o2[0]) return 1;
                if(o1[0] < o2[0]) return -1;
                return 0;
            }
        });

        heap.add(new int[] {0, start});
        while(!heap.isEmpty()){
            int[] element = heap.poll();
            // 방문했으면 다음 루프
            if(visited[element[1]]) 
                continue;

            // 방문했다 표시하고 현재 거리가 목표와 같다면 추가
            visited[element[1]] = true;
            if(element[0] == target){
                ret.add(element[1]);
                continue;
            }

            element[0]++;
            for(int next: map.get(element[1]))
                heap.add(new int[]{element[0], next});
        }
        return ret; 
        
    }
}
public class Problem18352{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n, m, k, x; // 도시 개수, 도로 개수, 최단 거리, 출발 도시
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken())+1;
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        List<List<Integer>> map = new ArrayList<>(n);
        for(int i = 0; i < n; i++)
            map.add(new ArrayList<>());
        for(int i = 0; i < m; i++){
            int start, end;
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken()); 
            end = Integer.parseInt(st.nextToken());
            map.get(start).add(end);
        }

        City city = new City(map, x, k);
        List<Integer> ans = city.dijk();
        if(ans.isEmpty())
            System.out.println(-1);
        else{
            ans.sort(Comparator.naturalOrder());
            for(int element: ans)
                System.out.println(element);
        }
    }
}
