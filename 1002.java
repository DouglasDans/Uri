import java.io.IOException;
import java.util.*;
public class Main {
	public static void main(String[]Args) {
		int i,h,t=1;
		Scanner in =new Scanner(System.in);
		in.useLocale(Locale.ENGLISH);
		double Area, resp;
		Area = in.nextDouble();
		resp = 3.14159 * (Area*Area);
		System.out.printf("A=%.4f/n",resp);
	}
}
