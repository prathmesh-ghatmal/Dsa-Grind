import java.util.Scanner;

public class reverseNo {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a no: ");
    int n= sc.nextInt();
    int result = reverse(n);
    System.out.println("Reversed no : " + result);
  
}

public static int reverse(int n){
  int rev=0;
  while(n>0){
    int digit = n % 10;
    rev = rev * 10 +digit;
    n=n/10;
  }
  return rev;
}
}



