package algorithm.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj9613 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        long sum;
        for (int i = 0; i < n; i++) {
            sum = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int[] arr = new int[t];
            for (int j = 0; j < t; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < t; j++) {
                for (int k = j+1; k < t; k++) {
                    sum += gcd(arr[j], arr[k]);
                }
            }
            sb.append(sum +"\n");
        }

        System.out.println(sb);
    }
    public static int gcd(int a, int b){
        while(b != 0){
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
