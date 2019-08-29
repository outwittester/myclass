# Java SE

1. **OOP** (Encapsulation & Inheritance & Polymorphism)

  - Object Oriented Programming  (VS Functional)

  - OOD -> Object Oriented Design

  - Class and Object

  - Class AS concept 

    > data + actions (actions to deal with data)
    >
    > data is noun called property or attribute or member variable 
    >
    > action is verb called method
    >
    > **class is a blueprint or template which describe state and behavior of its type**

  - Object AS concept

    > one specific thing of a class, **instance of a class**

  - Class Definition in java

  - Code in IDE(integrated development environment)  —> introduction about intellij 

    ```java
    class Player {
        //class name should be capital letter with camel rule
    }
    class PlayerField{
    
    }
    ```

    Entrance of an application is Main

    class contains main method must be declared as public?

    ```java
    public class Play {
        public static void main(String[] args) {
    
        }
    }
    ```

  - Method Definition in java

    ```java
    modifier returnType methodName(param1,param2, ...){
    	      method body;
    			      //method name should use camel rule
    }
    
    private static int gcd(int p, int q) {
            if (q == 0) {
                return p;
            }
            int r = p % q;
            return gcd(q, r);
        }
    ```

  - Object in java

    ```java
    Player player1 = new Player();// means use Player class as template to create an object, an object has all the features from that class
    Player player2 = new Player();
    //each object is also called instance
    //Object is controlled by reference
    //player1 is reference not object
    //An object can be referred by multiple references
    //But one reference can only refer to one object at a time,any one changes effects
    //Then which part is object above?
    //new key word opens a new address in memory heap (you can go further if you dive deep into it) 
    //player is in stack
    ```

    ```java
    //reference makes the change
    public class Player {
        int age = 25;
        
      	  public void change(Player player) {
      			     // player = new Player();
            player.age = 30;
        }
        public static void main(String[] args) {
            Player player = new Player();
            int age = player.age;
            System.out.println(age);
            player.change(player);
            age = player.age;
            System.out.println(age);
        }
    }
    ```

  - java is **pass by value**

    ```java
    Pass by Value: The method parameter values are copied to another variable and then the copied object is passed, that's why it's called pass by value.
    
    Whatever reference type or primitive type in java, all pass by value. 
    The value of reference type is memory address.
    
    public class Player {
        public static void main(String[] args) {
            int i = 9;
            increaseByOne(i);
            System.out.println(i);
        }
    
        public static void increaseByOne(int input) {
            input = input + 1;
        }
    }
    
    public class Player {
        public static void main(String[] args) {
            int x = 3;
            int y = 4;
            Player.swap(x, y);
            System.out.println("x is " + x);
            System.out.println("y is" + y);
        }
    
        public static void swap(int a, int b) {
            int temp = a;
            a = b;
            b = temp;
            System.out.println("a is " + a);
            System.out.println("b is " +  b);
        }
    }
    //Array variable is a reference, primitive is value itself
    public class Player {
        public static void main(String[] args) {
            char[] input = {'A', 'C'};
            swap(input, input[1]);
            for (Character each : input) {
                System.out.println(each); 
            }
        }
    
        public static void swap(char[] ch, char c) {
            ch[0] = 'B';
            c = 'D';
        }
    }
    
    //what's the result?
    public class Player {
        public static void main(String[] args) {
            int[] a = {1, 2, 3};
            int[] b = {1, 2, 3};
            System.out.println(a.equals(b));
        }
    }
    ```

    

  - Method calling

    ```java
    1. static method can be called directly within the class or via the className.methodName
    2. no static method should be called via an object
    object.methodName
    ```

    > As the returned type is *Obviously* declared, you will have to declare to fetch it.
    >
    > Java is Strong-typed.
    >
    > No return type then must use **void** key word

    

