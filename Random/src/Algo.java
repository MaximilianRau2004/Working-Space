
public class Algo {

	public static void main(String[] args) {

		System.out.println(f12(1000000000));
	}

	public static int f1(int n) {
		int sum = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				sum++;
			}
			
		}
		return sum;
	}
	
	public static int f2(int n) {
		int sum = 0;
		for (int i=0; i<n; i++) {
			for (int j=i; j<n; j++) {
				sum++;
			}
			
		}
		return sum;
	}
	
	public static int f3(int n) {
		int sum = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<=i; j++) {
				sum++;
			}
			
		}
		return sum;
	}
	
	public static int f6(int n) {
		int sum2 =0;
		int sum = 0;
		for(int i=1; i<n; i++) {
			sum = sum + f6(n-1);
			sum2++;
		}
		return sum2;
	}
	public static int f12(double d) {
		if (d>=4) {
			return f12(Math.sqrt(d));	
			
		} else {
			return 1;
		}
	}
	
}
