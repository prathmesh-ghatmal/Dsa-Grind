import java.util.*;
public class palindrome {
  public static void main(String args[]){
   int number=122;
   palindrome obj = new palindrome();
   if(obj.isPalindrome(number)){
    System.out.println(number + " is a palindrome");
   }
   else{
    System.out.println(number + " is not a palindrome");
   }
   
}


public static boolean isPalindrome(int n){
  int rev = 0;
  int duplicate = n;
  while(n>0){
    int digit = n%10;
    rev = rev*10+digit;
    n=n/10;
  }
  return rev==duplicate;
}
}
