import java.util.Scanner;

public class Rechner {

	public static void main(String[] args) {
		 Scanner scanner = new Scanner(System.in);

	        System.out.println("Willkommen zum Taschenrechner!");
	        System.out.print("Geben Sie die erste Zahl ein: ");
	        double operand1 = scanner.nextDouble();
	        
	        System.out.print("Geben Sie den Operator ein (+, -, *, /, %, §, ^): ");
	        char operator = scanner.next().charAt(0);

	        System.out.print("Geben Sie die zweite Zahl ein: ");
	        double operand2 = scanner.nextDouble();

	        double ergebnis = berechne(operand1, operator, operand2);

	        System.out.println("Ergebnis: " + ergebnis);

	        scanner.close();
	}


    public static double berechne (double operand1, char operator, double operand2) {
    	 double ergebnis = 0.0;

         switch (operator) {
             case '+':
                 ergebnis = operand1 + operand2;
                 break;
             case '-':
                 ergebnis = operand1 - operand2;
                 break;
             case '*':
                 ergebnis = operand1 * operand2;
                 break;
             case '/':
                 if (operand2 != 0) {
                     ergebnis = operand1 / operand2;
                 } else {
                     System.out.println("Division durch Null ist nicht erlaubt.");
                 }
                 break;
             case '%':
                 ergebnis = operand1 % operand2;
                 break;
             case '§':
                 ergebnis = Math.sqrt(operand1);
                 break;
             case '^':
                 ergebnis = Math.pow(operand1, operand2);       
                 break;   
             default:
                 System.out.println("Ungültiger Operator.");
         }

         return ergebnis;
    
       }
    }