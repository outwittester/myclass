# JavaSE

1. **JVM**

  > - **JVM** – **Java Virtual machine**(JVM) is a very important part of both JDK and JRE because it is contained or inbuilt in both. Whatever Java program you run using JRE or JDK goes into JVM and JVM is responsible for **executing the java program line by line** hence it is also known as interpreter.
  > - **Java Virtual machine** (JVM) is the virtual machine that runs the Java bytecodes. You get this bytecode by compiling the `.java` files into `.class` files. `.class` files contain the bytecodes understood by the JVM.

  - ClassLoader   —> assembly language 

  	- Run —> Java process running and main thread starts

  	- JVM stops when:

  		- System.exit()
  		- Non caught Exception or Error
  		- OS error
  		- Code to End

  	- 1. Loading —> find .class and load into memory

  			- put bytes in the method block of runtime area then Create a Class object in heap to encapsulate the data inside of the method block (that's why we can use reflection via Class Object and fetch all the info of that class)

  		2. Linking —> 1. verify .class is under jvm standard 2. prepare static variable and set default value for class 3. parse symbolic reference to direct reference (package.class.method.reference —> real direct memory method address)

  		3. Initializing class variable to the right value

  			```java
  			public class Player{
  					      private static int a = 9;
  			      //in jvm a = 0 first then a = 9, int is 4 bytes and long is 8 bytes
  			}
  			```

  			- Active usage (the first time of active use will load the class)

  				- new

  				- call class or interface static variable or assign value to the static variable

  					ClassName.a

  				- call class static method

  					ClassName.method

  				- reflection (ex: Class.forName)

  				- initialize a subclass

  				- starter java class (main method)

  					Jvm allows to load class before using it, if .class not found when first time active use —> linkageError, if non-found class won't be used, no error will be reported

  					(use difference jdks will cause such errors when deploy)

  			- Passive usage  —> won't cause class's initialization

  				- Except all 6 above 

  			Final result —> after a class loaded , the Class Object stores inside heap

  	- JVM default classloader

  		- Bootstrap (C++, developer can't see for security reason, load by this class return null)

  			- It's for core class libraries written in native code and itself is part of JVM (Object, doesn't extends ClassLoader)

  			```java
  			public class Player {
  			    public static void main(String[] args) throws ClassNotFoundException {
  			        Class clazz = Class.forName("java.lang.String");
  			        System.out.println(clazz.getClassLoader());
  			
  			        Class myClazz = Class.forName("Algorithm.MyClass");
  			        System.out.println(myClazz.getClassLoader());
  			    }
  			}
  			class MyClass{
  			
  			}
  			```

  		- Extension 

  			- Super class is Bootstrap 
  			- Extension class loader loads from the JDK extensions directory, usually *$JAVA_HOME/lib/ext* directory or any other directory mentioned in the *java.ext.dirs* system property.

  		- System(App)  Default

  			- super class is Extension

  			- The system or application class loader, on the other hand, takes care of loading all the application level classes into the JVM. **It loads files found in the classpath environment variable, -classpath or -cp command line option**. Also, it’s a child of Extensions classloader.

  			- what to **classpath** in JVM is what $PATH to OS

  				```java
  				 String path = System.getProperty("java.class.path");
  				        System.out.println(path);
  				```

  				—> NoClassDefFoundError 

  	- java.lang.ClassLoader  (inherit from this to make your own classLoader, since java classloader only load class once and inheritance feature, malcode won't be able to load into JVM to make harm and no duplicate named class allowed in one name space, at runtime JVM is checking .class both classLoader and package name and class name, Even you write your own classLoader and hack into jvm but is different from java.lang.* classLoader which makes java secure)

  	- [ClassLoader](https://www.baeldung.com/java-classloaders)

  - Guess the result below

  ```java
  public class Player {
      public static void main(String[] args) {
          Singleton context = Singleton.getInstance();
          System.out.println("counter1 = "+context.getCounter1());
          System.out.println("counter2 = "+context.getCounter2());
      }
  }
  
  class Singleton {
  
      private static Singleton instance = new Singleton(); //change line to #line to run
  //1. load class --> simply take left side at first
  //2. set static default values  null 0 0 
  //3. initialization 1 1 --> then simply take right side
  
      private static int counter1;
      private static int counter2 = 0;
  //#
      public Singleton() {
          counter1++;
          counter2++;
      }
  
      public static Singleton getInstance(){
          return instance;
      }
  
      public static int getCounter1() {
          return counter1;
      }
  
      public static int getCounter2() {
          return counter2;
      }
  }
  ```

  - order of load

  	if not loaded, load and link first

  	if super class exists, if super class not loaded, load super class 

  	if class contains new , then initialize in order

  	when load a class requires all its super class loaded (not apply for interface, only the first time use interface static variable will cause the interface initialized)

  	```java
  	public class Player {
  	    static{
  	        System.out.println("player");
  	    }
  	    public static void main(String[] args) {
  	        System.out.println(Sub.b);
  	    }
  	}
  	
  	class Super {
  	    static int a = 2;
  	    static {
  	        System.out.println("super class");
  	    }
  	}
  	
  	class Sub extends Super{
  	    static int b = 5;
  	    static {
  	        System.out.println("sub class");
  	    }
  	}
  	```

  	```java
  	public class Player {
  	    static{
  	        System.out.println("player");
  	    }
  	    public static void main(String[] args) {
  	        Super superObject;
  	        System.out.println("-----");
  	        superObject = new Super();
  	        System.out.println(Super.a);
  	        System.out.println(Sub.b); //super class won't init second time in a single classloader, comment out above line to check
  	    }
  	}
  	
  	class Super {
  	    static int a = 2;
  	
  	    static {
  	        System.out.println("super class");
  	    }
  	}
  	
  	class Sub extends Super{
  	    static int b = 5;
  	
  	    static {
  	        System.out.println("sub class");
  	    }
  	}
  	```

  - loadClass is not Active usage

  	```java
  	public class Player {
  	    public static void main(String[] args) throws ClassNotFoundException {
  	        ClassLoader loader = ClassLoader.getSystemClassLoader();
  	
  	        Class clazz = loader.loadClass("Algorithm.SevenDeveloper");
  	        System.out.println("------");
  	        clazz = Class.forName("Algorithm.SevenDeveloper");
  	    }
  	}
  	
  	class SevenDeveloper{
  	    static {
  	        System.out.println("class 7");
  	    }
  	}
  	```

  	- Custom ClassLoader (search online and write your own class loader for practice)

2. **Design Pattern**  —> lead to interface oriented program

  Creation: Singleton Factory AbstractFactory Builder Prototype (new in different place make a difference)

  Structure: Adapter Bridge Decorator Composite Facade Proxy Flyweight

  Action: Template  Command Iterator Observer Mediator Memento State Strategy ReponsibilityChain Visitor

  - **-Singleton**  —> eager loading : use when call is frequent 

  ```java
  class Singleton{
      private static Singleton instance = new Singleton();
      // when init this class, load immediately and it's thread safe and fast (no use of synchronized)
      //but no use of this class will waste space
  
      private Singleton() {  // private contructor
      }
  
      public static Singleton getInstance() {
          return instance;
      }
  }
  ```

  —> lazy loading : use when cost of creation is high

  ```java
  class Singleton {
  
      private static Singleton instance;
  
      private Singleton() {
  
      }
  
      public static synchronized Singleton getInstance() { //for concurrent issue to avoid multiple objects creation
          if (instance == null) {
              instance = new Singleton(); //load when use, save space but slow
          }
          return instance;
      }
  }
  ```

  —> use static inner class to implement : many products use this way

  ```java
  class Singleton {
  		    //outer class no static, won't load immediately 
      private static class SingletonClassInstance{
          private static final Singleton instance = new Singleton();
      }
      //only call this method will load static inner class and thread safe and final makes instance unique
      public static Singleton getInstance() {
          return SingletonClassInstance.instance;
      }
  
      private Singleton() {
      }
  }
  ```

  for all 3 ways above of Singleton creation **master them**

  —> use enum : avoid reflection to hack 

  no lazy loading for this way

  ```java
  class Player {
  
      public static void main(String[] args) {
          Singleton o1 = Singleton.INSTANCE;
          Singleton o2 = Singleton.INSTANCE;
          System.out.println(o1 == o2);
      }
  }
  
  enum Singleton {
      INSTANCE;
  
      public void singletonMethod() {
      }
  }
  ```

  - hack Singleton use reflection 

  	```java
  	class Player {
  	
  	    public static void main(String[] args) throws Exception {
  	        Singleton o1 = Singleton.getInstance();
  	        Singleton o2 = Singleton.getInstance();
  	        System.out.println(o1 == o2);
  	
  	        Class<Singleton> clazz = (Class<Singleton>) Class.forName("Algorithm.Singleton");
  	        Constructor<Singleton> constructor = clazz.getDeclaredConstructor(null);
  	        System.out.println(constructor);
  	
  	        constructor.setAccessible(true); //
  	        Singleton o3 = constructor.newInstance();
  	        Singleton o4 = constructor.newInstance();
  	
  	        System.out.println(o3);
  	        System.out.println(o4);
  	
  	    }
  	}
  	
  	class Singleton {
  	
  	    private static Singleton instance;
  	
  	    private Singleton() {
  	    }
  	
  	    public static synchronized Singleton getInstance() {
  	        if (instance == null) {
  	            instance = new Singleton();
  	        }
  	        return instance;
  	    }
  	}
  	```

  - throw new RuntimeException in constructor to avoid when insatnce is not null

  	- for inner project may not restirct to this level
  	- for public product must consider (deserialization can also hack, think why)

  - Concurrency util to test efficiency

  	```java
  	class Player {
  	
  	    public static void main(String[] args) throws Exception {
  	
  	        long start = System.currentTimeMillis();
  	        int totalThread = 15;
  	        final CountDownLatch countDownLatch = new CountDownLatch(totalThread);
  	        for (int i = 0; i < totalThread; i++) {
  	            new Thread(new Runnable() {
  	                @Override
  	                public void run() {
  	                    for (int j = 0; j < 100000; j++) {
  	                        Singleton instance = Singleton.getInstance();
  	                    }
  	                    countDownLatch.countDown();
  	                }
  	            }).start();
  	        }
  	
  	        countDownLatch.await();
  	
  	        long end = System.currentTimeMillis();
  	        System.out.println(end-start);
  	    }
  	}
  	
  	class Singleton {
  	
  	    private static Singleton instance;
  	
  	    private Singleton() {
  	    }
  	
  	    public static synchronized Singleton getInstance() {
  	        if (instance == null) {
  	            instance = new Singleton();
  	        }
  	        return instance;
  	    }
  	}
  	```

  	
  	- **Strategy** —> Separate a group of  algorithms in different classes in order to replace when use while client won't get affected 
  	- Check Collections util source code

  ```java
  class Player {
  
      private Strategy strategy;
  
      public Player(Strategy strategy) {
          this.strategy = strategy;
      }
  
      public Strategy getStrategy() {
          return strategy;
      }
  
      public void setStrategy(Strategy strategy) {
          this.strategy = strategy;
      }
  
  
      public int calculate(int a, int b) {
          return strategy.calculate(a, b);
      }
  
      public static void main(String[] args) {
          Strategy a = new AddStrategy();
          Player player = new Player(a);
          System.out.println(player.calculate(2, 3));
          Strategy s = new SubStrategy();
          player.setStrategy(s);
          System.out.println(player.calculate(4,5));
      }
  }
  
  
  
  interface Strategy{
      int calculate(int a, int b);
  }
  
  class SubStrategy implements Strategy{
  
      @Override
      public int calculate(int a, int b) {
          return a-b;
      }
  }
  
  class AddStrategy implements Strategy{
  
      @Override
      public int calculate(int a, int b) {
          return a+b;
      }
  }
  ```

  - - Client must know different strategies before using and must strategy classes created
  	- Check Car For Factory 

  - **Proxy**  —> Client doesn't want to know any change about the real object when using (AOP)

  	-  normally involve one interface one proxy role and one real role

  	```java
  	class Player {
  	    public static void main(String[] args) {
  	        Subject subject = new ProxySubject();
  	        subject.request();
  	    }
  	}
  	
  	
  	abstract class Subject{
  	    public abstract void request();
  	}
  	
  	class RealSubject extends Subject {
  	    @Override
  	    public void request() {
  	        System.out.println("I'm real");
  	    }
  	}
  	
  	class ProxySubject extends Subject{
  	    private RealSubject realSubject;
  	
  	    @Override
  	    public void request() {
  	        filter();
  	        if (realSubject == null) {
  	            realSubject = new RealSubject();
  	        }
  	        realSubject.request();
  	    }
  	
  	    private void filter() {
  	        System.out.println("do something before ");
  	    }
  	}
  	```

  	- Real subject must exist before using, developer to provide the proxy service

  	

  	**Abstract Proxy**  —> java.lang.reflect  Interface InvocationHandler  (or called dynamic proxy)

  	  —> the jvm to generate the proxy service at runtime 

  	JDK dynamic proxy:

  	​	java.lang.reflect.Proxy —> for generate class and object
  	
  	​	java.lang.reflect.InvocationHandler —> call realSubjcet method 
    
  	 public object invoke(Object obj, Method method, Object[] args)
    
  	obj —> proxy class, method —> request () , args —> input parameters 
  	
  	use below example as temple when use
  	
  	```java
  	public class Player implements InvocationHandler {
  	
  	    private Object sub;
  	
  	
  	    public Player(Object sub) {
  	        this.sub = sub;
  	    }
  	
  	    @Override
  	    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
  	        if (method.getName().equals("request")) {
  	            System.out.println("before ");
  	            method.invoke(sub, args);
  	            System.out.println("after ");
  	        }
  	        return null;
  	    }
  	
  	
  	    public static void main(String[] args) {
  	        Subject subject = new RealSubject();
  	        InvocationHandler handler = new Player(subject);
  	        Class clazz = subject.getClass();
  	        Subject proxyInstance = (Subject) Proxy.newProxyInstance(clazz.getClassLoader(), clazz.getInterfaces(), handler);
  	        proxyInstance.request();
  	        proxyInstance.request2();
  	        System.out.println("------");
  	
  	    }
  	}
  	
  	
  	interface Subject {
  	    void request();
  	
  	    void request2();
  	}
  	
  	
  	class RealSubject implements Subject {
  	
  	    @Override
  	    public void request() {
  	        System.out.println("I'm real");
  	    }
  	
  	    public void request2() {
  	        System.out.println("I'm real in request2");
  	    }
  	}
  	
  	```
  	
  	
  	
  	**Factory**
  	
  	> simple factory : for producing any product in the same level (code has to change when add new product)
  	
  	> factory method : for producing the same product in the same level (support add new product)
  	
  	> abstract factory : for producing all products in different groups of product (can't add new single product, support new group of product)
  	>
  	> - simple project use simple
  	>
  	> - JDK Calendar getInstance
  	>
  	> - JDBC Connetion to create Connection
  	>
  	> - Hibernate SessionFactory create session
  	>
  	> - Spring IOC create and manage bean objects + Singleton 
  	>
  	> - parsing XML DocumentBuilderFactory
  	>
  	> 	
  	
  	- use without any design pattern
  	
  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        BMW c1 = new BMW();
  	        Benz c2 = new Benz();
  	        c1.run();
  	        c2.run();
  	    }
  	}
  	
  	
  	interface Car {
  	    void run();
  	}
  	
  	class BMW implements Car {
  	
  	    @Override
  	    public void run() {
  	        System.out.println("BMW running");
  	    }
  	}
  	
  	class Benz implements Car {
  	
  	    @Override
  	    public void run() {
  	        System.out.println("Benz running");
  	    }
  	}
  	```
  	
  	- use simple factory
  	
  	```java
  	public class CarFactory {
  	    //add new car will change code below, code can't extend without changing code by using simple factory
  	    public static Car createCar(String type) {
  	        if ("BMW".equals(type)) {
  	            return new BMW();
  	        } else if ("Benz".equals(type)) {
  	            return new Benz();
  	        } else {
  	            return null;
  	        }
  	    }
  	
  	    // another way to create object
  	    public static Car createBMW() {
  	        return new BMW();
  	    }
  	
  	    public static Car createBenz() {
  	        return new Benz();
  	    }
  	}
  	
  	public class Main {
  	    public static void main(String[] args) {
  	        // For client only deal with CarFactory
  	        Car c1 = CarFactory.createCar("BMW");
  	        Car c2 = CarFactory.createCar("Benz");
  	
  	        c1.run();
  	        c2.run();
  	    }
  	}
  	```
  	
  	- factorymethod (in order to use design pattern to design)
  	
  	```java
  	public class BenzFactory implements CarFactory {
  	    @Override
  	    public Car createCar() {
  	        return new Benz();
  	    }
  	}
  	
  	public class BMWFactory implements CarFactory {
  	    @Override
  	    public Car createCar() {
  	        return new BMW();
  	    }
  	}
  	
  	public interface CarFactory {
  	    Car createCar();
  	}
  	
  	public class Main {
  	    public static void main(String[] args) {
  	
  	        //when adding a new car, just create new class without changing any existing code
  	        Car c1 = new BMWFactory().createCar();
  	
  	        Car c2 = new BenzFactory().createCar();
  	
  	        c1.run();
  	
  	        c2.run();
  	    }
  	}
  	```
  	
  	- abstract factory
  	
  	```java
  	public interface CarFactory {
  	    Engine createEngine();
  	
  	    Seat createSeat();
  	
  	    Tyre createTyre();
  	}
  	
  	public interface Engine {
  	    void run();
  	
  	    void start();
  	}
  	
  	public interface Seat {
  	    void warm();
  	
  	    void massage();
  	}
  	
  	public interface Tyre {
  	    void aging();
  	}
  	
  	public class LuxuryCarFactory implements CarFactory{
  	    @Override
  	    public Engine createEngine() {
  	        return new LuxuryEngine();
  	    }
  	
  	    @Override
  	    public Seat createSeat() {
  	        return new LuxurySeat();
  	    }
  	
  	    @Override
  	    public Tyre createTyre() {
  	        return new LuxuryTyre();
  	    }
  	}
  	
  	public class LuxuryEngine implements Engine {
  	    @Override
  	    public void run() {
  	        System.out.println("Luxury Engine rotating fast");
  	    }
  	
  	    @Override
  	    public void start() {
  	        System.out.println("Luxury Engine starts fast");
  	    }
  	}
  	
  	public class LuxurySeat implements Seat {
  	    @Override
  	    public void warm() {
  	        System.out.println("Luxury can warm your seat in winter");
  	    }
  	
  	    @Override
  	    public void massage() {
  	        System.out.println("Luxury can massage when driving");
  	    }
  	}
  	
  	public class LuxuryTyre implements Tyre {
  	    @Override
  	    public void aging() {
  	        System.out.println("Luxury tyre can be used up to 6 years");
  	    }
  	}
  	
  	public class StandardEngine implements Engine{
  	    @Override
  	    public void run() {
  	        System.out.println("standard engine rotates");
  	    }
  	
  	    @Override
  	    public void start() {
  	        System.out.println("standard engine starts");
  	    }
  	}
  	
  	public class StandardFactory implements CarFactory {
  	    @Override
  	    public Engine createEngine() {
  	        return new StandardEngine();
  	    }
  	
  	    @Override
  	    public Seat createSeat() {
  	        return new StandardSeat();
  	    }
  	
  	    @Override
  	    public Tyre createTyre() {
  	        return new StandardTyre();
  	    }
  	}
  	
  	public class StandardSeat implements Seat {
  	    @Override
  	    public void warm() {
  	        System.out.println("standard seat can let you sit");
  	    }
  	
  	    @Override
  	    public void massage() {
  	        System.out.println("standard seat is a seat to sit,want massage, buy luxury");
  	    }
  	}
  	
  	public class StandardTyre implements Tyre {
  	    @Override
  	    public void aging() {
  	        System.out.println("standard tyre changes every 3 years");
  	    }
  	}
  	```
  	
  	
  	
  	- Key to use design pattern is how to encapsulate and "wrapper your code" 
  	
  		

3. **XML**  —> extensible markup language

  - SAX  —> based on event stream               (startElement, endElement)
  - DOM —> based on xml tree structure
  - DOM4J 
  - JDOM

4. TCP** (server — clients) 

  - stable with 3 hands shake
  - connect first then communicate

  server — port —IP — client — port — application (thread with byte stream)

  ```java
  public class TcpServer {
      public static void main(String[] args) throws IOException {
          ServerSocket ss = new ServerSocket(5000);
  
          Socket socket = ss.accept();
  
  
          InputStream is = socket.getInputStream();
  
          OutputStream os = socket.getOutputStream();
  
          byte[] buffer = new byte[200];
  
          int length = is.read(buffer);
  
          System.out.println(new String(buffer,0,length));
  
          os.write("Dear I am coming ".getBytes());
  
          is.close();
          os.close();
          socket.close();
  
      }
  }
  ```

  

  ```java
  public class TcpClient {
      public static void main(String[] args) throws IOException {
          Socket socket = new Socket("127.0.0.1", 5000);
  
          InputStream is = socket.getInputStream();
  
          OutputStream os = socket.getOutputStream();
  
          os.write("hello world".getBytes());
  
          byte[] buffer = new byte[200];
  
          int length = is.read(buffer);
  
          System.out.println(new String(buffer, 0, length));
          is.close();
          os.close();
          socket.close();
      }
  }
  ```

  

  **UDP**

  - unstable but fast (game , video)
  - each unit of data is independent 

5. **URL** —> one standard of TCP/IP, weak but simple, no need to understand protocol itself

  https://www.google.com/webhp?authuser=1

  protocol domain hostname port resource location

  - java.net.URL 

  ```java
  public class Player {
      public static void main(String[] args) throws IOException {
          URL url = new URL("https://www.google.com");
          System.out.println(url.toString());
          System.out.println(url.getContent());
          System.out.println(url.getHost());
          System.out.println(url.getProtocol());
          //test more methods on your own
  
          URLConnection connection = url.openConnection();
          InputStream is = connection.getInputStream();
  		        //InputStream is = url.openStream();  // open stream directly
     
          OutputStream os = new FileOutputStream("test.txt");
          byte[] buffer = new byte[1024];
          int length = 0;
          while (-1 != (length = is.read(buffer, 0, 1024))) {
              os.write(buffer,0,length);
          }
  
          is.close();
          os.close();
      }
  }
  ```

6. Tomcat

  Follow me —> check examples

7. JDBC

  ```java
  public class jdbcTest {
      // JDBC driver name and database URL
      static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
      static final String DB_URL = "jdbc:mysql://localhost:3306/blog?useSSL=false&useUnicode=true&characterEncoding=utf-8&serverTimezone=UTC";
  //    jdbc:mysql://localhost/db?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC
  
      //  Database credentials
      static final String USER = "yourusername";
      static final String PASS = "yourpassword";
  
      public static void main(String[] args) throws ClassNotFoundException {
          Connection connection = null;
          Statement statement = null;
  
          Class clazz = Class.forName("com.mysql.jdbc.Driver");
          try {
              connection = DriverManager.getConnection(DB_URL, USER, PASS);
              statement = connection.createStatement();
              String sql = "select * from role";
              ResultSet rs = statement.executeQuery(sql);
  
              while (rs.next()) {
                  System.out.println(rs.getInt(0));
              }
          } catch (SQLException e) {
              System.out.println("out");
              e.printStackTrace();
          }
  
      }
  }
  ```

  - statement (sql injection) VS prepare statement (multiple) vs callable statement (procedure)trigger

  	Google above and be sure understand

  	



