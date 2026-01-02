import java.util.*;
public class findGcd {
  public static void main(String args[]){
    int a=9;
    int b=12;
    int result =main(a,b);
    System.out.println("GCD of "+ a + " and " + b + " is: " + result);
  }


public static int main(int a,int b){
  int gcd=1;
  for(int i=1;i<Math.min(a,b);i++){
    if(a%i==0 && b%i==0){
      gcd=i;
    }
  }
  return gcd;
}
}