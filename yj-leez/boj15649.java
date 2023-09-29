package algorithm.bruteforce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj15649 {
    public static int[] arr;
    public static boolean[] contain;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[m];
        contain = new boolean[n];
        dfs(n, m, 0);
        System.out.println(sb);

    }

    public static void dfs(int n, int m, int depth) {
        if(depth == m){
            for (int i: arr) {
                sb.append(i).append(' ');
            }
            sb.append('\n');
            return;
        }
        for (int i = 0; i < n; i++) {
            if(contain[i] != true){
                contain[i] = true;
                arr[depth] = i + 1;
                dfs(n, m , depth + 1);
                contain[i] = false;
            }
        }
    }
}
