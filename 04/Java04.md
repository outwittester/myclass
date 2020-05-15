# JavaSE

1. Collection

  - A Collection is a group of individual objects represented as a single unit. 
  - java.lang.Collection
  - When use each collection, seach its hierachy in SE library
  - Generic 
  	- compile checking to fix the type of a collection

2. **ArrayList**

  -  usage of java SE API (write a reference type and check if all the methods are working)

  	```java
  	public static void main(String[] args) {
  	        ArrayList<Integer> list = new ArrayList();
  	        for (int i = 0; i < 10; i++) {
  	            list.add(i);
  	        }
  	        for (int i = 0; i < list.size(); i++) {
  	            System.out.printf("current is %s", list.get(i));
  	            System.out.println();
  	        }
  	        list.remove(1);
  	        System.out.println("1 is "+list.get(1));
  	        System.out.println("----------------");
  	        for (int i = 0; i < list.size(); i++) {
  	            System.out.printf("current is %s", list.get(i));
  	            System.out.println();
  	        }
  	        list.clear();
  	        System.out.println(list.size());
  	    }
  	//try to delete first 5 elements in ArrayList see what's the result and think why
  	```

  - write your own arraylist 

  - ArrayList is storing the reference 

  - **very high cost on deletion and insertion as move all later elements ahead** but fast on get and set

  - **In Collection, Only objects can be stored** , not primitive data types ,Check with Set

  	```java
  	public class SelfArrayList {
  	    //ArrayList in root is array
  	    private Object[] elementData;
  	
  	    private int size;
  	
  	    public SelfArrayList() {
  	        this(10);
  	    }
  	
  	    public SelfArrayList(int initialCapacity) {
  	        if (initialCapacity < 0) {
  	            try {
  	                throw new Exception();
  	            } catch (Exception e) {
  	                e.printStackTrace();
  	            }
  	        }
  	        elementData = new Object[initialCapacity];
  	    }
  	
  	    public void add(Object obj) {
  	        // expand the capacity
  	        if (size == elementData.length) {
  	            Object[] newElementData = new Object[(size * 2) + 1];
  	            System.arraycopy(elementData, 0, newElementData, 0, elementData.length);
  	            elementData = newElementData;
  	        }
  	        // assign first then increase
  	        elementData[size++] = obj;
  	
  	    }
  	
  	
  	    public int getsize() {
  	        return size;
  	    }
  	
  	    public Object get(int index) {
  	        rangeCheck(index);
  	        return elementData[index];
  	    }
  	
  	    public void remove(int index) {
  	        // a b c d e delete one，consecutive elements shoud be put one position ahead
  	        rangeCheck(index);
  	        int numMoved = size - index - 1;
  	        if (numMoved > 0)
  	            System.arraycopy(elementData, index + 1, elementData, index, numMoved);
  	        elementData[--size] = null; //last position becomes null
  	    }
  	
  	    public void remove(Object o){
  	        for(int i=0;i<size;i++){
  	            if(get(i).equals(o)){
  	                remove(i);
  	            }
  	        }
  	    }
  	
  	    public Object set(int index,Object obj){
  	        rangeCheck(index);
  	        Object oldValue = elementData[index];
  	        elementData[index] = obj;
  	        return oldValue;
  	    }
  	
  	    private void rangeCheck(int index) {
  	        if (index >= size)
  	            throw new IndexOutOfBoundsException();
  	    }
  	
  	    public static void main(String[] args) {
  	        SelfArrayList list = new SelfArrayList(3);
  	        list.add("aaa");
  	        list.add("aab");
  	        list.add("aac");
  	        list.add("aad");
  	        list.add("aae");
  	        list.add("aaf");
  	
  	        System.out.println(list.get(2));
  	        list.set(2, "www");
  	        System.out.println(list.get(2));
  	        System.out.println(list.getsize());
  	    }
  	}
  	
  	```

  - LinkedList

  	- only one first element
  	- only one last element
  	- every element has one previous element but first one
  	- every element has one subsequent element but last one
  	- **fast on deletion and insertion but slow on get and set**
  	
