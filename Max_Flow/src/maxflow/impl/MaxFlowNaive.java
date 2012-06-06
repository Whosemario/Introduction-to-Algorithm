package maxflow.impl;

import java.util.Arrays;

/*
 * 算法导论第26章，利用求最短路的方式求增广路径的Edmonds-Karp算法
 */
public class MaxFlowNaive {
	
	private int[][] mat;
	private int[][] flow;
	private int n;
	private int source, sink;
	
	private int[] pre;
	private int[] dist;
	private int[] queue;
	private int head,tail;
	
	private final static int INF = 1000000000;
	
	public MaxFlowNaive(int[][] mat,int n,int source,int sink){
		this.mat = mat;
		this.n = n;
		this.source = source;
		this.sink = sink;
		flow = new int[n][n];
	}
	
	public int process(){
		int ret = 0;
		pre = new int[n];
		dist = new int[n];
		queue = new int[n+2];
//		Arrays.fill(flow, 0);
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				flow[i][j] = 0;
        while(true){
        	Arrays.fill(pre, -1);
        	dist[source] = INF;
        	head = tail = 0;
        	queue[tail++] = source;
        	while(head < tail){
        		int t = queue[head++];
        		int j;
        		for(int i=0;i<n;i++)
        			if(pre[i]==-1&&(j=mat[t][i]-flow[t][i])!=0){
        				pre[i] = t;
        				queue[tail++] = i;
        				dist[i] = dist[t] < j ? dist[t]:j;
        			}
        	}
        	if(pre[sink] == -1) break;
        	int t=sink;
        	while(t!=source){
        		int p = pre[t];
        		flow[p][t] += dist[sink];
        		flow[t][p] = - flow[p][t];
        		t=p;
        	}
        }
        for(int i=0;i<n;i++)
        	if(flow[source][i]>0)
        		ret += flow[source][i];
		return ret;
	}

}
