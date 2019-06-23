# JavaSE

1. **Generics** (introduced in SE 5)

	> When class definition logic are the same but only the types of class variable(member variable) are different. Java provides generics  to avoid generating too many silimar classes.
	>
	> - Generics is effective in compile stage. No influence at runtime. 

	```java
	public class Player {
	    public static void main(String[] args) {
	        GenericsFoo<String> s = new GenericsFoo<>();
	        s.setFoo("what");
	        System.out.println(s.getFoo());
	
	        GenericsFoo<Integer> s2 = new GenericsFoo<>();
	        s2.setFoo(100);
	        System.out.println(s2.getFoo());
	    }
	}
	
	class GenericsFoo<T>{
	    private T foo;
	
	    public GenericsFoo() {
	    }
	
	    public T getFoo() {
	        return foo;
	    }
	
	    public void setFoo(T foo) {
	        this.foo = foo;
	    }
	
	}
	```
	
- Generics in Collection
	
- Generics will help erase cast as type is known at first place
	
	```java
		public class Player {
		    public static void main(String[] args) {
		        List<Integer> ages = new ArrayList<>();
		
		        ages.add(1);
		        ages.add(1);
		        ages.add(1);
		        ages.add(1);
		        System.out.println(ages.isEmpty());
		        System.out.println(ages.size());
		        System.out.println("--------");
		        for (int each : ages) {
		            System.out.println(each);
		        }
		        System.out.println("-------");
		
		        for (int i = 0; i < ages.size(); i++) {
		            Integer each = ages.get(i);
		            System.out.println(each);
		        }
		    }
		}
	```
	
- Reading Any collection source code(ArrayList) — understand how to write custom Generics
	
	```java
		public class Player {
		    public static void main(String[] args) {
		        Map<Integer, String> map = new HashMap<>();
		        map.put(1, "a");
		        map.put(2, "b");
		        map.put(3, "c");
		        map.put(4, "a");
		
		        Set keys = map.keySet();
		        for (Iterator<Integer> i = keys.iterator(); i.hasNext(); ) {
		            int key = i.next();
		            String value = map.get(key);
		            System.out.println(key + " = " + value);
		        }
		        System.out.println("-------");
		        Set<Map.Entry<Integer,String>> entry = map.entrySet();
		        for (Map.Entry<Integer, String> each : entry) {
		            System.out.println(each);
		        }
		    }
		}
	```
	
	- extends to restrict the usage
	
		```java
			public class Player {
			    public static void main(String[] args) {
			        ListGenericsFoo<LinkedList> obj1 = new ListGenericsFoo<>();
			        ListGenericsFoo<ArrayList> obj2 = new ListGenericsFoo<>();
			
			    }
			}
			
			class ListGenericsFoo<T extends List>{
			    private T[] fooArray;
			
			    public T[] getFooArray() {
			        return fooArray;
			    }
			
			    public void setFooArray(T[] fooArray) {
			        this.fooArray = fooArray;
			    }
			
			}
		```
	
	- ? and super can also be used in generics
	
	- If you want to write your own generics well then keep learning (for usage purpose now is enough to go)
	
2. **Varargs**

	```java
	public class Player {
	    public static void main(String[] args) {
	        System.out.println(sum(1,2,3,4,5,6,7,8,9,10));
	    }
	
	
	    private static int sum(int... inputs) {
	        int sum = 0;
	        for (int each : inputs) {
	            sum += each;
	        }
	
	        return sum;
	    }
	}
	```

	