```java
  	public class Node {
  		private Node previous;
  	
  		private Object obj;
  	
  		private Node next;
  	
  		public Node() {
  	
  		}
  	
  		public Node(Node previous, Object obj, Node next) {
  			super();
  				    this.previous = previous;
  			    this.obj = obj;
  			    this.next = next;
  		}
  	
  		public Node getPrevious() {
  			    return previous;
  		}
  	
  		public void setPrevious(Node previous) {
  			    this.previous = previous;
  		}
  	
  		public Object getObj() {
  			    return obj;
  		}
  	
  		public void setObj(Object obj) {
  			    this.obj = obj;
  		}
  	
  		public Node getNext() {
  	    		return next;
  		}
  	
  		public void setNext(Node next) {
  			    this.next = next;
  		}
  	
  	}
  	
  	
  	
  	public class SelfLinkedList {
  	    private Node first;
  	    private Node last;
  	
  	    private int size;
  	
  	    public void add(Object obj) {
  	        Node n = new Node();
  	        if (first == null) {
  	            n.setPrevious(null);
  	            n.setObj(obj);
  	            n.setNext(null);
  	            last = first = n;
  	        } else {
  	            n.setPrevious(last);
  	            n.setObj(obj);
  	            n.setNext(null);
  	            last.setNext(n);
  	            last = n;
  	        }
  	        size++;
  	    }
  	
  	    public int size() {
  	        return size;
  	    }
  	
  	    public Object get(int index) {
  	        rangeCheck(index);
  	        Node temp = null;
  	        if (first != null) {
  	            temp = first;
  	            for (int i = 0; i < index; i++) {
  	                temp = temp.next;
  	            }
  	
  	        }
  	        return temp.obj;
  	    }
  	
  	    public void remove(int index) {
  	        Node temp = null;
  	        if (first != null) {
  	            temp = first;
  	            for (int i = 0; i < index; i++) {
  	                temp = temp.next;
  	            }
  	
  	        }
  	        if (temp != null) {
  	            Node pre = temp.previous;
  	            Node next = temp.next;
  	            pre.next = next;
  	            next.previous = pre;
  	            size--;
  	        }
  	
  	    }
  	
  	    public void rangeCheck(int index) {
  	        if (index >= size) {
  	            try {
  	                throw new Exception();
  	            } catch (Exception e) {
  	                e.printStackTrace();
  	            }
  	
  	        }
  	    }
  	
  	    public void add(int index, Object obj) {
  	        rangeCheck(index);
  	        Node temp = null;
  	        if (first != null) {
  	            temp = first;
  	            for (int i = 0; i < index; i++) {
  	                temp = temp.next;
  	            }
  	
  	        }
  	        Node newNode = new Node();
  	        newNode.obj = obj;
  	        if (temp != null) {
  	            Node pre = temp.previous;
  	            pre.next = newNode;
  	            newNode.previous = pre;
  	
  	            newNode.next = temp;
  	            temp.previous = newNode;
  	        }
  	        size++;
  	    }
  	
  	    public static void main(String[] args) {
  	
  	        SelfLinkedList list = new SelfLinkedList();
  	        list.add("aaa");
  	        list.add("bbb");
  	        list.add(1, "BBB");
  	        list.add("ccc");
  	
  	        System.out.println(list.size);
  	        System.out.println(list.get(0));
  	        System.out.println(list.get(1));
  	        System.out.println(list.get(2));
  	        System.out.println(list.get(3));
  	        list.remove(1);
  	        System.out.println(list.size);
  	        System.out.println(list.get(0));
  	        System.out.println(list.get(1));
  	    }
  	}
  	```
  
3. Use LinkedList to implement Stack and Queue —> means one is using SE Library to implement your own data structure. (SE already has Stack and Queue, search and read doc and know how to use it)

