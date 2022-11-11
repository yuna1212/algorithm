/*
 * 시작 시간: 2022년 11월 11일 7:13 PM
 * 소요 시간: 2시간
 * 풀이 방법: enemy를 계속 deep copy 해야함... 다른 효율적인 방법 찾기
 */

import java.util.*;
import java.io.*;

class Castle{
    List<int[]> enemies;
    int n, m, d; // 행, 열, 거리
    int[] archers = new int[3]; // 궁수 위치
    public int attackingCounter = 0;

    int getDistance(int[] enemy, int archer){
        // 거리 구하기
        return Math.abs(enemy[0] - n) + Math.abs(enemy[1] - archer);
    }
    void setArchers(int first, int second, int third){
        archers[0] = first;
        archers[1] = second;
        archers[2] = third;
        attackingCounter = 0;

    }


    public Castle(List<int[]> enemies, int n, int m, int d){
        this.enemies = enemies;
        this.n = n;
        this.m = m;
        this.d = d;
    }

    public void attack(){
        // 궁수가 가장 가까운 적 공격하기
        List<Integer> attackingIndecies = new ArrayList<>(3);
        int[] attackingDistances = new int[3];
        Arrays.fill(attackingDistances, 16*16);
        for(int enemyIdx = 0; enemyIdx < enemies.size(); enemyIdx++){
            for(int archerIdx = 0; archerIdx < 3; archerIdx++){
                System.out.println(enemyIdx+" "+archerIdx);
                int dist = getDistance(enemies.get(enemyIdx), archers[archerIdx]);
                System.out.println("distance: "+dist);
                if(dist < attackingDistances[archerIdx]){
                    attackingDistances[archerIdx] = dist;
                    attackingIndecies.set(archerIdx, enemyIdx);
                }
            }
        }
        Set<Integer> attackedIndecies = new HashSet<Integer>(); 
        attackingIndecies.sort(Comparator.naturalOrder());
        for(int attackingIndex: attackingIndecies){
            if(attackedIndecies.contains(attackingIndex)) continue;
            enemies.remove(attackingIndex-attackedIndecies.size());
        }
        attackingCounter += attackedIndecies.size();
    }

    public void move(){
        for(int i = 0; i < enemies.size(); i++){
            int[] enemy = enemies.get(i);
            if(enemy == null) continue;
            if(enemy[0] == n-1) enemies.set(i, null);
            enemy[0]++;
        }
    }
}
public class Problem17135{
    public static void main(String[] args) throws IOException{
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        List<int[]> enemies = new ArrayList<>();
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                if(st.nextToken().equals("1")){
                    int[] position = {i, j};
                    enemies.add(position);
                }
            }
        }

        // 시작
        int max = -1;
        Castle castle = new Castle(enemies, n, m, d);
        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                for(int k = j+1; k < n; k++){
                    castle.setArcher(i, j, k);
                    while(!castle.enemies.isEmpty()){
                        castle.attack();
                        castle.move();
                    }
                }
            }
        }
        System.out.println(castle.attackingCounter);
                    


    }
}
