/*(6) 编写程序，输出从公元1900年到2100年所有闰年的年号，每输出5个年号换一行。
 * 判断年是否为闰年的条件是：① 若年号可以被4整除，而不能被100整除，则是闰年；
 * ② 若年号可以被400整除，也是闰年。
 * */
package test1;


public class sixth {


	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		int temp = 0;
		
		for(int i = 1900; i <= 2100; i++)
		{
			if((i%4 == 0 && i%100 != 0) || (i%400 == 0))
			{
				temp++;
				System.out.print((temp < 5) ? i+" " : i);
				
			}
			if(temp == 5)
			{
				System.out.println("");
				temp = 0;
			}
				
				
		}

	}

}
