
public class Modulo {

	public static void main(String[] args) {
		System.out.println(function(true, false, false));
		System.out.println(function2(true, false, false));
		System.out.println(function3(false, true, false));
	}
    public static boolean function(boolean A, boolean B, boolean C) {
    	boolean y = !((!C) || (!A) || B) || ((!A) || C);
    	if (A == B) {
    		if (A == true) {
    		   return B;
    		} else {
    		   return true;
    	    }
    	} else {
    		y = y || (C && (!B));
    	}
    	return y;
    }
    
    public static boolean function2(boolean A, boolean B, boolean C) {
		boolean y = ((A && B) || (!A && !B)) || (B || !A) || C;
    	return y;
    	
    }
    public static boolean function3(boolean A, boolean B, boolean C) {
		boolean y = !A && B && C;
    	return y;
    }
}
