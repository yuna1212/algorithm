/*
 * 시작 시간: 2022년 11월 12일 12:02 AM
 * 소요 시간: 2시간
 * 풀이 방법: 오버플로!
 */
import java.util.*;
import java.io.*;

class Game{
    int[][] board;
    List<List<List<int[]>>> previouses;

    public Game(int[][] board){
        this.board = board;
        previouses = new ArrayList<>(board.length);
        for(int i = 0; i < board.length; i++)
            previouses.add(new ArrayList<List<int[]>>());
    }

    public void toEnd(int preX, int preY, int x, int y){
        if(x < 0 || x >= board.length || y < 0 || y >= board.length)
            return;
        if(previouses.get(x).isEmpty()){
            toEnd(x, y, x + board[x][y], y);
            toEnd(x, y, x, y + board[x][y]);
        }
        previouses.get(x).get(y).add(new int[]{preX, preY});
    }

    public int toStart(int x, int y){
        int ret = 0;
        if(x == 0 && y == 0)
            return 1;
        for(int[] last: previouses.get(x).get(y))
            ret += toStart(last[0], last[1]);
        return ret;
    }
    
}
public class Problem1890{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];
        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++)
                board[i][j] = Integer.parseInt(st.nextToken());
        }
        Game game = new Game(board);
        game.toEnd(0, 0, 0, 0);
        System.out.println(game.toStart(n-1, n-1));
    }

}
