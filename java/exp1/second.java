//��ˮ�ɻ�������ָһ��3λ�������λ��ʮλ����λ�ϵ����ֵ������͵��ڸ�����������371=33+73+13�����371��һ��ˮ�ɻ�������д���������е�ˮ�ɻ�����
package test1;
import java.lang.Math;


public class second {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		for(int i = 100; i <= 999; i++)
			if(is_suixian(i))
				System.out.print(i+"  ");

	}
	
	public static boolean is_suixian(int a) {
		int g = a % 10;
		int s = (a/10) % 10;
		int b = (a/100) % 10;
		
		if(Math.pow(g,3)+Math.pow(s, 3)+Math.pow(b, 3) == a)
			return true;
		else
			return false;
			
		
			
		
		
		
	}

}


