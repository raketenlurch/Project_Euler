public class Multiples {
  public static void main(String[] args) {
    int number = 1000;
    int sum    = 0;

    for (int i=0; i<number; i++) {
      if (i%3 == 0 || i%5 == 0) {
        sum += i;
      }
    }
    System.out.println(sum);
  }
}
