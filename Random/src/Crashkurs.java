
import java.util.Scanner;

public class Crashkurs {
    public static void main(String[]args){
        System.out.println("Gebe bitte die erste Zahl ein: ");
        Scanner eingabe1 = new Scanner(System.in);
        int a1 = eingabe1.nextInt();

        System.out.println("Gebe bitte die zweite Zahl ein:");
        Scanner eingabe2 = new Scanner(System.in);
        int b1 = eingabe2.nextInt();

        System.out.println("Eingaben werden nun berechnet: ");
        rechenOperationen((a, b) -> a + b, a1, b1);
        rechenOperationen((a, b) -> a - b, a1, b1);
        rechenOperationen((a, b) -> a * b, a1, b1);
        rechenOperationen((a, b) -> a / b, a1, b1);

    }

    public static void rechenOperationen(Rechner rechner, int zahl1, int zahl2){
        int e = rechner.rechnen(zahl1, zahl2);
        System.out.println(e);
    }
}