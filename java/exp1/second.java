//“水仙花数”是指一个3位数，其个位、十位、百位上的数字的立方和等于该数本身，例如371=33+73+13，因此371是一个水仙花数。编写程序，求所有的水仙花数。
package test1;
import java.lang.Math;


public class second {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
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


