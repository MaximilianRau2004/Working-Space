import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println(isPrime(15));
        int[] array = {5, 2, 9, 1, 5, 6};
        System.out.println(Arrays.toString(bubbleSort(array)));

    }

    public static boolean isPalindrome(String input) {
        if (input == null || input.isEmpty()) {
            return false;
        }
        int begin = 0;
        int end = input.length() - 1;

        while (begin < end) {
            if (input.charAt(begin) != input.charAt(end)) {
                return false;
            }
        begin++;
        end--;
        }
        return true;
    }

    public static boolean isPrime(int number) {
        if (number < 2 ) {
            return false;
        }
        if (number == 2) {
            return true;
        }
        if (number % 2 == 0) {
            return false;
        }

        for (int i = 3; i * i <= number; i+=2) {
            if (number % i == 0) {
                return false;
            }
        }
     return true;
    }

    public static int[] bubbleSort(int[] array) {
        if (array == null || array.length == 0) {
            return array;
        }
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        return array;
    }
}