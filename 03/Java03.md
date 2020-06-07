# Java SE

1. **package**

  ```java
  java
  		   com
  		     companyname
  		        package1
  		        package2
  		        ....
  import key word
  javac -d . Player.java  (change the package to see difference)
  ```

  > package won't affect compile(javac) but affect run(java) (disk should know the directory hierarchy)
  >
  > If you don't define package, default package is provided (Eclipse)
  >
  > package should be all in lower case

2. **Object** Class  java.lang.Object  (9 methods in total 2 overloads)

  > Ancestor of All

  - API (Application Programming Interface)

  	Check the Library inside of any java project

  - start with ==

  	1. primitive data type -> check literal values are equal
  	2. refercence data type -> check object memory address are the same (the same object)

  - Every class has Object as it's superclass, so whatever methods Object has, it's subclasses have too

  ```java
  Object obj = new Object();
  System.out.println(obj);  
  System.out.println(obj.toString());
  // -- when print the reference is calling the toString() as default
  
  public class Player {
      public static void main(String[] args) {
          Object obj = new Object();
          System.out.println(obj);
          System.out.println(obj.toString());
          System.out.println(obj.getClass().getName()+"@"+Integer.toHexString(obj.hashCode()));
     // understand hex to decimal and binary to decimal 
          String s = "anyString";
          System.out.println(s);
          System.out.println(s.toString());
  
          SevenYearsDeveloper sevenYearsDeveloper = new SevenYearsDeveloper();
          System.out.println(sevenYearsDeveloper);
          System.out.println(sevenYearsDeveloper.toString());
      }
  
  }
  
  class SevenYearsDeveloper{
  
      @Override
      public String toString() {
          return "I'm going have seven years experience after the training";
      }
  }
  ```