3.  **Emum** 

	- public static final by default,compiler help use to hide some details but same level with class and interface
	- java.lang.Enum  
	- every member of Enum is an public static final instance 
	- number of Emum objects in is fixed by definition, define 4 then the Enum has 4

	```java
	public class Player {
	    public static void main(String[] args) {
	        Season spring = Season.SPRING;
	        System.out.println(spring);
	
	        for (Season each : Season.values()) {
	            System.out.println(each);
	        }
	    }
	}
	
	enum Season {
	    SPRING, SUMMER, AUTUMN, WINTER;
	}
	```

	- Practice:write a enum days class and use switch case to print out each day by input as numbers

	```java
	enum Season {
	    SPRING("comfortable"), SUMMER("hot"), AUTUMN("comfortable"), WINTER("cold"),WHAT(1);
	
	    private String value;
	    private int time;
	
	    Season(String value) {
	        this.value = value;
	    }
	
	    Season(int time) {
	        this.time = time;
	    }
	
	    public String getValue() {
	        return value;
	    }
	
	    public static void main(String[] args) {
	        Season spring = Season.SPRING;
	        System.out.println(spring);
	
	        String valueOfSpring = spring.getValue();
	        System.out.println(valueOfSpring);
	
	        Season what = Season.WHAT;
	        int valueOfWhat = what.time;
	        System.out.println(valueOfWhat);
	        System.out.println("-----------");
	
	        for (Enum each : Season.values()) {
	            int index = each.ordinal();
	            System.out.println(index);
	            System.out.println(each);
	        }
	    }
	
	}
	```

	- Iterator to loop an Enum

		```java
		enum Season {
		    SPRING("comfortable"), SUMMER("hot"), AUTUMN("comfortable"), WINTER("cold"), WHAT(1);
		
		    private String value;
		    private int time;
		
		    Season(String value) {
		        this.value = value;
		    }
		
		    Season(int time) {
		        this.time = time;
		    }
		
		    public String getValue() {
		        return value;
		    }
		
		    public static void main(String[] args) {
		        Season autumn = Season.valueOf("AUTUMN"); //rethink of wrapper class Integer.valueOf() doing
		        System.out.println(autumn);
		
		        System.out.println("------");
		
		        EnumSet set = EnumSet.of(Season.SPRING, Season.SUMMER, Season.AUTUMN); //just part of Season
		        set.add(Season.AUTUMN); //no duplicate as it's a set
		        set.add(Season.WINTER);
		        for (Iterator i = set.iterator(); i.hasNext(); ) {
		            System.out.println(i.next());
		        }
		
		        System.out.println("------");
		
		        EnumSet set2 = EnumSet.allOf(Season.class);
		        Iterator i2 = set2.iterator();
		        while (i2.hasNext()) {
		            Enum each = (Enum) i2.next();
		            System.out.println(each);
		        }
		
		        System.out.println("-------");
		        //java 8
		        EnumSet.allOf(Season.class).forEach(season -> System.out.println(season));
		    }
		
		}
		```

		- EnumMap learn on yourself 

	- Reasons for using enum

		- Old way of dealing with Constant is not safe

		```java
		public class Player {
		    public static void main(String[] args) {
		        boolean manager = Player.checkAccessibility("M");
		        System.out.println(manager);
		        boolean managerTypingWrong = Player.checkAccessibility("m");
		        System.out.println(managerTypingWrong);
		    }
		
		
		    public static boolean checkAccessibility(String role) {
		        if (role.equals("M")) {
		            return true;
		        } else if (role.equals("D")) {
		            return false;
		        } else if (role.equals("S")) {
		            return false;
		        }
		        return false;
		        //code is verbose, you can simplify on logic
		    }
		}
		
		
		class Constants {
		    public static final String manager = "M";
		    public static final String developer = "D";
		    public static final String staff = "S";
		}
		```

		- improvement

		```java
		public class Player {
		    public static void main(String[] args) {
		        Roles role = Roles.MANAGER;
		        boolean manager = checkAccessibility(role);
		        System.out.println(manager);
		        Roles role2 = Roles.DEVELOPER;
		        boolean developer = checkAccessibility(role2);
		        System.out.println(developer);
		
		        //As you can only choose role from enum, no other roles will be given as input
		    }
		
		    public static boolean checkAccessibility(Roles role) {
		
		        if (role == Roles.MANAGER) {
		            return true;
		        } else if (role.equals(Roles.DEVELOPER)) {
		            return true;
		        }else{
		            return false;
		        }
		
		        //think does == and equals in enum make difference?
		    }
		
		
		}
		
		
		enum Roles {
		    MANAGER, DEVELOPER, STAFF;
		}
		```

		

