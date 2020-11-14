import java.util.Scanner;
public class Main {
	public static void main (String[] Args) {
		int a,b,c,d,e;
		Scanner in = new Scanner (System.in);
		a=in.nextInt();
		b=in.nextInt();
		c=in.nextInt();
		d=in.nextInt();
		e=a * b - c * d;
		System.out.println("DIFERENCA = "+e);
	}
}