3. **String** class

  ```java
  public class Player {
      public static void main(String[] args) {
          Object obj1 = new Object();
          Object obj2 = new Object();
          System.out.println(obj1 == obj2);
          System.out.println("==============");
          String s1 = new String("I love java");
          String s2 = new String("I love java");
          System.out.println(s1 == s2);
          System.out.println("--------------");
          String s3 = "She loves java too";
          String s4 = "She loves java too";
          System.out.println(s3 == s4);
          System.out.println(",,,,,,,,,,,,,,");
          String s6 = new String("You");
          String s5 = "You";
          System.out.println(s5 == s6);
          System.out.println("..............");
          String s = "Hello World";
          String h = "Hello ";
          String w = "World";
          System.out.println(s == h + w);
          System.out.println("??????????????");
          System.out.println(s == "Hello " + "World");
      }
  
  }
  ```

  - equals method in Object 

    - check source code (remember the origin of equals method is comparing address)

      ```java
      public class Player {
          public static void main(String[] args) {
              String s1 = new String("java");
              String s2 = new String("java");
              System.out.println(s1.equals(s2));
              String s3 = "java";
              String s4 = "java";
              System.out.println(s3.equals(s4));
              System.out.println("????????????????");
              Object obj1 = new Object();
              Object obj2 = new Object();
              System.out.println(obj1.equals(obj2));
              System.out.println(obj1 == obj2);
              System.out.println("----------------");
              System.out.println(s1 == s2);
              System.out.println(s3 == s4);
              System.out.println(s1 == s3);
          }
      
      }
      
      //String equals is comparing the content the same or not
      //When compare String use equals not ==
      ```

      ```java
      public class Player {
          public static void main(String[] args) {
              SevenYearsDeveloper s1 = new SevenYearsDeveloper("Kyle");
              SevenYearsDeveloper s2 = new SevenYearsDeveloper("Kyle");
              System.out.println(s1 == s2);
              System.out.println(s1.equals(s2));
          }
      
      }
      
      class SevenYearsDeveloper {
          String name;
      
          public SevenYearsDeveloper(String name) {
              this.name = name;
          }
      }
      ```

      - rewrite equals method

      ```java
      public class Player {
          public static void main(String[] args) {
              SevenYearsDeveloper s1 = new SevenYearsDeveloper("Kyle");
              SevenYearsDeveloper s2 = new SevenYearsDeveloper("Kyle");
              System.out.println(s1 == s2);
              System.out.println(s1.equals(s2));
          }
      
      }
      
      class SevenYearsDeveloper {
          String name;
      
          public SevenYearsDeveloper(String name) {
              this.name = name;
          }
      
          @Override
          public boolean equals(Object obj) {
              if(this == obj){
                  return true;
              }
              if(obj instanceof SevenYearsDeveloper){
                  SevenYearsDeveloper sevenYearsDeveloper = (SevenYearsDeveloper) obj;
                  if (sevenYearsDeveloper.name.equals(this.name)) {
                      return true;
                  }
              }
              return false;
          }
      }
      ```

      - String is constant, once it's object is created which becomes immutable
      - Java String pool, literal assignment ("literal")

      ```java
      public class Player {
          public static void main(String[] args) {
              String s1 = "Hello";
              String s2 = "Hello";
              System.out.println(s1 == s2);
         
          		    String s1 = new String("Hello");
              String s2 = new String("Hello");
              System.out.println(s1 == s2);
          }
      
      }
      ```

      - new create object in heap 
      - java pool in stack

      ```java
      public class Player {
          public static void main(String[] args) {
              String s1 = new String("Hello");
              String s2 = "Hello";
              System.out.println(s1 == s2);
          }
      
      }
      ```

      - "+" is generating new Object not original String content
      - Here is why you can't simply use == to compare String but use equals method

      ```java
      public class Player {
          public static void main(String[] args) {
              String s = "hello";
              String s1 = "hel";
              String s2 = "lo";
              System.out.println(s == s1 + s2);
          }
      
      }
      
      ```

      - Any class if not override equals  is comparing address (==)
      - == is comparing if they are the same object

      - Rewrite String equals method

      ```java
      public class StringClassAnalysis {
          public static void main(String[] args) {
              char[] v1 = {'a', 'b', 'c'};
              char[] v2 = {'a', 'b', 'c'};
              for (int i = 0; i < v1.length; i++) {
                  if (v1[i] == v2[i]) {
                      System.out.println("v1[" + i + "]=" + "v2[" + i + "]");
                  } else {
                      System.out.println("v1[" + i + "]!=" + "v2[" + i + "]");
                  }
              }
      
              //equals methods core algorithm
      
               int n = v1.length;
              int i = 0;
              while (n-- != 0) {
                  System.out.println(n);
                  if (v1[i] != v2[i]) {
                      System.out.println("not equal");
                  } else {
                      System.out.println("equal");
                  }
                  i++;
              }
      
          }
      }
      ```

      homework 234

