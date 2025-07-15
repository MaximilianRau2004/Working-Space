import java.util.LinkedList;

public class NEA {
     // SCAN trennt Zustände für aktuelles Zeichen von denen fürs nächste
	 static final int SCAN = -1;
	 static final int F = -1; // Endzustand
	 
	 static class State { // Repräsentation der Zustände
		 char symbol;     // zu akzeptierendes Symbol
		 int next1, next2;  // Nachfolgezustände 
		 public State(char s,int n1, int n2) {
			 symbol = s; next1 =n1; next2 = n2;
		 }
	 }
	 
	 // NEA
     State[] states = {
        new State ('\0', 1, 3), new State ('A', 1, 3),
        new State ('\0', 3, 1),  new State ('B', 4, 4),
        new State ('A', 5, 5),  new State ('\0', F, F)
     };
     
     public boolean match(String s) {
    	 LinkedList<Integer> deque = new LinkedList<Integer>();
    	 int j = 0; 
    	 int state = 0; 
    	 deque.addLast(SCAN);
    	 while (j <= s.length()) {
    		 if (state == F) {
    			 if (j == s.length()) // Wort zuende gelesen
    				 return true;
    		 } else if(state == SCAN) {
    			 j++;
    			 deque.addLast(SCAN);
    		 } else if (states[state].symbol == '\0') { // leeres Zeichen/epsilon
    			 deque.addFirst(states[state].next1); // Einfügen am Anfang
    			 if (states[state].next1 != states[state].next2)
    				 deque.addFirst(states[state].next2);
    		 } else if (j < s.length() && states[state].symbol == s.charAt(j)) {
    			 // Zeichen akzeptiert
    			 deque.addLast(states[state].next1); // Einfügen am Ende
    		 }
    	     // in neuen Zustand übergehen
    		 state = deque.removeFirst();
    	 }
     return false;
     }

     public static void main(String[] args) {
    	 
     }
}
