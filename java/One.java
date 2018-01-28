/**
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

public class One {
    /*
     * Returns true if n is multiple of 3 or 5.
     */
    static boolean isMultiple(int n) {
        return n % 3 == 0 || n % 5 == 0;
    }

    static int sumMultiplesTo(int n) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (isMultiple(i)) {
                sum += i;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(sumMultiplesTo(1000));
    }
}
