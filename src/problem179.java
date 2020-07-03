public class problem179 {
    public static void main(String[] args) {
        int curr = numDivisors(2);
        int next = numDivisors(3);
        int total = 0;
        for (int i = 2; i < 10000000; i++) {
            next = numDivisors(i + 1);
            if (curr == next) {
                total++;
            }
            curr = next;
        }
        System.out.println(total);
    }

    public static int numDivisors(int number) {
        int total = 0;
        int limit = (int) Math.sqrt(number);
        for (int i = 1; i <= limit; i++) {
            if (number % i == 0) {
                total++;
                if (i != (int)(number / i)) {
                    total++;
                }
            }
        }
        return total;
    }
}