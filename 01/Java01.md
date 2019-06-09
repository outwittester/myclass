# 				Java

1. Java introduction

  - Java SE -> Standard Edition

  - Java EE -> Enterprise Edition

  - Java ME -> Micro Edition

  - JRE : Runtime Environment 

    - JVM
    - Class Library
    - java

  - JDK : Development Kit

    - JRE
    - javac
    - jdb (java debugger)

  - check bin folder of java

  - bin : bnary executable file

  - source code  -> .java

  - bytecode -> .class

  - JVM -> no .exe but JVM use bytecode to execute, JVM written in C

  - Java is platform independent, but JVM is dependent on OS(operating system)

    - Windows
    - Unix
    - Linux
    - IOS
    - Android  (for smartphone)

  - Download : 8 or above 

    - java -version
    - which java
    - set java environment variable

  - Compile -> javac 

  - run -> java

  - java Calculate

    ```java
    import java.lang.Math;
    public class Calculate{
        public static void main(String[] args){
            for(int i=0;i<5;i++){
                for(int j=0;j<5-i;j++){
                    System.out.print(" ");
                }
                for(int k=0;k<=i;k++){
                    System.out.print("* ");
                }
            System.out.println();
            }
        }
    }
    ```

    

  - Q: What is the difference between java and python?  (static and dynamic)

    - Run Diff.py 

    	```python
    	a = 3
    	print("can still run to here though later throw error %s"%a)
    	print("can still run to here though later throw error %s"+a)
    	```

    	

# Java SE

