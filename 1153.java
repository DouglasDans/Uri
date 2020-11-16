import java.util.Scanner;
public class Main {
	public static void main(String[]Args) {
		int i,h,t=1;
		Scanner ler=new Scanner(System.in);
		i=1;
		h=ler.nextInt();
		while (i<=h) {
			t=t*i;
			i++;  
		}
			System.out.println(t);
		}
}
