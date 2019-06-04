//求一个3*3矩阵对角元素之和。
package test2;

import java.util.Scanner;

public class two {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		float[][] su = new float[3][3];
		Scanner sc = new Scanner(System.in);
		
		
		for(int i = 0; i < 3; i++)
			for(int j = 0; j < 3; j++)
			{
				float aa = sc.nextFloat();
				su[i][j] = aa;
			}
				
		System.out.println(su[0][0]*su[2][2]);
			
		sc.close();
		

	}

}