2. **Comment**

  - single  -> //
  - multiple -> /* */
  - javadoc -> /**  */    [String](<https://docs.oracle.com/javase/7/docs/api/java/lang/String.html>)
  - create a new folder and run any class to try

3. **Naming convention** -> *Good habbit is important*

  - Useful resource for java Development [AlibabaHandBook](<https://github.com/alibaba/p3c/blob/master/%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4Java%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C%EF%BC%88%E8%AF%A6%E5%B0%BD%E7%89%88%EF%BC%89.pdf>)

  - Naming variable: _ letter $ , bestPractice , best_practice 

  - Avoid using $, as inner class will use it as distinction

    - Run InnerTest

    	```java
    	public class InnerTest{
    	    public static void main(String[] args){
    	        class Insider{
    	            int id;
    	            String name;
    	        }
    	    }
    	}
    	```

    	

  - curly braces (choose one and stick to it)

    ```java
    method(){
    
    }
    method()
    {
    
    }
    ```

  - camel or understore (choose one and stick to it)

    - ```java
    	ReverseInteger -> class name first letter in upper case and then camel
    	int myAge;
    	myAge = 29;
    	int myAge = 29;
    	int my_age;
    	```

4. **Data types**

  - primitive data types

  - boolean -> true or false

  - byte -128 ~ 127 2^8 256  

    - 1 byte  = 8 bit   --> often use in IO as byte[]

      1 KB = 1024 Byte 
      1 MB = 1024 KB
      1 GB = 1024 MB

    - Run Range

    	```java
    	public class Range{
    	    public static void main(String[] args){
    	        byte a = 128;
    	        System.out.println(a);
    	    }
    	}
    	```

    	

  - char -> 'a'

  - short -> 16 bits

  - int -> 32 bits

  	```java
  	//write a static function to find the minimum value of an int array,input is array
  	//output is min value
  	```

  	

  - long -> 64 bits  (will be used as id for development)

  - float -> 32 bits

    ```java
    float f = 3.14;
    //imcompatible types, as java use double as default;
    ```

  - double -> 64 bits

    Q: 100 bottles of water, 1 poison , at least how many mice you need to check out? 

    (mouse dies one week later after drinking )

    1      0000001      135 : 1010100 --> 2^6 + 2^4 + 2^2 = 84      
    2      0000010				      n < 2^m  n : bottles , m : mice  --> m > math.log2(100)
    3      0000011      base change formula  
    ...
    100    1100100     

    - Run Mice

    	```java
    	import java.lang.Math;
    	public class Mice{
    	    public static void main(String[] args){
    	        double mouseNumber = Math.log(100)/Math.log(2);
    	        System.out.println(mouseNumber);
    	    }
    	}
    	```

    	

    Q: Why java is strong typed language?

    - Run DefaultValues 

    	```java
    	public class DefaultValues{
    	    int a;
    	    boolean b;
    	    char ch;
    	    byte by;
    	    short sh;
    	    long lo;
    	    float f;
    	    double d;
    	    public static void main(String[] args){
    	        DefaultValues object = new DefaultValues();
    	        System.out.println("default value of int is "+ object.a);
    	        System.out.println("default value of boolean is "+ object.b);
    	        System.out.println("default value of char is "+ object.ch);
    	        System.out.println("default value of byte is "+ object.by);
    	        System.out.println("default value of short is "+ object.sh);
    	        System.out.println("default value of long is "+ object.lo);
    	        System.out.println("default value of float is "+ object.f);
    	        System.out.println("default value of double is "+ object.d);
    	    }
    	}
    	```

    	

5. **Variables**

  - variable in method, method variable must initialize before use
  - variable in class, class variable and instance variable not necessary

6. **Operator**

  - +
  - -
  - *
  - /
  - %

    - Run ReverseInteger

    	```java
    	public class ReverseInteger {
    	    public static void main(String[] args) {
    	        System.out.println(Integer.MAX_VALUE);
    	        System.out.println(Integer.MIN_VALUE);
    	        System.out.println(reverseInt(1234567892));
    	        System.out.println(reverseInt(1234567891));
    	    }
    	
    	    private static int reverseInt(int x) {
    	        int currentDigit;
    	        long result = 0;
    	        while (x != 0) {
    	            currentDigit = x % 10;
    	            result = result * 10 + currentDigit;
    	            x /= 10;
    	        }
    	        if(result > 2147483647 || result < -2147483648){
    	            return 0;
    	        } else {
    	            return (int) result;
    	        }
    	    }
    	}
    	```

  - &&
  - ||
  - &
  - |

    - Run Logic 

    	```java
    	public class Logic{
    	    public static void main(String[] args){
    	        int a = 1;
    	        int b = 2;
    	        int c = 3;
    	        int d = 4;
    	        int e = 5;
    	
    	        boolean bool = (a<b)&&((e=c)<d);
    	        System.out.println(bool);
    	        System.out.println(e); 
    	    }
    	}
    	```

    	

7. **flow control**

  - ternary ->    () ? x:y    —> true return x false return y

    - Run Ternary

    	```java
    	public class Ternary{
    	    public static void main(String[] args) {
    	        int a = 5;
    	        String result = (a > 10)? "Yes":"No";
    	        System.out.println(result);
    	    }
    	}
    	```

    	

  - if (boolean expression){

    ​	statements;

    }else if(boolean expression){

    ​	statements;

    }else{

    ​	statements;

    }

    - GuessBirthDay

    	```java
    	public class Player {
    	    public static void main(String[] args) {
    	        String set1 = " 1  3  5  7\n 9 11 13 15\n17 19 21 23\n25 27 29 31";
    	        String set2 =" 2  3  6  7\n10 11 14 15\n18 19 22 23\n26 27 30 31";
    	        String set3="  4  5  6  7\n12 13 14 15\n20 21 22 23\n28 29 30 31";
    	        String set4=" 8  9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31";
    	        String set5="16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31";
    	
    	        int day = 0;
    	
    	        @SuppressWarnings("resource")
    	        Scanner scan = new Scanner(System.in);
    	
    	        System.out.print("Is your birthday in set1?\n");
    	        System.out.print(set1);
    	        System.out.print("\nEnter 0 for No and 1 for Yes: ");
    	        int answer = scan.nextInt();
    	        if(answer==1)
    	            day+=1;
    	
    	        System.out.print("\nIs your birthday in set2?\n");
    	        System.out.print(set2);
    	        System.out.print("\nEnter 0 for No and 1 for Yes: ");
    	        answer = scan.nextInt();
    	        if(answer==1)
    	            day+=2;
    	
    	        System.out.print("\nIs your birthday in set3?\n");
    	        System.out.print(set3);
    	        System.out.print("\nEnter 0 for No and 1 for Yes: ");
    	        answer = scan.nextInt();
    	        if(answer==1)
    	            day+=4;
    	
    	        System.out.print("\nIs your birthday in set4?\n");
    	        System.out.print(set4);
    	        System.out.print("\nEnter 0 for No and 1 for Yes: ");
    	        answer = scan.nextInt();
    	        if(answer==1)
    	            day+=8;
    	
    	        System.out.print("\nIs your birthday in set5?\n");
    	        System.out.print(set5);
    	        System.out.print("\nEnter 0 for No and 1 for Yes: ");
    	        answer = scan.nextInt();
    	        if(answer==1)
    	            day+=16;
    	        System.out.println("\nYour birthday is "+day+" !");
    	
    	    }
    	}
    	```

    	

    - Run Palindrome

    	```java
    	public class Palindrome {
    	    public static void main(String[] args) {
    	        System.out.println(isPalindrome(1221221));
    	    }
    	
    	
    	    private static boolean isPalindrome(int x) {
    	        if (x < 0) {
    	            return false;
    	        } else if (x > 0 && x < 10) {
    	            return true;
    	        } else {
    	            StringBuilder sx = new StringBuilder(String.valueOf(x));
    	            for (int i = 0; i < sx.length() / 2; i++) {
    	                if (!(sx.charAt(i) == sx.charAt(sx.length() - 1 - i))) {
    	                   return false;
    	                }
    	            }
    	        }
    	        return true;
    	    }
    	}
    	```

    	

  - 

  - switch (!!! careful with break key word)

    - break and continue 

    	> break : jump out the whole loop 
    	>
    	> continue : jump out current circle

    Q: what are the types can be used as switch cases?

     	[officialAnswer](<https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html>)

    - Run Switch

    	```java
    	public class Switch{
    	    public static void main(String[] args) {
    	        int day = 7;
    	        String dayString;
    	     switch (day) {
    	        case 1:
    	            dayString = "Monday";
    	            break;
    	        case 2:
    	            dayString = "Tuesday";
    	            break;
    	        case 3:
    	            dayString = "Wednesday";
    	            break;
    	        case 4:
    	            dayString = "Thursday";
    	            break;
    	        case 5:
    	            dayString = "Friday";
    	            break;
    	        case 6:
    	            dayString = "Saturday";
    	            break;
    	        case 7:
    	            dayString = "Sunday";
    	            break;
    	        default:
    	            dayString = "Invalid day";
    	            break;
    	        }
    	        System.out.println(dayString);
    	    }
    	}
    	```

    	

  - while(boolean expression){

    ​	statements;

    }

    - Run While

    	```java
    	public class While {
    	        public static void main(String[] args) throws InterruptedException {
    	            int counter = 100;
    	            while(counter > 0){
    	                counter--;
    	                Thread.sleep(100);
    	                System.out.println(counter);
    	            }
    	            if(counter==0){
    	                System.out.println("You are fired");
    	            }
    	        }
    	}
    	```

    	

  - do{

    ​	statements; // inside of do will run at least one time

    }while(boolean expression)

  - for(initialization; judgement; step forward){

    ​	statements;

    }

    - run initialization
    - check judgement, false -> get out of loop, true -> run statements inside;
    - run step forward
    - recheck judgement to the end

      - Run Divisors

      	```java
      	public class Divisors {
      	    public static void main(String[] args) {
      	        getDivisors(68834021);
      	    }
      	    private static void getDivisors(int input) {
      	        for(int i=1;i<=input;i++){
      	            if (input%i==0){
      	                System.out.println(i);
      	            }
      	        }
      	    }
      	}
      	```

      	

  

