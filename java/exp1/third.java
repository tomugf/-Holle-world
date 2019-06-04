//编写一个程序，求1-100间的素数。
package test1;

public class third {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
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