4.  **Set**

  - no order
  - no duplicate element
  - **HashSet** is Implemented using a hash table. Elements are not ordered. The add, remove, and contains methods have constant time **complexity O(1)**

  ```java
  public class Player {
      public static void main(String[] args) {
          HashSet set = new HashSet();
          set.add("a");
          set.add("b");
          set.add("c");
          set.add("d");
          set.add("a"); // String as we know is a new object here, though still regard as duplicate in Set which won't be added
          System.out.println(set);
          System.out.println(set.isEmpty());
          System.out.println(set.size());
          set.remove("b");
          System.out.println(set);
          System.out.println(set.contains("d"));
          System.out.println(set);
      }
  }
  ```

  - **More on Object class equals method**

  ```markdown
  
  	If the Set already contains the element, the call leaves the set unchanged and return false. Adds the specified element e to the set if this set contains no element e2 such that (e==null ? e2==null : e.equals(e2))
  
  For any non-null reference it has below properties -->
  -reflexive: x.equals(x) return true
  -symmetric: x.equals(y) should return true only if y.equals(x) returns true
  -transitive: if x.equals(y) return true and y.equals(z) returns true, then x.equals(z) should return true
  -consistent: multiple invocations of x.equals(y) consistently return true or consistently return false, provided no information used in equals comparisions on the objects is modified.
  -x.equals(null) returns false
  Object equals non-null reference values x and y returns true if and only if x and y refers to the same object (x==y has the value true)
  
  **when override equals method, hashcode() method must be override too**  !!!
  
  
  ```

  - public int hashcode() —> returns a hash code value for the object

  - this method is supported for the benefit of hashtables and hashmaps such as those provided by java.util.hashtable 

  	> 1. `Hashtable` is [synchronized](https://stackoverflow.com/questions/1085709/what-does-synchronized-mean), whereas `HashMap` is not. This makes `HashMap` better for non-threaded applications, as unsynchronized Objects typically perform better than synchronized ones.
  	> 2. `Hashtable` does not allow `null` keys or values. `HashMap` allows one `null` key and any number of `null` values.

  - Seach and read hashcode method doc

  	- find the contract of hashCode and understand 
  		- in one execution of java app hashcode return the same integer 
  			- need not remain consistent from another execution of the same application
  		- obj1.equals(obj2) returns true then they have to have the same hashcode integer value 
  		- !obj1.equals(obj2) not required the two objects have the same hashcode integer value
  		- BUT Developer should be aware that producing the distinct integer results for unequal objects may improve the performance of hashtables

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        List<String> list = Arrays.asList("pollinating sandboxes",
  	                "amusement & hemophilias",
  	                "schoolworks = perversive",
  	                "electrolysissweeteners.net",
  	                "constitutionalunstableness.net",
  	                "grinnerslaphappier.org",
  	                "BLEACHINGFEMININELY.NET",
  	                "WWW.BUMRACEGOERS.ORG",
  	                "WWW.RACCOONPRUDENTIALS.NET",
  	                "Microcomputers: the unredeemed lollipop...",
  	                "Incentively, my dear, I don't tessellate a derangement.",
  	                "A person who never yodelled an apology, never preened vocalizing transsexuals.");
  	        for (String s : list) {
  	            System.out.println(s.hashCode());
  	        }
  	    }
  	}
  	```

  	- For Java Object class, hashCode method defined by class Object does return distinct integers for distinct objects. But not required by Java Language itself.

  	- Means only objects of Object class hashcode method **represent** their address

  		```java
  		Integer.toHexString(hashCode());
  		//which converting the internal address of the object into an integer
  		```

  		Q: Why override equals method must override hashcode when using Collection?

  		- for implementation when using Collection, override one must override the other one
  		- if you are very clear that your class won't be able to used in collection,you can only just override equals

  	- **When comparing objects in HashSet,HashTable,HashMap(hash Collection), hashcode method is called, if false, then add the new element, if true, then check equals method, if true (means one same element already added),otherwise, add the new element** 

  	- Q: Why check hashcode first not equals directly?

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        String s1 = new String("a");
  		        String s2 = new String("a");
  		
  		        System.out.println(s1.hashCode());
  		        System.out.println(s2.hashCode());
  		    }
  		}
  		```

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        HashSet set = new HashSet();
  		        Developer d1 = new Developer("Java");
  		        Developer d2 = new Developer("Java");
  		
  		        set.add(d1);
  		        set.add(d2);
  		        System.out.println(set);
  		    }
  		}
  		
  		class Developer{
  		    private String name;
  		
  		    public Developer(String name) {
  		        this.name = name;
  		    }
  		
  		
  		    //override the hashcode based on the String hashcode itself is enough
  		    @Override
  		    public int hashCode() {
  		        return this.name.hashCode();
  		    }
  		
  		    @Override
  		    public boolean equals(Object obj) {
  		        if (this == obj) {
  		            return true;
  		        }
  		        if (null != obj && obj instanceof Developer) {
  		            Developer d = (Developer) obj;
  		            if (name.equals(d.name)) {
  		                return true;
  		            }
  		        }
  		        return false;
  		    }
  		}
  		```
  		
- Use IDE generate methods
  	
	```java
  		public class Player {
  		
  		    public static void main(String[] args) {
  		        HashSet set = new HashSet();
  		        Developer d1 = new Developer("Java");
  		        Developer d2 = new Developer("Java");
  		
  		        set.add(d1);
  		        set.add(d2);
  		        System.out.println(set);
  		
  		        //how to get Name of the developer, show
  		        Iterator i = set.iterator();
  		        Developer developer = (Developer) i.next();
  		
  		    }
  		}
  		
  		class Developer{
  		    private String name;
  		
  		    public Developer(String name) {
  		        this.name = name;
  		    }
  		
  		
  		    //override the hashcode based on the String hashcode itself is enough
  		    @Override
  		    public int hashCode() {
  		        return this.name.hashCode();
  		    }
  		
  		    @Override
  		    public boolean equals(Object obj) {
  		        if (this == obj) {
  		            return true;
  		        }
  		        if (null != obj && obj instanceof Developer) {
  		            Developer d = (Developer) obj;
  		            if (name.equals(d.name)) {
  		                return true;
  		            }
  		        }
  		        return false;
  		    }
  		}
  ```
  
	```java
  		public class Player {
  		
  		    public static void main(String[] args) {
  		        HashSet set = new HashSet();
  		        Developer d1 = new Developer("Java");
  		        Developer d2 = new Developer("Java");
  		
  		        set.add(d1);
  		        set.add(d2);
  		        System.out.println(set);
  		
  		        //how to get Name of the developer, show
  		        Iterator i = set.iterator();
  		        Developer developer = (Developer) i.next();
  		
  		    }
  		}
  		
  		class Developer{
  		    private String name;
  		
  		    public Developer(String name) {
  		        this.name = name;
  		    }
  		
  		
  		    //override the hashcode based on the String hashcode itself is enough
  		    @Override
  		    public int hashCode() {
  		        return this.name.hashCode();
  		    }
  		
  		    @Override
  		    public boolean equals(Object obj) {
  		        if (this == obj) {
  		            return true;
  		        }
  		        if (null != obj && obj instanceof Developer) {
  		            Developer d = (Developer) obj;
  		            if (name.equals(d.name)) {
  		                return true;
  		            }
  		        }
  		        return false;
  		    }
  		}
  ```
  
5. **Iterator** —> java.util.Iterator

  - Returns an itrator over the elements in Collection

  - Every Collection provides an iterator

  - iterator() fetch one element a time, use hasNext() and next() to loop over

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        HashSet set = new HashSet();
  	        set.add("A");
  	        set.add("B");
  	        set.add("C");
  	        set.add("D");
  	        set.add("E");
  	        Iterator i = set.iterator();
  	
  	        while (i.hasNext()) {
  	            String current = (String) i.next();
  	            System.out.println("current is "+current);
  	        }
  	   		     //think why?
  	        System.out.println(i.hasNext());
  	        System.out.println(i.next());
  	   		     //why above show no more elements, and below can still loop over
  	        for (Iterator i2 = set.iterator(); i2.hasNext(); ) {
  	            String current = (String) i2.next();
  	            System.out.println(current);
  	        }
  	    }
  	}
  	```

