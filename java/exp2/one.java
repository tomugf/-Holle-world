//��дһ�������ڿ���̨����10����������С˳�������
package test2;

public class one {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
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
		float temp; // ��¼��ʱ�м�ֵ   
		int size = numbers.length; // �����С   
		for (int i = 0; i < size - 1; i++) {   
		     for (int j = i + 1; j < size; j++) {   
		          if (numbers[i] > numbers[j]) { // ����������λ��   
		                 temp = numbers[i];   
		                 numbers[i] = numbers[j];   
		                 numbers[j] = temp;   
		           }   
		      }   
		 }   
	}

}
