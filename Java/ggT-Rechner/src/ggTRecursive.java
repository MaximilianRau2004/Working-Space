
public class ggTRecursive {

	public static void main(String[] args) {
         //int result = ggTRecursive(1912, 2148);
         //System.out.println("ggT: " +result);
         System.out.println("Hello");
	}

	public static int ggTRecursive(int a, int b) {
		if (b == 0) {
			return a;
		}
		if (b > a) {
			int r = b%a;
			return ggTRecursive(a, r);
		}
		int r = a%b;
		return ggTRecursive(b, r);
	} 
}
