//��дһ��������1-100���������
package test1;

public class third {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		for(int i = 2; i < 100; i++)
			if(is_su(i))
				System.out.print(i+" ");

	}
	
public static boolean is_su(int a) {
	
	for(int i = 2; i < a/2 + 1; i++)
		if(a % i == 0)
			return false;
	return true;
}


}
