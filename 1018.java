import java.util.*;
import java.io.IOException;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		in.useLocale(Locale.ENGLISH);
		int num ,i, notas100;
		num = in.nextInt();
		System.out.println(num);
		
		for (i = 0; num >= 100; i++) {
			num -= 100;
		}
		System.out.println(i+" nota(s) de R$ 100,00");
		
		for (i = 0; num >= 50; i++) {
			num -= 50;
		}
		System.out.println(i+" nota(s) de R$ 50,00");
		
		for (i = 0; num >= 20; i++) {
			num -= 20;
		}
		System.out.println(i+" nota(s) de R$ 20,00");
		
		for (i = 0; num >= 10; i++) {
			num -= 10;
		}
		System.out.println(i+" nota(s) de R$ 10,00");
		
		for (i = 0; num >= 5; i++) {
			num -= 5;
		}
		System.out.println(i+" nota(s) de R$ 5,00");
		
		for (i = 0; num >= 2; i++) {
			num -= 2;
		}
		System.out.println(i+" nota(s) de R$ 2,00");
		
		for (i = 0; num >= 1; i++) {
			num -= 1;
		}
		System.out.println(i+" nota(s) de R$ 1,00");
	}

}
