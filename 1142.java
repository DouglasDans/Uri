import java.io.IOException;
import java.util.*;
public class Main {
	public static void main(String[]Args) {
		Scanner in =new Scanner(System.in);
		int contador, i,j=1, t=0;
		contador = in.nextInt();
		for (i = 1;t < contador; i++ ) {
			System.out.print(i+" ");
			if (j == 3) {
				System.out.print("PUM\n");
				t++;
				j = 0;
				i++;
			}
			j++;
		}
	}
}
