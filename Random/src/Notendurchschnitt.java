
import java.util.Scanner;

public class Notendurchschnitt {

	public static void main(String[] args) {
		
		        double counter = 0;  
		        double sum = 0;  
		        boolean weiter = true;

		        Scanner scan = new Scanner(System.in);

		        System.out.println("Welche Noten hattest du?");
		        System.out.println("Um den Durchschnitt zu errechnen, tippe fertig.");

		        while(weiter) {
		            String eingabe = scan.nextLine();
		            counter++;

		            switch (eingabe) {

		                case "Eins":
		                    sum++;
		                    break;

		                case "Zwei":
		                    sum += 2;
		                    break;

		                case "Drei":
		                    sum += 3;
		                    break;

		                case "Vier":
		                    sum += 4;
		                    break;

		                case "Fünf":
		                    sum += 5;
		                    break;

		                case "Sechs":
		                    sum += 6;
		                    break;

		                case "fertig":
		                    weiter = false;
		                    counter --;
		                    break;

		                default:
		                    counter --;
		                    System.out.println("Da hast Du dich wohl vertippt");
		                    System.out.println("Hast du die Zahlen auch groß geschrieben?");
		            }

		        }

		        double durchschnitt = sum / counter;
		        System.out.println(" Dein Durchschnitt lautet: " + durchschnitt );

    }
}
