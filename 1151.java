import java.util.*;
import java.io.IOException;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int p = 0,i = 0,k,a = 0,ant = 0;
		Scanner ler=new Scanner(System.in);
		k=ler.nextInt(); 
		ant=0;
		p=1;
		while(i < k){
			if (i == 1) ant = 0;
			if (i >= k - 1) {
				System.out.print(a+"\n");
			}else {
				System.out.print(a+" ");
			}
			
			a=ant+p;
			ant=p;
			p=a;
			i++;
		}
}
}