6.  **TreeSet**

  - ordered
  - **TreeSet** is implemented using a tree structure(red-black tree in algorithm book). The elements in a set are sorted, but the add, remove, and contains methods has time **complexity O(log (n)**). It offers several methods to deal with the ordered set like `first(), last(), headSet(), tailSet()`, etc.

  ```java
  public class Player {
      public static void main(String[] args) {
          TreeSet set = new TreeSet();
          set.add("M");
          set.add("O");
          set.add("N");
          set.add("E");
          set.add("Y");
          System.out.println(set);
      }
  }
  ```

  - order maters, TreeSet sorted
  - every new element must be compared before adding

  ```java
  public class Player {
      public static void main(String[] args) {
          TreeSet set = new TreeSet();
          set.add(new Car(4000));
          set.add(new Car(2000));
          set.add(new Car(3000));
          set.add(new Car(1000));
          
          System.out.println(set);
      }
  }
  
  class Car{
      int price;
  
      public Car(int price) {
          this.price = price;
      }
  
      @Override
      public String toString() {
          return "price of this car is "+this.price;
      }
  }
  ```

  - Once implement comparator, no need to override equals

  - if very clear, you may override equals to improve the performance

  	- Comparable      --> paractice LeetCode 451

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        TreeSet set = new TreeSet();
  		        set.add(new Car(4000));
  		        set.add(new Car(2000));
  		        set.add(new Car(3000));
  		        set.add(new Car(1000));
  		
  		        System.out.println(set);
  		    }
  		}
  		
  		class Car implements Comparable<Car>{
  		    int price;
  		
  		    public Car(int price) {
  		        this.price = price;
  		    }
  		
  		    @Override
  		    public String toString() {
  		        return "price of this car is "+this.price;
  		    }
  		
  		    @Override
  		    public int compareTo(Car o) {
  		        System.out.println("coming price is "+o.price);
  		        return this.price-o.price;
  		    }
  		}
  		```

  		

  	- Comparator  (Strategy Design pattern)

  		> in most real-life scenarios, we want sorting based on different parameters. For example, as a CEO, I would like to sort the employees based on Salary, an HR would like to sort them based on age. This is the situation where we need to use **Java Comparator** interface because *Comparable.compareTo(Object o)*method implementation can provide default sorting and we can’t change it dynamically. Whereas with Comparator, we can define multiple methods with different ways of sorting and then chose the sorting method based on our requirements.

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        TreeSet set = new TreeSet(new CarAgeComparator());
  		        set.add(new Car(4000, 10));
  		        set.add(new Car(2000, 5));
  		        set.add(new Car(3000, 20));
  		        set.add(new Car(1000, 0));
  		
  		        System.out.println(set);
  		    }
  		}
  		
  		class Car implements Comparable<Car> {
  		    int price;
  		    int age;
  		
  		    public Car(int price) {
  		        this.price = price;
  		    }
  		
  		    public Car(int price, int age) {
  		        this.price = price;
  		        this.age = age;
  		    }
  		
  		    @Override
  		    public String toString() {
  		        return "Car{" +
  		                "price=" + price +
  		                ", age=" + age +
  		                '}';
  		    }
  		
  		    @Override
  		    public int compareTo(Car o) {
  		        return this.price - o.price;
  		    }
  		}
  		
  		class CarAgeComparator implements Comparator<Car> {
  		    @Override
  		    public int compare(Car o1, Car o2) {
  		        return o1.age - o2.age;
  		    }
  		}
  		```

  		Q: What's the difference between Set(HashSet) and TreeSet?

  		Check **Collections** API

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        LinkedList list = new LinkedList();
  		        list.add(3);
  		        list.add(1);
  		        list.add(4);
  		        list.add(1);
  		        list.add(5);
  		        list.add(9);
  		        list.add(2);
  		        list.add(7);
  		        System.out.println(list);
  		        Collections.sort(list);
  		        System.out.println(list);
  		        Collections.reverse(list);
  		        System.out.println(list);
  		        Comparator c = Collections.reverseOrder();
  		        Collections.sort(list, c);
  		        System.out.println(list);
  		        Collections.shuffle(list);
  		        System.out.println(list);
  		        System.out.println(Collections.min(list));
  		        System.out.println(Collections.max(list));
  		    }
  		}
  		```

  		

7. **Map**

  > The **Map** Interface. A **Map** is an object that maps keys to values. A **map** cannot contain duplicate keys: Each key can **map** to at most one value. It models the mathematical function abstraction. ... The **Java** platform contains three general-purpose **Map** implementations: **HashMap** , TreeMap , and LinkedHashMap
  >
  > - no order 
  > - O(1) time complexity for get and ContainsKey
  > - keys can't be duplicate, values can. So values return collection

  ```java
  public class Player {
      public static void main(String[] args) {
          HashMap map = new HashMap();
          map.put(1, "a");
          map.put(2, "b");
          map.put(3, "c");
          map.put(4, "d");
          System.out.println(map);
  
          Set keys = map.keySet();
          System.out.println(keys);
  
          Collection values =  map.values();
          System.out.println(values);
      }
  }
  ```

  - Seach online for all mentioned collections time complexity, think and remember

  - Collections used in this file are frequently from SE, Be sure know how to use them and understand

  - Above Collections are provided by SE but in real life, they all may not meet our needs, so we need to find some third parties API to use. 

  - Manager is telling you your company is going to use guava maps, seach them and learn on yourself.

    - use HashMap to count each letter in input

    	```java
    	public class Player {
    	    public static void main(String[] args) {
    	        String[] input = {"a", "a", "b", "c", "b", "a"};
    	        HashMap map = new HashMap();
    	        for (String each : input) {
    	            if (map.get(each) == null) {
    	                int currentCount = 1;
    	                map.put(each, currentCount);
    	            }else{
    	                int currentCount = (Integer) map.get(each);
    	                map.put(each, ++currentCount);
    	            }
    	        }
    	
    	        System.out.println(map);
    	    }
    	}
    	```

    	

    - Loop map  —> change definition by Polymorphism

    	```java
    	public class Player {
    	    public static void main(String[] args) {
    	        Map<Integer, String> map = new HashMap<>();
    	        map.put(1, "a");
    	        map.put(2, "b");
    	        map.put(3, "c");
    	        map.put(4, "d");
    	        map.put(5, "e");
    	
    	        Set<Map.Entry<Integer, String>> set = map.entrySet();
    	
    	        for (Iterator<Map.Entry<Integer, String>> it = set.iterator(); it.hasNext(); ) {
    	            Map.Entry<Integer, String> eachEntry = it.next();
    	            System.out.println(eachEntry);
    	            Integer key = eachEntry.getKey();
    	            String value = eachEntry.getValue();
    	            System.out.println("current key is " + key);
    	            System.out.println("current value is " + value);
    	        }
    	    }
    	}
    	```

    	```java
    	public class Player {
    	    public static void main(String[] args) {
    	        Map<Integer, String> map = new HashMap<>();
    	        map.put(1, "a");
    	        map.put(2, "b");
    	        map.put(3, "c");
    	        map.put(4, "d");
    	        map.put(5, "e");
    	
    	        Set keys = map.keySet();
    	
    	        Iterator it = keys.iterator();
    	
    	        while (it.hasNext()) {
    	            int key = (int) it.next();
    	            String value = map.get(key);
    	            System.out.println(key+" = "+value);
    	        }
    	
    	    }
    	}
    	```

    	- EntrySet is Inner Class of Map and is more object oriented

    - Read HashSet and HashMap Source Code

    - Q: Tell me your understanding of HashSet and HashMap?

    	———Bonus understanding

    	```java
    	public class Player {
    	    public static void main(String[] args) {
    	   	//Properites are used for reading files configuration such as xml...
    	   //below is reading system properties 
    	        Properties p = System.getProperties();
    	        Set keySet = p.keySet();
    	        Iterator it = keySet.iterator();
    	        while (it.hasNext()) {
    	            String key = (String) it.next();
    	       				     //getObject is ok but need downcasting
    	            String value = p.getProperty(key);
    	            System.out.println(key + " = " + value);
    	        }
    	    }
    	}
    	```

  - Practice: input is  word = "…"  —> output :  [Node1, Node2]
  
  	```java
  	public class Test {
  	    public static void main(String[] args) throws IOException {
  	        String word = "<Order> <OrderLine Node=”Node1″ Quantity=”10″ /> <OrderLine Node=”Node1″ Quantity=”20″ /> <OrderLine Node=”Node2″ Quantity=”10″ /> </Order>";
  	        System.out.println(word);
  	        word = word.replaceAll("″", "");
  	        word = word.replaceAll("”","");
  	        String[] splits = word.split(" ");
  	        Set result = new HashSet();
  	        for (String each : splits) {
  	            if (each.startsWith("Node=")) {
  	                result.add(each.substring(5));
  	            }
  	        }
  	        System.out.println(word);
  	//        String word = "<Order> <OrderLine Node=”Node1″ Quantity=”10″ /> <OrderLine Node=”Node1″ Quantity=”20″ /> <OrderLine Node=”Node2″ Quantity=”10″ /> </Order>";
  	
  	//        for (int index = word.indexOf("Node="); index >= 0; index = word.indexOf("Node=", index + 1)) {
  	//            result.add(word.substring(index + 6, index + 11));
  	//        }
  	        System.out.println(result);
  	        InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
  	        BufferedReader in = new BufferedReader(reader);
  	        String line;
  	        while ((line = in.readLine()) != null) {
  	            System.out.println(line);
  	        }
  	
  	
  	    }
  	```
  
  	
