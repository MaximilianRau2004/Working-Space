
import java.awt.Point;
import java.util.Scanner;

public class Game {

	public static void main(String[] args) {
		Point playerPosition = new Point(10,9);
        Point snakePosition = new Point(15,5);
        Point goldPosition = new Point(6,6);
        Point doorPosition = new Point(2,5);
        boolean continu = true;
        boolean goldCollected = false;
        
       while (continu) {
	   for (int i = 0; i<10; i++) {
		   for (int j = 0; j<40; j++) {
			   Point p = new Point(j, i);
			   if (p.equals(playerPosition)) {
				   System.out.print("P");
			   } else if (p.equals(snakePosition)) {
				   System.out.print("S");
			   } else if (p.equals(goldPosition)) {
				   System.out.print("G");
			   } else if (p.equals(doorPosition)) {
				   System.out.print("D");
			   } else {
			   System.out.print(".");
			   }
		   }  
	       System.out.println();
	   }
	   
	   if (snakePosition.equals(playerPosition)) {
		   continu = false;
		   System.out.println("The snake got ya");
	       playerPosition = new Point(-1,-2);
	   }
	    
	   if (goldPosition.equals(playerPosition)) {
		   goldCollected = true;
		   goldPosition = new Point(-1, -1);
	   }
	    
	   if (playerPosition.equals(doorPosition) && goldCollected) {
		   continu = false;
		   System.out.println("Victory Royale");
	   }
	
	   movePlayer(playerPosition);
       moveSnake(snakePosition, playerPosition);
       
	   }
	}
	private static void moveSnake(Point snakePosition, Point playerPosition) {
		if (playerPosition.x < snakePosition.x)
			snakePosition.x--;
		else if (playerPosition.x > snakePosition.x)
			snakePosition.x++;
		if (playerPosition.y < snakePosition.y)
			snakePosition.y--;
		else if (playerPosition.y > snakePosition.y)
			snakePosition.y++;
	}
	private static void movePlayer(Point playerPosition) {
		Scanner scan = new Scanner(System.in);
		String input = scan.next();
	
	    if (input.equals("w")) {
	    	if(playerPosition.y > 0) 
	    		playerPosition.y--;
	    	} else if (input.equals("s")) {
	    	     if (playerPosition.y < 9) 
	    		    playerPosition.y++;
	    	} else if (input.equals("d")) {
	             if (playerPosition.x < 39) 
	    			playerPosition.x++;
	        } else if (input.equals("a")) {
	    	     if (playerPosition.x > 0) 
	    			 playerPosition.x--;		  
	   
	    }
	}

}
