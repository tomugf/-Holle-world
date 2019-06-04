//输入一段字符串，统计其中有多少个单词。（单词用空格隔开）
package test2;

import java.util.Scanner;

public class three {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		sc.close();
		
		String[] split = str.split(" ");
        System.out.println(split.length);
        
//       方法二		
//      int num = 0;
//		char[] ch = str.toCharArray();
//		
//		for(int i = 0; i < ch.length; i++)
//		{
//			if(ch[i] == ' ')
//				num++;
//		}
//		 System.out.println(num+1);
		 
		
 
	}

}
