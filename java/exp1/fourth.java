/*��һ������
 *     x        ��x<1��
 *	Y= 3x-2      ��1��x<10��
 *     4x        ��x��10��
 *    дһ���򣬸���xֵ�����yֵ��
 * 
 * */
package test1;

import java.util.Scanner;

public class fourth {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		Scanner sc = new Scanner(System.in);
		
		while(true)
		{
			float x = sc.nextFloat();
			if(x < 1)
				System.out.println(x);
			if(x >= 1 && x < 10)
				System.out.println(3*x -2);
			if(x >= 10)
				System.out.println(4*x);
					
		}
//		sc.close();

	}

}