2. **Encapsulation**

  - Wrap data (variables) and action (methods) together as a single unit

  - Below is encapsulation and also a typical pojo -> plain java object

  	```java
  	public class Player {
  	    private int age;
  	    private String name;
  	
  	    public Player(int age, String name) {
  	        this.age = age;
  	        this.name = name;
  	    }
  					    //contructor -> method has the same name with class
  			    //do something when initialize the object
  	    //no return type and no void
  			    //when not provided by developer, java compiler will generate an ampty constructor to use, otherwise will use the one which developer defines
  	    //when new is used, contructor is called
  	    public int getAge() {
  	        return age;
  	    }
  	
  	    public void setAge(int age) {
  	        this.age = age;
  	    }
  	
  	    public String getName() {
  	        return name;
  	    }
  	
  	    public void setName(String name) {
  	        this.name = name;
  	    }
  	}
  	```

  - Method

  	- overload (don't recommend personally, multiple same named methods in huge debug is a mess)

  	- method param numbers

  	- method param types

  	- overload is not a OOP concept as overload methods are not late binding

  		- compile stage -> early binding
  		- runtime stage -> late binding

  		```java
  		public class Player {
  		    public static void main(String[] args){
  		        System.out.println(Adder.add(1,2));
  		        System.out.println(Adder.add(3, 4, 5));
  		        System.out.println(Adder.add(3.14,3.14));
  		    }
  		}
  		
  		class Adder{
  		    static int add(int a,int b){return a+b;}
  		    static int add(int a,int b,int c){return a+b+c;}
  		    static double add(double a, double b){return a+b;}
  		}
  		```

3. **Inheritence**

  - java is single Inheritence by using key word **extends**

  	```java
  	public class Player extends Parent {
  	
  	    private Player() {
  	        System.out.println("Player");
  	    }
  	
  	    public static void main(String[] args) {
  	        Player player = new Player();
  	    }
  	}
  	
  	class Parent {
  	    public Parent() {
  	        System.out.println("Parent");
  	    }
  	}
  	What is the output?
  	```

  	```java
  	public class Player extends Parent {
  	
  	    private Player() {
  	        super(1);
  	   	    //call parent empty constructor by default
  	   	    	//super key word is used for calling parent's object reference
  	   		    //this key word is used for calling current object reference  -> check above Player class
  	       //super method has to be first
  	        System.out.println("Player");
  	    }
  	
  	    public static void main(String[] args) {
  	        Player player = new Player();
  	    }
  	}
  	
  	class Parent {
  	
  	    public Parent() {
  	        System.out.println("Parent");
  	    }
  	
  	    public Parent(int i){
  	        System.out.println("Parent with int");
  	    }
  	}
  	```

  - Override 

  	Q: what's the difference/relation between overload and override?  

  	```java
  	public class Player extends Parent {
  	
  	    //String name = "earth";
  	    public static void main(String[] args) {
  	        Player player = new Player();
  	        System.out.println(player.name);
  	
  	    }
  	}
  	
  	class Parent {
  	    String name = "sun";
  	}
  	
  	
  	```

  	- what parent has, child has          (super class and subclass)
  	- what parent doesn't have, child can add
  	- what parent has, child can change

  	```java
  	public class Player extends Parent {
  	
  	    private String name = "earth";
  	    public static void main(String[] args) {
  	        Player player = new Player();
  	        String name = player.getName(1);
  	        System.out.println(name);
  	    }
  	    public String getName(int i){
  	        System.out.println(this.name+" is inside getName");
  	        return this.name;
  	    }
  	
  	}
  	
  	class Parent {
  	    private String name = "sun";
  	    public String getName(){
  	        return this.name;
  	    }
  	}
  	```

  - All classes' Parent -> Object  (java.lang.Object in JDK)

4. **Polymorphism**

  - remember -> Parent reference refer to Child's Object **or** interface reference refer to its implementation instance

  - Polymorphism on OO techniques will expand your view beyond use individual class

  - Significant effort is a worthy struggle

    - faster program development
    - better code organization
    - extensible programs -> decouple *what* from *how*
    - easier code maintenance

    ```java
    public class Player extends Parent {
    
        private String name = "moon";
        public String getName(){
            return this.name;
        }
    
        public static void main(String[] args) {
            Parent parentObject = new Player();
            String name = parentObject.getName();
            System.out.println(name);
        }
    }
    
    class Parent {
        private String name = "sun";
        public String getName(){
            return this.name;
        }
    }
    
    ```

    ```java
    public class Player {
    
        public static void main(String[] args) {
            Shape shape = new Triangle();
           //shape.draw();
       			    // Shape shape = new Shape(); only runtime can decide which object it refers
            Triangle triangle = (Triangle) shape;
            triangle.draw();
            //doesn't above work?
        }
    }
    
    
    class Triangle extends Shape {
        private String name;
        private Point pA;
        private Point pB;
        private Point pC;
    
        public void draw() {
            System.out.println("triangle");`
        }
    }
    
    class Point {
        private double x, y;
    }
    
    class Shape {
        private String name;
    }
    ```

  - dynamic binding

    > understand args 

    - Run Test

    ```java
    public class Test{
        public static void main(String[] args){
            for(String each:args){
                System.out.println(each);
            }
    
        }
    }
    ```

    

    ```java
    public class Player {
    
        public static void main(String[] args) {
            Shape shape = new Shape();
            if (args[0].equals("0")) {
                shape = new Triangle();
            } else if (args[0].equals("1")) {
                shape = new RegularTriangle();
            } else if (args[0].equals("2")) {
                shape = new EquicruralTriangle();
            } else if (args[0].equals("3")) {
                shape = new RightTriangle();
            }
    
            shape.draw();
            System.out.println("-----");
            for (int i = 0; i < args.length; i++) {
                System.out.print(args[i]);
            }
        }
    }
    
    
    class Triangle extends Shape {
        private String name;
        private Point pA;
        private Point pB;
        private Point pC;
    
        @Override
        public void draw() {
            System.out.println("triangle");
        }
    }
    
    class RegularTriangle extends Triangle {
        @Override
        public void draw() {
            System.out.println("RegularTriangle");
        }
    }
    
    class EquicruralTriangle extends Triangle {
        @Override
        public void draw() {
            System.out.println("EquicruralTriangle");
        }
    }
    
    class RightTriangle extends Triangle {
        @Override
        public void draw() {
            System.out.println("RightTriangle");
        }
    }
    
    class Point {
        private double x, y;
    }
    
    class Shape {
        private String name;
    
        public void draw() {
            System.out.println("shape");
        }
    }
    ```

  - Example of Benefit of Polymorphism

    ```java
    public class Player {
    
        public void run(BMW bmw) {
            bmw.drive();
        }
    
        public void run(Fort fort) {
            fort.drive();
        }
        public static void main(String[] args) {
            Player player = new Player();
            BMW bmw = new BMW();
            player.run(bmw);
            Fort fort = new Fort();
            player.run(fort);
    
        }
    }
    
    class Car{
    
        public void drive() {
            System.out.println("Car driving");
        }
    }
    
    class BMW extends Car{
    
        @Override
        public void drive() {
            System.out.println("BMW driving");
        }
    }
    
    class Fort extends Car{
        @Override
        public void drive() {
            System.out.println("Fort driving");
        }
    }
    ```

    > refactor

    ```java
    public class Player {
    
        public void run(Car car) {
            car.drive();
        }
    
        public static void main(String[] args) {
            Player player = new Player();
            Car car1 = new BMW();
            player.run(car1);
            System.out.println("-----");
            Car car2 = new Fort();//Fort car2 = new Fort();
            player.run(car2);
        }
    }
    
    class Car{
        public void drive() {
            System.out.println("Car driving");
        }
    }
    
    class BMW extends Car{
    
        @Override
        public void drive() {
            System.out.println("BMW driving");
        }
    }
    
    class Fort extends Car{
        @Override
        public void drive() {
            System.out.println("Fort driving");
        }
    }
    //no matter how many new cars added, no new run method will be created
    //that's why better code organization and also extensible
    ```

    

- Polymorphism => abstract thinking 

	- **abstract** 

		```java
		public class Player {
		
		    public static void main(String[] args) {
		        T t = new T() {
		            @Override
		            int ha() {
		                return 0;
		            }
		        };
		
		        int a = t.ha();
		        System.out.println(a);
		        t.what();
		    }
		
		}
		
		
		abstract class T{
		    abstract int ha();
		
		    public void what() {
		        System.out.println("what");
		    }
		}
		class S extends T{
		
		    @Override
		    int ha() {
		        return 0;
		    }
		
		    public void own() {
		        System.out.println("own");
		    }
		}
		
		//subclass must implement superclass abstract methods
		//abstract method force you to implement
		```

		- understand // check myBlog

			```java
			public interface TypeRepository extends JpaRepository<Type,Long> {
			}
			```

		

	- **interface**  -> implements

		> all methods in inteface are abstract
		>
		> **think** When to use abstract class and interface
		>
		> you can implements multiple intefaces but extends only one class 
		>
		> Java is single inheritance
		>
		> non-abstract class must implement interface's methods

		Q: How java realizes multiple inheritance ?

	- ```java
		interface A{
		    void method1();
		
		    int method2();
		
		    double method3();
		}
		
		interface B{
		    boolean method4();
		}
		```

		```java
		public interface UserDao {
		    User findByUsernameAndPassword(String username, String password);
		}
		```

		```java
		public class UserDaoImpl implements UserDao {
		
		    @Autowired
		    private JdbcTemplate jdbcTemplate;
		
		    @Override
		    public User findByUsernameAndPassword(String username, String password) {
		        String sql = String.format("select * from t_user where username='%s' and password ='%s'", username, password);
		        RowMapper mapper = new UserMapper();
		        try {
		            User user = (User) jdbcTemplate.queryForObject(sql, mapper);
		            System.out.println("sql in daoimpl " + sql);
		            return user;
		        } catch (EmptyResultDataAccessException e) {
		            return null;// null is not best practice
		        }
		
		    }
		
		}
		```

- Key words : 

  - static

  	> static -> fields(class member variables) 
  	> 			          methods 
  	> 			          class

  ```java
  
  
  // what's the age of p2?
  	public class Player {
      public static void main(String[] args) {
  
          Parent p1 = new Parent();
          Parent p2 = new Parent();
          p1.age = 50;
          System.out.println(p2.age);
  
      }
  }
  
  
  class Parent {
      int age;
  }
  //what if add static to age?
  
  //Whatever how many instance created, they share the same static variable
  //static makes it unique in memory
  //when to use static -> util, global thinking, does it make sense to call this method, even if no Obj has been constructed yet?
  
  ```

  > check myblog MD5Utils for static methods
  >
  > ```java
  > public static String code(String str) {
  >  try {
  >      MessageDigest md = MessageDigest.getInstance("MD5");
  >      md.update(str.getBytes());
  >      byte[] byteDigest = md.digest();
  >      int i;
  >      StringBuffer buf = new StringBuffer("");
  >      for (int offset = 0; offset < byteDigest.length; offset++) {
  >          i = byteDigest[offset];
  >          if (i < 0)
  >              i += 256;
  >          if (i < 16)
  >              buf.append("0");
  >          buf.append(Integer.toHexString(i));
  >      }
  >      //32位加密
  >      return buf.toString();
  >      // 16位的加密
  >      //return buf.toString().substring(8, 24);
  >  } catch (NoSuchAlgorithmException e) {
  >      e.printStackTrace();
  >      return null; //still null is not best practice
  >  }
  > 
  > }
  > ```
  >
  > className.methodName  
  >
  > ```java
  > public class Player {
  >     public static void main(String[] args) {
  >         String set1 = " 1  3  5  7\n 9 11 13 15\n17 19 21 23\n25 27 29 31";
  >         String set2 = " 2  3  6  7\n10 11 14 15\n18 19 22 23\n26 27 30 31";
  >         String set3 = "  4  5  6  7\n12 13 14 15\n20 21 22 23\n28 29 30 31";
  >         String set4 = " 8  9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31";
  >         String set5 = "16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31";
  > 
  >         int day = 0;
  > 
  >         int answer = JOptionPane.showConfirmDialog(null,
  >                 "Is your birthday in thess numbers\n" + set1);
  >         if (answer == JOptionPane.YES_OPTION)
  >             day += 1;
  > 
  >         answer = JOptionPane.showConfirmDialog(null,
  >                 "Is your birthday in thess numbers\n" + set2);
  >         if (answer == JOptionPane.YES_OPTION)
  >             day += 2;
  > 
  >         answer = JOptionPane.showConfirmDialog(null,
  >                 "Is your birthday in thess numbers\n" + set3);
  >         if (answer == JOptionPane.YES_OPTION)
  >             day += 4;
  > 
  >         answer = JOptionPane.showConfirmDialog(null,
  >                 "Is your birthday in thess numbers\n" + set4);
  >         if (answer == JOptionPane.YES_OPTION)
  >             day += 8;
  > 
  >         answer = JOptionPane.showConfirmDialog(null,
  >                 "Is your birthday in thess numbers\n" + set5);
  >         if (answer == JOptionPane.YES_OPTION)
  >             day += 16;
  > 
  >         JOptionPane.showMessageDialog(null, "your birthday is " + day);
  >     }
  > }
  > ```
  >
  > 
  >
  > Q: Why return null is no good?
  >
  > ```java
  > Parent p = null;
  > System.out.println(p.age);
  > ```
  >
  > ```java
  > public class Player {
  >  static{
  >      System.out.println("static block");
  >  }
  > 	    public static void main(String[] args) {
  >      System.out.println("first");
  >  }
  > }
  > // Q: what's the reuslt?
  > // JVM will read content(classloader) disk of class file, the static block is already executed in memory regardless inheritance feature,but only once
  > public class Player {
  >  static{
  >      System.out.println("static block");
  >  }
  > 
  >  public static void main(String[] args) {
  >      new Player();
  >      new Player();
  > 
  >      System.out.println("first");
  >  }
  > }
  > ```
  >
  > - Can access non-static viriable in static method?
  >
  > 	```java
  > 	    int a;
  > 	    public static void what() {
  > 	        a =9;
  > 	    }
  > 	//why?
  > 	//Thus static method can't use this key word
  > 	//static method can't be override
  > 	```
  >
  > 	

  

  - final

  	>final primitive data type can't be changed 
  	>
  	>final reference date type can't refer to other object, but the content can change 
  	>
  	>final class can't be extended
  	>
  	>final method can't be override

  	```java
  	final int number = 0; //if you want to use, have to initialize immediatly or in constructor are best practices;
  	```

  	

  - Accessibility

  	>- The data members, class or methods which are not declared using any access modifiers i.e. having default access modifier are accessible **only within the same package**.
  	>
  	>	-------------
  	>
  	>- The methods or data members declared as **private** are accessible only **within the class** in which they are declared.
  	>
  	>- Any other **class of same package will not be able to access**these members.
  	>
  	>- Top level Classes or interface can not be declared as private because
  	>
  	>	1. private means “only visible within the enclosing class”.
  	>	2. protected means “only visible within the enclosing class and any subclasses”
  	>
  	>	---------
  	>
  	>- The methods or data members declared as **protected** are **accessible within same package or sub classes in different package.**
  	>
  	>	---------
  	>
  	>- The **public** access modifier has the **widest scope** among all other access modifiers.
  	>
  	>- Classes, methods or data members which are declared as public are **accessible from every where** in the program. There is no restriction on the scope of a public data members.







