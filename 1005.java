import java.io.IOException;
import java.util.*;
public class Main {
	public static void main(String[]Args) {
		Scanner in =new Scanner(System.in);
		double n1, n2, resp;
		String num1,num[] = new String[2];
		n1 = in.nextDouble();
		n2 = in.nextDouble();
		
		resp = ((n1 * 3.5) + (n2 * 7.5)) / 11;
		
		System.out.printf("MEDIA = %.5f" , resp);
		System.out.println();
	}
}

