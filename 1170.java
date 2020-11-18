import java.io.IOException;
import java.util.*;
public class Main {
	public static void main(String[]Args) {
		Scanner in =new Scanner(System.in);
		int a, dias;
		double n;
		a = in.nextInt();
		for(int i=0;i < a;i++) {
			dias = 0;
			n = in.nextDouble();
			while (n > 1) {
				dias++;
				n = n * 0.5;
			}
			System.out.println(dias+" dias");
		}
	}
}

