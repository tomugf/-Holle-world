package test1;

public class fifth {
	final static int STOREY = 4;

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		for(int i = 0; i < STOREY; i++)
		{
			for(int j = i; j < STOREY-1; j++ )
				System.out.print("   ");
			for(int j = 0; j < 2*i+1; j++ )
				System.out.print("☆");
			System.out.println("");
			
		}
		for(int i = STOREY-2; i >= 0; i--)
		{
			for(int j = i; j <= STOREY-1; j++ )
				System.out.print("  ");
			for(int j = 0; j < 2*i+1; j++ )
				System.out.print("☆");
			System.out.println("");
			
		}
			
			
	}

}
