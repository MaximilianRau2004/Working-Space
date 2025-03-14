
public class DSA {

	public static void main(String[] args) {
		 System.out.println(alg2(20));
	}
  
	public static int alg6 (int n ) {
        int result = 0;
        if ( n > 1) {
		result = alg6(n - 1) + 1;
		} else {
		result = 1;
		}
		for (int i = 0; i < n / 2; i ++) {
		result = result - 1;
		}
		return result;
		}
	
	public static int alg2 (int n ) {
        int p = 1, r = 0;
        for (int i = 1; i<= n; i++) {
		    for (int j = 1; j<=p; j++) {
		    	r++;
		    }
		    p = p*2;
	    }
        return r;
	}
}