4.  **Reflection**

  - Foundation of frameworks

  - reflection is to fetch information about class and object at runtime

  	- javac compile first then java run
  	- check an object's class at runtime
  	- construct an objcet of a class at runtime
  	- check class fileds and methods at runtime
  	- call any object at runtime
  	- By given a class name then reflection will have all the info
  	- This feature makes java not that static, kind of dynamic
  		- dynamic language can still run even exist compile error (check at runtime)
  		- dynamic language can change viable type after initialization

  - java.lang.reflect

  - Class —> a class

  - Field —> class fields

  - Method —> methods of class

  - Constructor  —> class constructor

  - Array  —> create array dynamically and static methods to call array elements

     Everything in java is object  How about primitive data type?

     - Reflection to fetch class info

     	```java
     	public class Player {
     	    public static void main(String[] args) throws ClassNotFoundException {
     	        Class clazz = Class.forName("java.lang.String");
     	        System.out.println(clazz);//which class is clazz?
     	        System.out.println("-------");
     	        Method[] methods = clazz.getMethods();
     	        for (Method each : methods) {
     	            System.out.println(each);
     	        }
     	
     	        System.out.println("-------");
     	        Field[] fields = clazz.getFields();
     	        for (Field each : fields) {
     	            System.out.println(each);
     	        }
     	
     	        System.out.println("--------");
     	        Constructor[] constructors = clazz.getConstructors();
     	        for (Constructor each : constructors) {
     	            System.out.println(each);
     	        }
     	    }
     	}
     	```

     	

     - Dynamically by passing parameter (client pass the info of class)

     	```java
     	public class Player {
     	    public static void main(String[] args) throws ClassNotFoundException {
     	        Class clazz = Class.forName(args[0]);
     	        Method[] methods = clazz.getMethods(); //which class is clazz?
     						
     	        for (Method each : methods) {
     	            System.out.println(each);
     	        }
     	
     	    }
     	}
     	```

     - Custom class

     	```java
     	class Person{
     	    private String name;
     	
     	    public String getName() {
     	        return name;
     	    }
     	
     	    public String sayHello(String message) {
     	        return "Hello " + this.name;
     	    }
     	
     	    public static void main(String[] args) throws ClassNotFoundException {
     	        Class clazz = Class.forName("Algorithm.Person");
     			        // Class clazz = Person.class;  // this way doesn't throw exception
     	        //because every class has an class object .class can be used when the class exists, no class then compile error, no need for exception
     	        Constructor[] constructors = clazz.getConstructors();
     	        for (Constructor each : constructors) {
     	            System.out.println(each);
     	        }
     	
     	        Method[] methods = clazz.getMethods();
     	        for (Method each : methods) {
     	            System.out.println(each);
     	        }
     	
     	        Field[] fields = clazz.getFields();
     	        for (Field each : fields) {
     	            System.out.println(each);
     	        }
     	
     	    }
     	}
     	```

     - constructor with parameter

     	```java
     	public class Player {
     	
     	    public static void main(String[] args) throws Exception {
     	        Class clazz = Person.class;
     	        Person p = (Person) clazz.getDeclaredConstructor(String.class).newInstance("initial Parameter");
     	        System.out.println(p.getName());
     	    }
     	}
     	
     	
     	class Person {
     	    private String name;
     	
     	    public Person(String name) {
     	        this.name = name;
     	    }
     	
     	    public void setName(String name) {
     	        this.name = name;
     	    }
     	
     	    public String getName() {
     	        return name;
     	    }
     	}
     	```

     	

     - create object by using Class method

     	```java
     	public class Player {
     	    public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, IllegalAccessException, InvocationTargetException, InstantiationException {
     	        Class clazz = Class.forName("Algorithm.Person");
     	
     	        Person p = (Person) clazz.getDeclaredConstructor().newInstance();
     	        System.out.println(p);
     	
     	        //what's the modifier of String name?
     	        String name = p.getName();
     	        System.out.println(name);
     	        System.out.println(p.sayHello("Lee"));
     	
     	        Constructor[] constructors = clazz.getConstructors();
     	        for (Constructor each : constructors) {
     	            System.out.println(each);
     	        }
     	
     	        Method[] methods = clazz.getMethods();
     	        for (Method each : methods) {
     	            System.out.println(each);
     	        }
     	
     	        Field[] fields = clazz.getFields();
     	        for (Field each : fields) {
     	            System.out.println(each);
     	        }
     	    }
     	}
     	
     	
     	class Person {
     	    private String name;
     	
     	    public String getName() {
     	        return name;
     	    }
     	
     	    public String sayHello(String name) {
     	        return "Hello " + name;
     	    }
     	}
     	```

     - call method by using reflection

       ```java
       public class Player {
       	    //if too many exceptions, just use Exception
           public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, IllegalAccessException, InvocationTargetException, InstantiationException {
               Class clazz = Class.forName("Algorithm.Person");
               //Class clazz = new Person().getClass();
       
               Method getName = clazz.getMethod("getName");
       //        Method getName = clazz.getMethod("getName");
               System.out.println(getName);
       
               Method sayHello = clazz.getMethod("sayHello", String.class, int.class);
               //same as above but explicit
       //        Method sayHello = clazz.getMethod("sayHello", new Class[]{String.class, int.class});
               System.out.println(sayHello);
       
               System.out.println("--------");
               System.out.println(Modifier.toString(sayHello.getModifiers()));
               System.out.println(sayHello.getReturnType());
               System.out.println(sayHello.getName());
       
               System.out.println("--------------");
       
               //invoke method
       //        Person p = new Person();
               Person p = (Person) clazz.getDeclaredConstructor().newInstance();
             //below is to create object with parameter using reflectiong
       //        Person p = (Person) clazz.getDeclaredConstructor(String.class).newInstance("parameter");
               String reflectWayOfCallingMethod = (String) sayHello.invoke(p, new Object[]{"Jackson",1});
               System.out.println(reflectWayOfCallingMethod);
       
           }
       }
       
       
       class Person {
           private String name;
       
           public String getName() {
               return name;
           }
       	
           public String sayHello(String name,int index) {
               return "Hello " + name+" you are number "+index;
           }
       }
       ```

       - Q: How reflection is used in framework? check stack overflow

       

       - use reflection to copy those custom defined methods

       - ```java
         public class ReflectToCopyAnObject {
             public static void main(String[] args) throws Exception {
                 ReflectToCopyAnObject r = new ReflectToCopyAnObject();
                 Customer c = new Customer();
                 Customer copyObj = (Customer) r.copy(c);
                 System.out.println("copied age is "+copyObj.getAge());
                 System.out.println("copied id is "+copyObj.getId());
                 System.out.println("copied name is "+copyObj.getName());
         
                 c.setAge(5);
                 c.setId(1l);
                 c.setName("first");
                 Customer copyObj2 = (Customer) r.copy(c);
                 System.out.println("copied age is "+copyObj2.getAge());
                 System.out.println("copied id is "+copyObj2.getId());
                 System.out.println("copied name is "+copyObj2.getName());
         
             }
             //this method is going to copy an Ojbect
             public Object copy(Object inputObject) throws Exception {
                 Class clazz = inputObject.getClass();
         
                 //the returned object is objectCopy
                 Object objectCopy = clazz.getConstructor().newInstance();
         
         
                 //get all fields
                 Field[] fields = clazz.getDeclaredFields();
                 for (Field each : fields) {
                     String name = each.getName();
                     String firstLetter = name.substring(0, 1).toUpperCase();
                     String getMethodName = "get" + firstLetter + name.substring(1);
                     String setMethodName = "set" + firstLetter + name.substring(1);
         //            System.out.println("getMethod name is " + getMethodName);
         //            System.out.println("setMethod name is " + setMethodName);
         //            System.out.println("----");
                     Method getMethodObj = clazz.getMethod(getMethodName);
         
                     //since we can get all the fields,then we can get their methods based on each filed's type
                     Method setMethodObj = clazz.getMethod(setMethodName, each.getType());
         //            System.out.println("getMethod obj is " + getMethodObj);
         //            System.out.println("setMethod obj is " + setMethodObj);
         //            System.out.println("====");
         
                     Object getMethodValue = getMethodObj.invoke(inputObject);
                //copy the value from getMethodObj(from inputOjbect) to the copied Object which is objectCopy, then objectCopy's method gets the value of invoked method
                     setMethodObj.invoke(objectCopy,getMethodValue);
         //            System.out.println(object);
                 }
         
                 return objectCopy;
             }
         }
         
         class Customer {
         
             private Long id;
             private String name;
             private int age;
         
         
             public Customer() {
             }
         
             public Customer(String name, int age) {
                 this.name = name;
                 this.age = age;
             }
         
             public Long getId() {
                 return id;
             }
         
             public void setId(Long id) {
                 this.id = id;
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
         }
         ```
  ```java
         
       - understand of using invoke method
       
       	```java
       	public class ReflectToCopyAnObject {
       	    public static void main(String[] args) throws Exception {
       	        Class clazz = Customer.class;
       	        System.out.println(clazz);
       	
       	        Customer c = (Customer) clazz.getConstructor().newInstance();
       	        c.setName("what");
       	        Customer c2 = (Customer) clazz.getConstructor().newInstance();
       	        c2.setName("hello");
       	        c2.setId(1l);
       	        Method getMethodObj = clazz.getMethod("getName");
       	        Method getMethodObj2 = clazz.getMethod("getId");
       	
       	        Method setMethodOfName = clazz.getMethod("setName", String.class);
       	        Method setMethodOfId = clazz.getMethod("setId", long.class);
       	
       	        Object getMethodValue = getMethodObj2.invoke(c2);
       	        Object getMethodValue2 = getMethodObj.invoke(c);
       	        System.out.println(getMethodValue);
       	        System.out.println(getMethodValue2);
       	
       	        Customer objectCopy = (Customer) clazz.getConstructor().newInstance();
       	        setMethodOfId.invoke(objectCopy, getMethodValue);
       	        System.out.println(objectCopy.getId());
       	    }
       	}
       	
       	class Customer {
       	
       	    private long id;
       	    private String name;
       	    private int age;
       	
       	
       	    public Customer() {
       	    }
       	
       	    public Customer(String name, int age) {
       	        this.name = name;
       	        this.age = age;
       	    }
       	
       	    public long getId() {
       	        return id;
       	    }
       	
       	    public void setId(long id) {
       	        this.id = id;
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
       	}
  ```

  ~~~java
   - Java refelction API for array(above is for class)
   
   - java.lang.Array 
   
   	- dynamically create and use array static methods
   
   	```java
   	public class Player {
   	    public static void main(String[] args) throws Exception {
   	        Class clazz = Class.forName("java.lang.String");
   	
   	        //use reflection to create an array new object, the length is 10
   	        Object array = Array.newInstance(clazz, 10);
   	        Array.set(array, 9, "world");
   	        String s = (String) Array.get(array, 9);
   	        System.out.println(s);
   	        System.out.println(Array.get(array, 0));
   	    }
   	}
   	```
   
   	Q: Search and tell difference of getMethod vs getDeclaredMethod?
   
   	- Break private restriction
   
   	```java
   	public class Player {
   	    public static void main(String[] args) throws Exception{
   	        Class clazz = Class.forName("Person");
   	        System.out.println(clazz);//which class is clazz?
   	        System.out.println("-------");
   	        Person p = new Person();
   	        System.out.println("p.name is "+p.getName());
   	        Field field = clazz.getDeclaredField("name");
   	        field.setAccessible(true);
   	        field.set(p, "xikai");
   	        System.out.println("p.name is "+p.getName());
   	//        field.set(Object,"xikai");
   	    }
   	}
   	
   	class Person {
   	    private String name = "xiong";
   	
   	    public String getName() {
   	        return name;
   	    }
   	}
   	```
  ~~~


  ​     	

5.  **Annotation**

  > Annotation can be read from source code (.java), byte code (.class) and runtime
  >
  > Regard it as app tool or library to affect app syntax

  ```java
  class Runner{
      private String name;
  
      @Override
      public String toString() { // rename the method to other names to test
          return "Runner{" +
                  "name='" + name + '\'' +
                  '}';
      }
  }
  ```

  ```java
  public class Player {
      @SuppressWarnings({"unchecked","deprecation"})
      public static void main(String[] args) {
          Map map = new TreeMap();
          map.put("date", new Date());
          System.out.println(map.get("date"));
          Date date = new Date();
          System.out.println(date.toLocaleString());
      }
  }
  ```

  - Self written Annotation

    - java.lang.annotation.Annotation  (extended by all annotation types) but itself is an interface not an annotation

    ```java
    @MyAnnotation
    public class Player {
    
        @MyAnnotation
        public static void main(String[] args) {
        }
    }
    
    @interface MyAnnotation {
    
    }
    ```

    ```java
    @MyAnnotation("must provide a string")
    public class Player {
    
        @MyAnnotation(value = "str")
        public static void main(String[] args) {
        }
    }
    
    @interface MyAnnotation {
        String value();  //value is special
    }
    ```

    ```java
    @MyAnnotation(value1 = "must provide a string")
    public class Player {
    
        @MyAnnotation(value1 = "str")
        public static void main(String[] args) {
        }
    }
    
    @interface MyAnnotation {
        String value1();
    }
    ```

    ```java
    @MyAnnotation(value = "must provide a string",value2 = Family.FATHER)
    public class Player {
    
        @MyAnnotation(value2 = Family.MOTHER)
        public static void main(String[] args) {
       
        }
    }
    
    @interface MyAnnotation {
        String value() default "if no str provided this str will be default";
    
        Family value2();
    }
    
    enum Family{
        FATHER,MOTHER;
    }
    ```

    - @Retention 

    	> tell compiler that this annotation information should be keep in byte code (.class) 
    	>
    	> JVM shall not read the information annotated by @Retention

    - Retention Policy

    	> {SOURCE  // compile finishes , then annotation done, compiler discards
    	>
    	> ​	—> check source code of @Retention
    	>
    	> ​	CLASS // annotation in .class  —> default
    	>
    	>    RUNTIME // annotation in .class, can be read by JVM
    	>
    	>    —> check @Deprecated
    	>
    	>   }

  - Reflection to read annotation

  	```java
  	@MyAnnotation(hello = "classLevel", world = "USA")
  	public class Player {
  	
  	
  	    @Deprecated
  	    @MyAnnotation(hello = "methodLevel", world = "Edison")
  	    public void playerMethod() {
  	        System.out.println("print anything");
  	    }
  	
  	    public static void main(String[] args) throws Exception {
  	        Player p = new Player();
  	//        p.playerMethod();
  	        Class clazz = Class.forName("Player");
  	        Method playerMethod = clazz.getMethod("playerMethod");
  	        System.out.println("here");
  	//        System.out.println(playerMethod.isAnnotationPresent(MyAnnotation.class));
  	        if (playerMethod.isAnnotationPresent(MyAnnotation.class)) {
  	            playerMethod.invoke(p);
  	        }
  	
  	        System.out.println(playerMethod.getName());
  	    }
  	
  	
  	}
  	
  	
  	@Retention(RetentionPolicy.RUNTIME) //change to other 2 policies to see the result
  	@interface MyAnnotation {
  	    String hello() default "Hello, I'm default";
  	
  	    String world();
  	}
  	```

  	- get annotation based on method

  	```java
  	@MyAnnotation(hello = "classLevel", world = "USA")
  	public class Player {
  	    @Deprecated
  	    @MyAnnotation(hello = "methodLevel", world = "Edison")
  	    public void playerMethod() {
  	        System.out.println("print anything");
  	    }
  	
  	    public static void main(String[] args) throws Exception {
  	        Player p = new Player();
  	//        p.playerMethod();
  	        Class clazz = Class.forName("Player");
  	        Method playerMethod = clazz.getMethod("playerMethod");
  	        System.out.println("here");
  	//        System.out.println(playerMethod.isAnnotationPresent(MyAnnotation.class));
  	        if (playerMethod.isAnnotationPresent(MyAnnotation.class)) {
  	            playerMethod.invoke(p);
  	        }
  	
  	        MyAnnotation myAnnotation = playerMethod.getAnnotation(MyAnnotation.class);
  	        System.out.println(myAnnotation);
  	        System.out.println(myAnnotation.hello());
  	        System.out.println(myAnnotation.world());
  	        System.out.println(playerMethod.getName());
  	    }
  	
  	
  	}
  	
  	
  	@Retention(RetentionPolicy.RUNTIME)
  	@interface MyAnnotation {
  	    String hello() default "Hello, I'm default";
  	
  	    String world();
  	}
  	```

  	- @Target

  	```java
  	@MyAnnotation(hello = "classLevel", world = "USA")
  	public class Player {
  	    @Deprecated
  	    @MyAnnotation(hello = "methodLevel", world = "Edison")
  	    @TargetTest//move this to class level to see
  	    public void playerMethod() {
  	        System.out.println("print anything");
  	    }
  	
  	
  	    public static void main(String[] args) throws Exception {
  	        Player p = new Player();
  	//        p.playerMethod();
  	        Class clazz = Class.forName("Algorithm.Player");
  	        Method playerMethod = clazz.getMethod("playerMethod");
  	        System.out.println("here");
  	//        System.out.println(playerMethod.isAnnotationPresent(MyAnnotation.class));
  	        if (playerMethod.isAnnotationPresent(MyAnnotation.class)) {
  	            playerMethod.invoke(p);
  	        }
  	
  	        MyAnnotation myAnnotation = playerMethod.getAnnotation(MyAnnotation.class);
  	        System.out.println(myAnnotation);
  	        System.out.println(myAnnotation.hello());
  	        System.out.println(myAnnotation.world());
  	        System.out.println(playerMethod.getName());
  	    }
  	
  	
  	}
  	
  	@Retention(RetentionPolicy.RUNTIME)
  	@interface MyAnnotation {
  	    String hello() default "Hello, I'm default";
  	
  	    String world();
  	}
  	
  	@Target(ElementType.METHOD)
  	@interface TargetTest{
  	    String value() default "can only used on method";
  	}
  	```

  	- @Documented —> seach online to check how to use, generate document to see the difference

  - By default, superclass annotation won't be inherited

  - @Inherited can make an annotation to be inherited 

6.  **jUnit**

	- add maven dependency
	- method must start with test, expalin why this method can run without main
	- unit test does not guarantee you are right(code right but not meet requirements) ,but make sure your codes are not wrong

	```java
	//junit 3
	public class Test extends TestCase {
	
	    @org.junit.Test
	    public static void testPrint() {
	        System.out.println("print");
	    }
	    
	}
	```

	```java
	//junit 4 and 5
	public class TestJunit {
	    @Test  // isAnnotationPresent to check, that's why newer version need not test as method name first word
	    public void printSysOut() {
	        System.out.println("print any thing");
	    }
	}
	```

	TDD 
	
	> Test Driven Development