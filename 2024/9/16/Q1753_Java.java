import java.util.*;

public class Main {

    public static int[] dijkstra(ArrayList<ArrayList<int[]>> graph, int N, int s){
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int[] dp = new int[N + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[s] = 0;
        pq.add(new int[]{0, s});
        while (!pq.isEmpty()){
            int[] nc = pq.poll();
            int cost = nc[0], node = nc[1];
            if (dp[node] < cost) continue;
            for(int[] new_nc : graph.get(node)){
                int new_cost = new_nc[1] + cost, new_node = new_nc[0];
                if (dp[new_node] > new_cost){
                    dp[new_node] = new_cost;
                    pq.add(new int[]{new_cost, new_node});
                }
            }
        }
        return dp;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt(), e = sc.nextInt();
        ArrayList<ArrayList<int[]>> graph = new ArrayList<>();
        for (int _v = 0; _v <=v; _v++) graph.add(new ArrayList<>());
        int k = sc.nextInt();
        for (int i = 0 ; i < e; i++){
            int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
            graph.get(a).add(new int[]{b, c});
//            graph.get(b).add(new int[]{a, c});
        }
        int dp[] = dijkstra(graph, v, k);
        sc.close();
        for (int i = 1; i < dp.length; i++){
            if (dp[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(dp[i]);
            }
        }
    }
}