4. **StringBuffer** and **StringBuilder**

  - StringBuffer an StringBuilder are **mutable**, you can add string on original string while not create a new object

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        StringBuffer buffer = new StringBuffer();
  	        StringBuffer buffer1 = buffer.append("hello").append("world").append(1).append(true);
  	
  	        String rel = buffer.toString();
  	        System.out.println(rel);
  	        System.out.println(buffer == buffer1);
  	
  	        StringBuilder builder = new StringBuilder();
  	        StringBuilder builder1 = builder.append("hello").append("world").append(1).append(true);
  	        String rel1 = builder.toString();
  	        System.out.println(rel1);
  	        System.out.println(builder == builder1);
  	    }
  	
  	}
  	
  	```

  - **ThreadSafe** and not ThreadSafe   —> check Thread

5. **Wrapper** Classes —> for primitive data types —> when need reference type —> makes it more oop

  - put the value into an object then use the reference 

  ```java
  public class Player {
      public static void main(String[] args) {
          int age = 29;
          Integer ageOjb = new Integer(age);
          int ageIntValue = ageOjb.intValue();
          System.out.println(age == ageIntValue);
      }
  }
  
  //8 primitive data types and 8 wrapper classes
  //Byte Short Integer Long Float Double Character Boolean
  //change to each other is simple
  ```

  

6.  **Array**  —> store the same data type collection

  - use new to create, imply that Array is an object
  - type[] viriableName = new type[number of elements]
  - virableName is reference, it points to the first address of the array, the address stores the pure type's data value itself

  ```java
  public class Player {
      public static void main(String[] args) {
          int[] primeNumbers = new int[5];
          primeNumbers[0] = 2;  // time complexity for looking up is O(1)
          primeNumbers[1] = 3;
          primeNumbers[2] = 5;
          primeNumbers[3] = 7;
          primeNumbers[4] = 11;
          System.out.println(primeNumbers[0]);
          System.out.println(primeNumbers[1]);
          System.out.println(primeNumbers[2]);
          System.out.println(primeNumbers[3]);
          System.out.println(primeNumbers[4]);
  
          int[] natural = {1, 2, 3, 4, 5, 6, 7, 8, 9};
          System.out.println(natural[0]);
          System.out.println(natural[1]);
          System.out.println(natural[2]);
          System.out.println(natural[3]);
          System.out.println(natural[4]);
          System.out.println(natural[5]);
          System.out.println(natural[6]);
          System.out.println(natural[7]);
          System.out.println(natural[8]);
  
          int[] even = new int[]{2, 4, 6, 8};
          System.out.println(even[0]);
          System.out.println(even[1]);
          System.out.println(even[2]);
          System.out.println(even[3]);
      }
  }
  ```

  - loop an Array

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        int[] natural = new int[100];
  	        for (int i = 0; i < natural.length; i++) {
  	            natural[i] = i;
  	        }
  	
  	        for (int i = 0; i < natural.length; i++) {
  	            System.out.println(natural[i]);
  	        }
  	
  	        for (int each : natural) {
  	            System.out.println(each);
  	        }
  	    }
  	}
  	```

  	- every length is public final int, once is initialized , it's fixed

  		> In Java, arrays internally use integers (int not Integer) for index, the max size is limited by the max size of integers. So theoretically it is **2^31-1** = 2147483647, which is Integer.MAX_VALUE. But in recent Hot Spot JVM it has been observed that the max size of array can be Integer.MAX_VALUE - 5. 

  - Reference type 

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        Car[] cars = new Car[3];
  	        System.out.println(cars[1]);
  	   			
  	    }
  	}
  	
  	class Car{
  	    int money;
  	
  	    public Car(int money) {
  	        this.money = money;
  	    }
  	}
  	```

  	```java
  	
  	public class Player {
  	    public static void main(String[] args) {
  	        Car[] cars = new Car[3];
  	        System.out.println(cars[1]);
  	        cars[1] = new Car(10000);
  	        System.out.println(cars[1]);
  	        System.out.println(cars[1].money);
  	    }
  	}
  	
  	class Car{
  	    int money;
  	
  	    public Car(int money) {
  	        this.money = money;
  	    }
  	}
  	```

  	

7. **2 dimensional array**

  ```text
  int[][] refer = new int[10][10];
  ```

  Practice:

  ​      0  1  2  3  4  5  6  7  8  9

  s1  A  B  A  C  C  D  E  E  A  D

  s2  D  B  A  B  C  A  E  E  A  D  

  s3  E  D  D  A  C  B  E  E  A  D

  s4  A  B  D  C  C  D  E  E  A  D   

  s5  B  B  E   C  C  D E  E  A D 

  s6  E  B  A  C  C  D  E  E  A  D

  s7  E  B  E  C  C  D  E   E  A  D

  right answer : 

  ​      D  B  D  C  C  D  A  E  A  D

  ```java
  char[][] answers={
                      {'A','B','A','C','C','D','E','E','A','D'},
                      {'D','B','A','B','C','A','E','E','A','D'},
                      {'E','D','D','A','C','B','E','E','A','D'},
                      {'C','B','A','E','D','C','E','E','A','D'},
                      {'A','B','D','C','C','D','E','E','A','D'},
                      {'B','B','E','C','C','D','E','E','A','D'},
                      {'B','B','A','C','C','D','E','E','A','D'},
                      {'E','B','E','C','C','D','E','E','A','D'},
              };
          }
  ```

  ***if interest: solve Sudoku game —> search and play on your own

8. **Arrays**

  ```java
  import java.util.Arrays;
  
  public class Player {
      public static void main(String[] args) {
          int[] a = {1, 2, 3};
          int[] b = {1, 2, 3};
          System.out.println(a.equals(b)); //if use array on your own, rewrite equals method
          System.out.println(Arrays.equals(a, b));
      }
  }
  ```

  - useful API relate to array provided by SE

  ```java
  public class Player {
      public static void main(String[] args) {
          int[] a = {1, 2, 3};
          int[] b = new int[5];
          System.arraycopy(a, 0, b, 0, 2);
          System.out.println(b);
          for (int each : b) {
              System.out.println(each);
          }
      }
  }
  ```

  - Assignments: migrate GuessBirthDay by using 3 dimensional array

    dates of sets will be stored as below: 

    ```java
     int[][][] dates = {
                            {{1, 3, 5, 7,}, 
                            {9, 11, 13, 15},
                            {17, 19, 21, 23},
                            {25, 27, 29, 31}},
                            {{2, 3, 6, 7},
                            {10, 11, 14, 15},
                            {18, 19, 22, 23},
                            {26, 27, 30, 31}}
            };
    ```

  - Bubble Sort:  write a method to sort an array in order (descent or ascend)

    ```java
    4 3 2 1
    3 4 2 1
    3 2 4 1
    3 2 1 4
    2 3 1 4
    2 1 3 4
    1 2 3 4
    ```

    - Analysis and improvement

    ```java
    public class Player {
        public static void main(String[] args) {
            int[] arr = { 9, 8, 7, 6, 5 };
            sort(arr);
            print(arr);
        }
    
    
    
        public static void sortFirst(int[] arr) {
            System.out.println("第一趟");
            for (int i = 0; i < arr.length - 1; i++) {
                System.out.print("第" + (i + 1) + "次");
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i]  = arr[i+1];
                    arr[i+1] = temp;
                }
                System.out.println(Arrays.toString(arr));
            }
        }
    
        public static void sortSecond(int[] arr) {
            System.out.println("第一趟");
            for (int i = 0; i < arr.length - 1; i++) {
                System.out.print("第" + (i + 1) + "次");
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i]  = arr[i+1];
                    arr[i+1] = temp;
                }
                System.out.println(Arrays.toString(arr));
            }
            System.out.println("第二趟");
            for (int i = 0; i < arr.length - 1; i++) {
                System.out.print("第" + (i + 1) + "次");
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i]  = arr[i+1];
                    arr[i+1] = temp;
                }
                System.out.println(Arrays.toString(arr));
            }
        }
    
        public static void sort(int[] arr){
            int len = arr.length;
            for(int j=0;j<len-1;j++){
                System.out.println("第"+(j+1)+"趟");
                for(int i=0;i<arr.length-1;i++){
                    System.out.print("第" + (i + 1) + "次");
                    if(arr[i]>arr[i+1]){
                        int temp = arr[i];
                        arr[i]= arr[i+1];
                        arr[i+1] = temp;
                    }
                    System.out.println(Arrays.toString(arr));
                }
            }
        }
    
    
        public static void print(int [] arr){
            System.out.println("Final: "+Arrays.toString(arr));
        }
    }
    ```

    - General Bubble sort

    ```java
    public class Player {
        public static void main(String[] args) {
            int[] value = { 3, 1, 6, 2, 9, 0, 7, 4, 5, 8 };
            sort(value);
            System.out.println(Arrays.toString(value));
    
        }
        private static void sort(int[] value) {
    
            int temp;
            for (int i = 0; i < value.length; i++) {
                for (int j = 0; j < value.length - 1 - i; j++) {
                    if (value[j] > value[j + 1]) {
                        temp = value[j];
                        value[j] = value[j + 1];
                        value[j + 1] = temp;
                    }
                }
            }
        }
    
    }
    ```

    - Improved Bubble Sort

    ```java
    public class Player {
        // 若已有某种顺序，则无需交换，不交换就不排列，停止之
        public static void main(String[] args) {
            int[] arr = { 9, 8, 7, 6, 5 };
    //		sort(arr);
    //		print(arr);
            System.out.println("=============================================");
    
            System.out.println("=============================================");
            sortFinal(arr);
            print(arr);
        }
    
        public static void sort(int[] arr) {
            int len = arr.length;
            for (int j = 0; j < len - 1; j++) {
                System.out.println("第" + (j + 1) + "趟");
                // 减少每一趟的次数,这里是多一趟，每趟少一次
                for (int i = 0; i < arr.length - 1 - j; i++) {
                    System.out.print("第" + (i + 1) + "次");
                    if (arr[i] > arr[i + 1]) {
                        int temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                    }
                    System.out.println(Arrays.toString(arr));
                }
            }
        }
    
        //交换就没有顺序，没有交换就有顺序
        public static void sortFinal(int[] arr) {
            boolean sorted = true;
            int len = arr.length;
            for (int j = 0; j < len - 1; j++) {
                System.out.println("第" + (j + 1) + "趟");
                // 减少每一趟的次数,这里是多一趟，每趟少一次
                for (int i = 0; i < arr.length - 1 - j; i++) {
                    sorted = true;
                    System.out.print("第" + (i + 1) + "次");
                    if (arr[i] > arr[i + 1]) {
                        int temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                        sorted = false;
                    }
                    System.out.println(Arrays.toString(arr));
                    if(sorted){ //每一趟有序
                    break;
                  }
                }
               
            }
        }
    
        public static void print(int[] arr) {
            System.out.println("Final: " + Arrays.toString(arr));
        }
    }
    ```

  - Array search

    - intuitive search

    ```java
    public class Player {
        public static void main(String[] args) {
            int[] input = {9, 5, 7, 3, 1, 11};
            int target = 7;
    
            int index = search(input, target);
            System.out.println("position of target is "+index);
        }
    		    //very bad in large scale 
        public static int search(int[] array, int target) {
            for (int i = 0; i < array.length; i++) {
                if (target == array[i]) {
                    return i;
                }
            }
    
            return -1;
        }
    }
    ```

    - find max or min in an array

    ```java
    public class Player {
        public static void main(String[] args) {
    
            int a[] = {1, 2, 3, 4, 5, 10, 7, 8, 9, 6};
            int max = Integer.MIN_VALUE;
            for (int i = 0; i < a.length; i++) {
                if (max < a[i]) {
                    max = a[i];
                }
            }
            System.out.println(max);
        }
    }
    ```

    

    - binary search using for  (in order to use binary search the input must be sorted)

    ```java
     public static void main(String[] args) {
            int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            char b[] = {'a', 'b', 'c'};
            System.out.println(indexOf(a, 6));
        }
    
    
        private static int indexOf(int[] a, int key) {
            int lo = 0;
            int hi = a.length - 1;
            for (int each : a) {
                if(lo > hi){
                  break;
                }  
                int mid = lo + (hi - lo) / 2;
                if (key < a[mid]) {
                    hi = mid - 1;
                } else if (key > a[mid]) {
                    lo = mid + 1;
                } else {
                    return mid;
                }
            }
            return -1;
        }
    ```

    - binary search using while

    ```java
    public static void main(String[] args) {
    
            int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            binarySearch(a, 7);
        }
    
    
        public static int binarySearch(int[] array, int target) {
            int low = 0;
            int high = array.length - 1;
            int middle;
    
            while (low < high) {
                middle = (low + high) / 2;
                
                
                //give a mark to show middle element
                for (int i = 0; i < array.length; i++) {
                    System.out.print(array[i]);
                    if (i == middle) {
                        System.out.print("*");
                    }
                    System.out.print(" ");
                }
                System.out.println();
                
                
                
                if (array[middle] == target) {
                    return middle;
                } else if (target < array[middle]) {
                    high = middle - 1;
                } else if (target > array[middle]) {
                    low = middle + 1;
                }
            }
    
            return -1;
        }
    ```

    - Remove duplicates in array

    	```java
    	public class ExcludeDuplicate {
    	    public static void main(String[] args) {
    	        int input[] = {1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 10, 11, 12, 12, 13, 14, 14, 14, 14, 14, 14, 14, 14};
    	        int[] res = test(input);
    	
    	        for (int i = 0; i < res.length; i++) {
    	            System.out.println(res[i]);
    	        }
    	    }
    	
    	
    	    private static int[] test(int[] input) {
    	        int slow = 0;
    	        int fast = 0;
    	        while (fast < input.length) {
    	        //when value of index slow is not equal index fast then move forward slow index value to next fast index value
    	            if (input[slow] != input[fast]) {
    	                input[++slow] = input[fast];
    	            }
    	            fast++;
    	        }
    	
    	        return Arrays.copyOf(input, slow + 1);
    	    }
    	
    	}
    	```

    	

