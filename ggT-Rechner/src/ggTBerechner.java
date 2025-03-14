
public class ggTBerechner {

	public static void main(String[] args) {
		int x = 1912;
		int y = 2000;
		int max, min, rest;
		if (x>y) {
			max = x;
			min = y;
		}else {
	        max = y;
	        min = x;
		} 
		rest = max%min;
		while (rest>0) {
	           max = min;
	           min = rest;
	           rest = max%min;
		} 
	   
	System.out.println("Der ggT von " + x + " und " + y + " ist " + min );
		
	}

}
