/*(6) ��д��������ӹ�Ԫ1900�굽2100�������������ţ�ÿ���5����Ż�һ�С�
 * �ж����Ƿ�Ϊ����������ǣ��� ����ſ��Ա�4�����������ܱ�100�������������ꣻ
 * �� ����ſ��Ա�400������Ҳ�����ꡣ
 * */
package test1;


public class sixth {


	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
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
