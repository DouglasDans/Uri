import java.io.IOException;
import java.util.*;
public class Main {
	public static void main(String[]Args) {
		Scanner in =new Scanner(System.in);
		double n1, n2, n3, resp;
		String num1,num[] = new String[2];
		n1 = in.nextDouble();
		n2 = in.nextDouble();
		n3 = in.nextDouble();
		resp = ((n1 * 2) + (n2 * 3) + (n3 * 5))  / 10;
		System.out.printf("MEDIA = %.1f" , resp);
		System.out.println();
	}
}

