package maxflow.test;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

import maxflow.impl.MaxFlowNaive;

public class MainTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			System.setIn(new BufferedInputStream(new FileInputStream("data.in")));
			Scanner cin = new Scanner(System.in);
			int n,m;
			int[][] mat;
			n = cin.nextInt();
			m = cin.nextInt();
			mat = new int[n][n];
//			Arrays.fill(mat, 0);
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
					mat[i][j] = 0;
			for(int i=0;i<m;i++){
				int s,e,c;
				s = cin.nextInt();
				e = cin.nextInt();
				c = cin.nextInt();
				mat[s][e] = c;
				
			}
			MaxFlowNaive maxFlow = new MaxFlowNaive(mat, n, 0, n-1);
			System.out.println(maxFlow.process());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
