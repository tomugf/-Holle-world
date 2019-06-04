//编写一个程序，在控制台输入10个数，按大小顺序输出。
package test2;

public class one {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		float[] numbers = new float[10];
		for(int i = 0; i < 10; i++)
			numbers[i] = Float.parseFloat(args[i]);
		ssort(numbers);
		for (int i = 0; i < numbers.length; i++) {
			System.out.print((i < numbers.length-1) ? i+" " : i+"\n");
			
		}
			

	}
	
	public static void ssort(float[] numbers)
	{
		float temp; // 记录临时中间值   
		int size = numbers.length; // 数组大小   
		for (int i = 0; i < size - 1; i++) {   
		     for (int j = i + 1; j < size; j++) {   
		          if (numbers[i] > numbers[j]) { // 交换两数的位置   
		                 temp = numbers[i];   
		                 numbers[i] = numbers[j];   
		                 numbers[j] = temp;   
		           }   
		      }   
		 }   
	}

}
