//��һ��3*3����Խ�Ԫ��֮�͡�
package test2;

import java.util.Scanner;

public class two {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
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
