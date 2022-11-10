/*
 * 시작 시간: 2022년 11월 10일 7:54 PM
 * 소요 시간: 1시간 20분
 * 풀이 방법: 초기화에 주의
 */
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

class Range implements Comparable<Range>{
    public int start;
    public int end;
    public Range(int start, int end){
        this.start = start;
        this.end = end;
    }
    @Override
    public int compareTo(Range range){
        if(this.start < range.start)
            return -1;
        else if(this.start == range.start)
            return 0;
        else
            return 1;
    }
}


class Solution{
    int end;
    int plankLength;
    int plankCounter;

    public Solution(int start, int end, int plankLength){
        plankCounter = (int) Math.ceil((double) (end - start)/plankLength);
        this.plankLength = plankLength;
        this.end = start + plankCounter*plankLength;
    }

    public void cover(int nextStart, int nextEnd){
        int extraPlank;
        if(nextStart <= end){
            extraPlank = (int) Math.ceil((double) (nextEnd - end) / plankLength);
            end += extraPlank*plankLength;
        }
        else{
            extraPlank = (int) Math.ceil((double) (nextEnd - nextStart) / plankLength);
            end = nextStart + extraPlank*plankLength;
        }
        plankCounter += extraPlank;
    }
}


public class Problem1911{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n, l;
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        PriorityQueue<Range> heap = new PriorityQueue<>();
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            heap.add(new Range(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        Range range;
        Solution solution = new Solution(heap.peek().start, heap.peek().end, l);
        for (int i = 0; i < n; i++){
            range = heap.poll();
            solution.cover(range.start, range.end);
        }
        System.out.println(solution.plankCounter);
    }
}
