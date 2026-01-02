import java.util.*;
public class Armstrong {
  public static void main(String args[]){
    int num = 153;
    if(isArmstrong(num)){
      System.out.println(num + "Armstrong " );
    }
    else{
      System.out.println(num + " Not Armstrong ");
    } 
  }


public static boolean isArmstrong(int n){
  int sum=0;
  int duplicate=n;
  while(n>0){
    int digit=n%10;
    sum=sum+(digit*digit*digit);
    n=n/10;
  }
  return sum==duplicate;
}
}
