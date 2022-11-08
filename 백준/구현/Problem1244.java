/*
 * 시작 시간: 2022년 11월 8일 4:56 PM
 * 소요 시간: 1시간 15분
 * 풀이 방법: 간단한 구현
 */
import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
class Switch{
    public int[] switches;
    public Switch(int[] switches){
        this.switches = switches;
    }

    public void switch_multiple(int number){
        for(int i = 1; i*number < switches.length; i++){
            switches[i*number] ^= 1;
        }

    }

    public void switch_symmetry(int middle){
        int left = middle; int right = middle;
        switches[middle] ^= 1; // 반복문에서 두번 반전되므로 미리 한번 반전
        while(left > 0 && right < switches.length){
            if(switches[left] != switches[right]) break;
            switches[left] ^= 1;
            switches[right] ^= 1;
            left--; right++;
        }
    }
}



public class Problem1244 {
    public static void main(String[] args) throws IOException{
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(br.readLine())+1;
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] switches = new int[size];
        for(int i = 1; i < size; i++){
            switches[i] = Integer.parseInt(st.nextToken());
        }
        Switch studentSwitch = new Switch(switches);

        size = Integer.parseInt(br.readLine());
        for(int i = 0; i < size; i++){
            st = new StringTokenizer(br.readLine());
            if(st.nextToken().equals("1"))
                // 남학생
                studentSwitch.switch_multiple(Integer.parseInt(st.nextToken()));
            else
                studentSwitch.switch_symmetry(Integer.parseInt(st.nextToken()));
        }

        // 출력
        for(int i = 1; i < studentSwitch.switches.length; i++){
            System.out.print(studentSwitch.switches[i]+" ");
            if(i%20 == 0)
                System.out.println();
        }
    }
}
