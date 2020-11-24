import java.io.IOException;
import java.util.*;
public class Main {
	public static void main(String[]Args) {
		Scanner in =new Scanner(System.in);
		int a,led,i=0,k;
		a = in.nextInt();
		for (i=0;i<a;i++) {
			led = 0;
			char[] letras = null;
			String palavra = in.next();
			letras = palavra.toCharArray();
			for (k=0;k< letras.length;k++) {
				if (letras[k] == '1'){ led += 2;}
				if (letras[k] == '2'){ led += 5;}
				if (letras[k] == '3'){ led += 5;}
				if (letras[k] == '4'){ led += 4;}
				if (letras[k] == '5'){ led += 5;}
				if (letras[k] == '6'){ led += 6;}
				if (letras[k] == '7'){ led += 3;}
				if (letras[k] == '8'){ led += 7;}
				if (letras[k] == '9'){ led += 6;}
				if (letras[k] == '0'){ led += 6;}
				
			}
			System.out.println(led+" leds");
		}
	}
}

