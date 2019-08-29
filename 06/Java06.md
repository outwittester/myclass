# JavaSE

1. **Exception**

	>An exception is an unwanted or unexpected event, which occurs during the execution of a program
	
	Object —> Throwable (Exceptions and Error)
	
	```java
	public class Player {
	    public static void main(String[] args) {
	        int a = 1;
	        int b = 0;
	        System.out.println(a / b);
	    }
	}

	Exception in thread "main" java.lang.ArithmeticException: / by zero
	at Algorithm.Player.main(Player.java:7)
	```

	- Checked Exception (Non Runtime Exception)

	- Unchecked Exception (Runtime Exception)

		- Q: Which exception does ArithmeticException belongs to?
	
- Error (can not be able to repair) but Exception can  (both from Throwable interface )
	
	- no need to care about error cause it's designed shoud not try to catch
		
	- abnormal serious problems (JVM Error)
	
- try catch exception
	
		- nothing wrong code run as normal 
		- exception happens, catch block will take care of the rest of try catch blocks
		- after dealing with exception, app keeps running (that's why exception can be repaired)
	
		```java
		public class Player {
		    public static void main(String[] args) {
		        try {
		            int a = 1;
		            int b = 0;
		            System.out.println(a / b);
		       			     System.out.println("where am i?");
		        } catch (ArithmeticException e) {
		            System.out.println("something went wrong");
		            System.err.println("something went wrong");
		            e.printStackTrace();
		        }
				         System.out.println("end of try catch");
		    }
		}
		```
	```
	
		- finally
			- finally block will run whatever exception throwed out or not
	
		```java
		public class Player {
		    public static void main(String[] args) {
		        try {
		            int a = 1;
		            int b = 1;
		            System.out.println(a / b);
		            System.out.println("where am i?");
		        } catch (ArithmeticException e) {
		            System.out.println("something went wrong");
		            System.err.println("something went wrong");
		            e.printStackTrace();
		        }finally {
		            System.out.println("finally I will print out");
		        }
		        System.out.println("end of try catch");
	
		    }
	}
	```
	
		- syntax to throw exception
		
			```java
			 public void methodName() throws Exception {
		        System.out.println("exception is typical implementation of inheritance");
			        throw new Exception();
		}
			```
		
			- either use **try catch block** or (**throws with throw new** ExceptionType)
		
			- if use throws, the exception will be deal with the one who is calling this method
		
		- if throws all the way down to main method, no one before main wants to catch, JVM will catch it then deal with it. 
		
				- calling method must either try catch or throws out
				- for checked exception, must deal with or can't compile
		
				```java
				public class Player {
				    public static void main(String[] args) {
				
				        Player player = new Player();
				        player.methodName(); // force you throws or try catch
				                
				    }
				
				    public void methodName() throws Exception {
				        System.out.println("exception is typical implementation of inheritance");
			        throw new Exception();
				    }
		}
				```
		
				- for unchecked exception(runtime exception), recommend not to deal with, give it JVM
	
	- **NullPointerException**
	
		- this exception happens as someone's reference is null and somewhere is still calling that reference method
	
		```java
		public class Player {
		    public static void main(String[] args) {
		        String s = null;
		        System.out.println(s.length());
	        NullPointerException
		    }
	}
		```

	- Custom Exception
	
		- Inherit from Exception directly or indirectly
		- Normal action is inherit from Exception
		- read the exception document hierarchy, learn from one and write your own exception
	
		```java
		public class Player {
		    public static void main(String[] args) throws MyException {
		        Player p = new Player();
		        p.method(null);
		    }
		
		    public void method(String s) throws MyException {
		        if (null == s) {
		            throw new MyException("input str should not be null");
		        }else{
		            System.out.println(s);
		        }
		    }
		}
		//think MyException is runtime exception or checked exception?
		```
	
- multiple exception
	
	- throws multiple exceptions  
	
	```java
		public class Player {
		    public static void main(String[] args) throws MyException, MyException2 {
		
		        Player p = new Player();
		        p.method("Tump");
		    }
		
		    public void method(String s) throws MyException, MyException2 {
		        if (null == s) {
		            throw new MyException("input str should not be null");
		        }else if(s.equals("Tump")){
		            throw new MyException2("Tump shall not be input ");
		        }else{
		            System.out.println(s);
		        }
		    }
		}
		
		class MyException extends Exception {
		    public MyException() {
		        super();
		    }
		
		    public MyException(String message) {
		        super(message);
		    }
		}
		
		class MyException2 extends Exception {
		    public MyException2() {
		        super();
		    }
		
		    public MyException2(String message) {
		        super(message);
		    }
		}
	```
	
	- catch multiple exceptions
	
	```java
		public class Player {
		    public static void main(String[] args) {
		
		        Player p = new Player();
		        try {
		            p.method("Tump");
		        } catch (MyException e) {
		            e.printStackTrace();
		        } catch (MyException2 myException2) {
		            myException2.printStackTrace();
		        }
		    }
		
		    public void method(String s) throws MyException, MyException2 {
		        if (null == s) {
		            throw new MyException("input str should not be null");
		        } else if (s.equals("Tump")) {
		            // tell what's the difference of s.equals("str") and str.equals(s)
		            throw new MyException2("give me another str");
		        } else {
		            System.out.println(s);
		        }
		    }
		}
		
		
		class MyException extends Exception {
		    public MyException() {
		        super();
		    }
		
		    public MyException(String message) {
		        super(message);
		    }
		}
		
		class MyException2 extends Exception {
		    public MyException2() {
		        super();
		    }
		
		    public MyException2(String message) {
		        super(message);
		    }
		}
	```
	
	
	
- When multiple catch clause, must put superclass exception clause after sub exception clause or generates unreachable code. Add throws Exception to main method to check why.
	
- return won't stop finally 
	
	```java
		public class Player {
		    public static void main(String[] args) throws Exception{
		
		        Player p = new Player();
		        try {
		            p.method("Tom");
		            return;
		        } catch (MyException e) {
		            e.printStackTrace();
		        } catch (MyException2 myException2) {
		            myException2.printStackTrace();
		        }finally {
		            System.out.println("finally");
		        }
		        System.out.println("out of try catch");
		    }
		
		    public void method(String s) throws MyException, MyException2 {
		        if (null == s) {
		            throw new MyException("input str should not be null");
		        } else if (s.equals("Tump")) {
		            throw new MyException2("give me another str");
		        } else {
		            System.out.println(s);
		        }
		    }
		}
		
		
		class MyException extends Exception {
		    public MyException() {
		        super();
		    }
		
		    public MyException(String message) {
		        super(message);
		    }
		}
		
		class MyException2 extends Exception {
		    public MyException2() {
		        super();
		    }
		
		    public MyException2(String message) {
		        super(message);
		    }
		}
	```
	
	
	
2.  **Inner Class**

	- defined at smaller scope than package(part of class)
	- reduce namespace clutter of related classes
	- can be inside of a class \ method \ an expression
	- 1. static inner class 2. member inner class 3. local inner class 4. anonymous inner class
			- static inner class

	```java
	//think static method again
	public class Player {
	    private static int playerFiled = 10;
	
	    public static void main(String[] args) {
	
	        Player.AnotherClassInsideOfPlayer inner = new AnotherClassInsideOfPlayer();
	        inner.a = 5;
	        System.out.println(inner.a);
	        int a = Player.playerFiled;
	        System.out.println(a);
	    }
	
	    static class AnotherClassInsideOfPlayer {
	        int a;
	    }
	
	}
	```

	- - member inner class

	```java
	public class Player {
	    private static int a = 10;
	
	    public static void main(String[] args) {
	
	        AnotherClassInsideOfPlayer inner = new Player().new AnotherClassInsideOfPlayer();
	//        AnotherClassInsideOfPlayer inner2 = (new Player()).new AnotherClassInsideOfPlayer();
	        inner.a = 5;
	        System.out.println(inner.a);
	        int a = Player.a;
	        System.out.println(a);
	    }
	
	     class AnotherClassInsideOfPlayer {
	        int a;
	    }
	
	}
	```

	- - method inner class

	```java
	public class Player {
	    public static void main(String[] args) {
	        Player p = new Player();
	        p.print();
	    }
	
	
	    public void print() {
	        final int a = 10;
	        class InnerMethod{
	            public void printOfInner() {
	                System.out.println("anything "+a);
	            }
	        }
	        new InnerMethod().printOfInner();
	    }
	
	}
	```

	- - anonymous class
		- Implicitly extend a **superclass** or implement an **interface**
		- {}  inherited from **the class after** **new** 

	```java
	public class Player {
	    public static void main(String[] args) {
	        Date d = new Date() {
	        };
	        System.out.println(d.getTime());
	    }
	}
	```
	
- rethink can an abstract  class be new? 
	- can static be used in anonymous class?
	
```java
	public class Player {
	    public static void main(String[] args) {
	        Date d = new Date() {
	            public String toString() {
	                return "nothing";
	            }
	        };
	        System.out.println(d.toString());
	    }
	}
	```
	
```java
	public class Player {
	    public static void main(String[] args) {
	        Player p = new Player() {
	            public void doSth() {
	                System.out.println("override");
	            }
	        };
	        p.doSth();
	   
	        UserService u = new UserService() {
	            @Override
	            public void greetUser(String greating) {
	                System.out.println("override of interface");
	            }
	        };
	        u.greetUser("whatever");
			       	//normally anonymous class only has one method which is very good to replace with java 8 new feature of lambda pression where makes code clean and more compact
	//Java lambda expressions can only be used where the type they are matched against is a single method interface.
	        UserService javaEightLambda = greating -> {
	            System.out.println("just be clean here yes override again");
	        };
	        javaEightLambda.greetUser("agiain");
	
	    }
	
	    public void doSth() {
	        System.out.println("hello world");
	    }
	}
	
	interface UserService {
	    void greetUser(String greating);
	}
```

	- little about Lambda Expression to loop
	
		```java
	public class Player {
		    public static void main(String[] args) {
		        ArrayList<Integer> list = new ArrayList<>();
		        list.add(1);
		        list.add(2);
		        list.add(3);
		        list.add(4);
		        list.add(5);
		        list.forEach((n)-> System.out.println(n));
		        System.out.println("-------------------");
		        list.forEach(n -> {
		            if (n % 2 == 0)
		            System.out.println(n);
		        });
		        System.out.println("----");
		
		    }
		}
		```


​		

3. **IO**   —>  input output Stream

	- File class —> file and directory
	- File itself can't read 
	- Common use file methods

	```java
	public class Player {
	    public static void main(String[] args) throws IOException {
	        File file = new File("abc.txt");
	        file.createNewFile();
	        File file2 = new File(".", "cde.txt");
	        file2.createNewFile();
	        File file3 = new File("givenPath");
	        file3.mkdir();
	        System.out.println(file.isFile());
	        System.out.println(file.isDirectory());
	
	        System.out.println(File.pathSeparator);
	        String pwd = System.getProperty("user.dir");
	        System.out.println(pwd);
	        File direcotry = new File(pwd);
	        String[] files = direcotry.list();
	        for (String each : files) {
	            System.out.println(each);
	        }
	        //Try File[] files = direcotry.listFiles(); //the same
	        System.out.println(direcotry.getParentFile());
	        System.out.println("--------");
	        for (String each : files) {
	            if (each.endsWith(".txt")) {
	                System.out.println("yes");
	                System.out.println(each);
	            }
	        }
	
	        //replace with lambda
	        String[] filterNames = direcotry.list((dir, name) -> {
	            if (name.endsWith(".txt")) {
	                return true;
	            }
	            return false;
	        });
	        System.out.println("====");
	        for (String each : filterNames) {
	            System.out.println(each);
	        }
	    }
	}
	```

	

4. **Recursion **

	- method call itself 
	- base case

	- Practice: use recursion to solve Fibonacci and Factorial

	- very careful to use recursion cause easily occur infinite loop

		```java
		public class Fibonacci {
		
		    public static void main(String[] args) {
		        System.out.println(fib(8));
		        System.out.println(improvedFib(8));
		    }
		    public static long fib(long index) {
		        if (index == 0) {
		            return 0;
		        } else if (index == 1) {
		            return 1;
		        } else {
		            return fib(index - 1) + fib(index - 2);
		        }
		    }
		
		    public static long improvedFib(long index) {
		        long f0 = 0;
		        long f1 = 1;
		        long f2 = 1;
		
		        if (index == 0) {
		            return f0;
		        }
		
		        else if (index == 1) {
		            return f1;
		        }
		
		        else if (index == 2) {
		            return f2;
		        }
		        ;
		
		        for (int i = 3; i <= index; i++) {
		            f0 = f1;
		            f1 = f2;
		            f2 = f0 + f1;
		        }
		
		        return f2;
		    }
		}
		```

	- Combine File and recursion to delete

		- create a direcotry and put some dump directories and files to test

		```java
		public class Player {
		    public static void main(String[] args) throws IOException {
		
		    }
		
		    public static void deleteAll(File file) {
		        if (file.isFile() || file.list().length == 0){
		            file.delete();
		        }else{
		            File[] files = file.listFiles();
		            for (File each : files) {
		                deleteAll(each);
		                each.delete();
		            }
		        }
		    }
		}
		```

		

5.  **java.io** and **Stream**

	- Stream is abstraction of contruction and consuption of information

	- Regardless of physical parts of PC, all stream has the same function, java provides the encapsulation and abstraction

	- For an app, it can be source or destination then it can be output or input

	- in java.io mainly has 2 streams, **InputStream** and **OutputStream** (byte stream —> deal with bytes)

	- Byte Stream and Character Stream ( Reader and Writer —> deal with character for convenience, like String encapsulation)  

	- 8 bits binary bytes vs 16 bits binary character

		- basic logic to deal with Stream

			```java
			open a stream
			while more information
			read information
			close the stream
			```

	- Another Classification

		- Node stream —> read from a specific space  (like from File) connect with source and destination
		- Filter stream —> use existed Node stream as input or output to create connection (FilterInputStream) shall not to connect with source or destination directly

	**InputStream and OutputStream**  (Byte Stream)

	```java
	public class Player {
	    public static void main(String[] args) throws IOException {
	        InputStream inputStream = new FileInputStream("test.txt");
	        byte[] buffer = new byte[200]; //each time can only store 200 long
	        int length = 0;
	        //every time read from the source to buffer
	        //each time put into buffer from 0 position to the length of 200
	        //actual content is length
	        //check if it returns -1 which means end of source
	        while (-1 != (length = inputStream.read(buffer, 0, 200))) {
	            String each = new String(buffer, 0, length);//now should know why need length variable
	            System.out.println(each);
	        }
	
	        inputStream.close(); //all stream must close after using
	    }
	}
	```

	- list tree structure of a directory

	```java
	public class Player {
	    public static void main(String[] args) throws IOException {
	        listFileTree(new File("/Users/xikaixiong/Desktop/fileTest/myclass"));
	    }
	
	    private static int time;
	
	    public static void listFileTree(File file) {
	        if (file.isFile() || 0 == file.listFiles().length) {
	            return;
	        } else {
	            File[] files = file.listFiles();
	            files = sort(files);
	
	            for (File each : files) {
	                StringBuffer output = new StringBuffer();
	                if (each.isFile()) {
	                    output.append(getTabs(time));
	                    output.append(each.getName());
	                } else {
	                    output.append(getTabs(time));
	                    output.append(each.getName());
	                    output.append("/");
	                }
	
	                System.out.println(output);
	
	                if (each.isDirectory()) {
	                    time++;
	                    listFileTree(each);
	                    time--;
	                }
	            }
	        }
	    }
	
	    private static File[] sort(File[] files) {
	        ArrayList<File> sortedFiles = new ArrayList<>();
	        for (File each : files) {
	            if (each.isDirectory()) {
	                sortedFiles.add(each);
	            }
	        }
	        for (File each : files) {
	            if (each.isFile()) {
	                sortedFiles.add(each);
	            }
	        }
	        return sortedFiles.toArray(new File[files.length]);
	    }
	
	    private static String getTabs(int time) {
	        StringBuffer buffer = new StringBuffer();
	        for (int i = 0; i < time; i++) {
	            buffer.append("\t");
	        }
	
	        return buffer.toString();
	    }
	}
	
	```

	

	- InputSteam —> 

	- - - - FileInputStream
				- ByteArrayInputStream
				- ObjectInputStream
				- PipeInputeStream
				- SequenceInputStream
				- StringBufferInputStream
				- FilterInputStream  —> (for transfering the stream to specific data type or format)
				- - - - - - - - DataInputStream   (readByte() readBoolean()... readLine())
											- BufferedInputStream 
											- LineNumberInputStream
											- PushbackInputStream

	- OutputStream (there is corresponding outputstream for inputstream)

		```java
		public class Player {
		    public static void main(String[] args) throws IOException {
		
		        OutputStream os = new FileOutputStream("test.txt");
		        String str = "Hello there";
		
		        byte[] brffer = str.getBytes();
		        os.write(brffer);
		        os.close();
		
		    }
		}
		```

		- BufferedOutputStream

		```java
		public class Player {
		    public static void main(String[] args) throws IOException {
		
		        OutputStream os = new FileOutputStream("test.txt");
		        BufferedOutputStream bos = new BufferedOutputStream(os);
		        bos.write("https://www.sincere.com".getBytes());
		        bos.close();  //comment out this line to check diff and think why
		        os.close();
		    }
		}
		```

		- based on different names choose the right stream to use

			- ByteOutputStream

			```java
			public class Player {
			    public static void main(String[] args) throws IOException {
			        ByteOutputStream bos = new ByteOutputStream();
			        String str = "hello world";
			        byte[] buffer = str.getBytes();
			        bos.write(buffer);
			        OutputStream os = new FileOutputStream("test.txt");
			        bos.writeTo(os);
			        bos.close();
			        os.close();
			    }
			}
			```

			- ByteArrayOutputStream

			```java
			public class Player {
			    public static void main(String[] args) throws IOException {
			        ByteArrayOutputStream bos = new ByteArrayOutputStream();
			        String str = "hello world ByteArrayOutputStream";
			        byte[] buffer = str.getBytes();
			        bos.write(buffer);
			        OutputStream os = new FileOutputStream("test.txt");
			        bos.writeTo(os);
			        bos.close();
			        os.close();
			    }
			}
			```

			- DataOutputStream and DataInputStream

			```java
			public class Player {
			    public static void main(String[] args) throws IOException {
			        DataOutputStream dos = new DataOutputStream(new BufferedOutputStream(new FileOutputStream("test.txt")));
			
			        byte b = 1;
			        short s = 2;
			        int i = 3;
			        float f = 4.0f;
			        double d = 5.0;
			        char c = 'c';
			        dos.writeByte(b);  //change this to dos.write(b) then run
			        dos.writeShort(s); //change this to dos.write(s) then run
			        dos.writeInt(i);    // think the difference
			        dos.writeFloat(f);
			        dos.writeDouble(d);
			        dos.writeChar(c);
			        dos.writeUTF("utf-8");
			
			        dos.close();
			
			        DataInputStream dis = new DataInputStream(new BufferedInputStream(new FileInputStream("test.txt")));
			        System.out.println(dis.readByte());
			        System.out.println(dis.readShort());
			        System.out.println(dis.readInt());
			        System.out.println(dis.readFloat());
			        System.out.println(dis.readDouble());
			        System.out.println(dis.readChar());
			        System.out.println(dis.readUTF());
			        dis.close();
			    }
			```

	- Byte stream though provides any data operations but can't deal with Unicode 

	- Character Stream  Reader and Writer

	- Java uses Unicode as String and char, 2 bytes as 1 character taking 16 bits

		- InputStreamReader and OutputStreamWriter

		- dealing with character is very convenient 

			```java
			public class Player {
			    public static void main(String[] args) throws IOException {
			        FileOutputStream fos = new FileOutputStream("test.txt");
			        OutputStreamWriter osw = new OutputStreamWriter(fos);
			        BufferedWriter bw = new BufferedWriter(osw);
			        bw.write("https://www.sincere.com");
			        bw.write("https://www.google.com");
			        bw.close();
			   			     //write inputStream to read, search on yourself
			    }
			}
			```

			- Understanding System.in

			```java
			public class Player {
			    public static void main(String[] args) throws IOException {
			        InputStreamReader isr = new InputStreamReader(System.in);
			
			        BufferedReader br = new BufferedReader(isr);
			
			        String input;
					
			        while (null != (input = br.readLine())) {
			            System.out.println(input);
			        }
			        br.close();
			
			    }
			}
			```

			- FileReader

			```java
			public class Player {
			    public static void main(String[] args) throws IOException {
			        FileReader fr = new FileReader("test.txt");
			
			        BufferedReader br = new BufferedReader(fr);
			
			        String input;
			        while (null != (input = br.readLine())) {
			            System.out.println(input);
			        }
			
			        br.close();
			    }
			}
			```

			- FileWriter

			```java
			public class Player {
			    public static void main(String[] args) throws IOException {
			        FileWriter fw = new FileWriter("test.txt");
			        fw.write("what are you doing here?");
			        fw.close();
			    }
			}
			```

			- RandomAccessFile (self learning)
			- EOF : end of file exception —> use seek to reset the position

6.  **Serializable**

	- Transfer an object  to byte stream and recover the object later is called serialization and deserialization

	- Keep  an object to a hardware is called persistence.  (data presistence)

	- Implement **Serializable** or **Externalizable**

	- Serializable is a marker interface

	- One object is referred by serialized object will cause this object serialized.

	- Non-Serializable Object throws NotSerializableException

	-  Use **transient** to modify non-serializable object

	- **static fields and methods won't be serializable**

	  - ObjectOutput interface   —> writeObject method : write an object to the underlying storage or stream 

	  - ObjectOutputStream class

	  - ObjectInput interface  —> readObject

	  - ObjectInputStream 

	  	```java
	  	public class Player {
	  	    public static void main(String[] args) throws IOException {
	  	        Person p1 = new Person("name1", 20, 5.5);
	  	        Person p2 = new Person("name2", 30, 6.5);
	  	        Person p3 = new Person("name3", 40, 7.5);
	  	
	  	        //file suffix doesn't matter
	  	        FileOutputStream fos = new FileOutputStream("test.txt");
	  	
	  	        ObjectOutputStream oos = new ObjectOutputStream(fos);
	  	        oos.writeObject(p1);
	  	        oos.writeObject(p2);
	  	        oos.writeObject(p3);
	  	        oos.close();
	  	    }
	  	}
	  	
	  	
	  	class Person implements Serializable {
	  	    //think again what's the diff by using private and without private
	  	    private String name;
	  	
	  	    private int age;
	  	
	  	    private double height;
	  	
	  	    public Person(String name, int age, double height) {
	  	        this.name = name;
	  	        this.age = age;
	  	        this.height = height;
	  	    }
	  	}
	  	```

	  - Read Object from file

	  	```java
	  	public class Player {
	  	    public static void main(String[] args) throws IOException, ClassNotFoundException {
	  	        Person p1 = new Person("name1", 20, 5.5);
	  	        Person p2 = new Person("name2", 30, 6.5);
	  	        Person p3 = new Person("name3", 40, 7.5);
	  	
	  	        //file suffix doesn't matter
	  	        FileOutputStream fos = new FileOutputStream("test.txt");
	  	
	  	        ObjectOutputStream oos = new ObjectOutputStream(fos);
	  	        oos.writeObject(p1);
	  	        oos.writeObject(p2);
	  	        oos.writeObject(p3);
	  	        oos.close();
	  	
	  	        System.out.println("---------");
	  	
	  	        FileInputStream fis = new FileInputStream("test.txt");
	  	        ObjectInputStream ois = new ObjectInputStream(fis);
	  	
	  	        Person p = null;
	  	        
	  	        for (int i = 0; i < 3; i++) {
	  	            p = (Person) ois.readObject();
	  	            System.out.println(p);
	  	        }
	  	
	  	    }
	  	}
	  	
	  	
	  	class Person implements Serializable {
	  	    //think again what's the diff by using private and without private
	  	    private String name;
	  	
	  	    private int age;
	  	
	  	    private double height;
	  	
	  	    public Person(String name, int age, double height) {
	  	        this.name = name;
	  	        this.age = age;
	  	        this.height = height;
	  	    }
	  	
	  	    public String getName() {
	  	        return name;
	  	    }
	  	
	  	    public void setName(String name) {
	  	        this.name = name;
	  	    }
	  	
	  	    public int getAge() {
	  	        return age;
	  	    }
	  	
	  	    public void setAge(int age) {
	  	        this.age = age;
	  	    }
	  	
	  	    public double getHeight() {
	  	        return height;
	  	    }
	  	
	  	    public void setHeight(double height) {
	  	        this.height = height;
	  	    }
	  	
	  	    @Override
	  	    public String toString() {
	  	        return "Person{" +
	  	                "name='" + name + '\'' +
	  	                ", age=" + age +
	  	                ", height=" + height +
	  	                '}';
	  	    }
	  	}
	  	```

	  	- use transient to modify one field to check the difference

	  - hidden methods of serializable to control serialization

	  	```java
	  	 private void writeObject(java.io.ObjectOutputStream out) throws IOException{
	  	        out.writeUTF(this.name);
	  	        out.writeInt(this.age);
	  	        System.out.println("writing");
	  	    }
	  	    private void readObject(java.io.ObjectInputStream in) throws IOException{
	  	   			     this.name = in.readUTF();
	  	        System.out.println("reading");
	  	    }
	  	```

	
