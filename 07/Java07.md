1. **Thread**

  - What is thread?

  	-  Thread is an independent running stream, it can't be run on its own, rely on an app

  	-  Process (app) has its own independent state and data, threads share the same memory and resource, may influence each other. 

  	-  Thread data often store in temp storage or the app's stack and heap, switch from one thread to another is much less costing comparing with process

  	-  In java, if we don't create thread on our own, OS will generate one for us which is main()

  	- only start method can invoke thread to run

  		For CPU one time can only run one thread, but fast enough for human to regard as multi-run

  		Real multi-programming is multiple physical core

  - Life circle of thread

  	- New
  	- Runnable stage:start() method to begin (ready to run cause CPU not allocated yet) 
  	- Running stage:run() method to execute (after fetch CPU resource)
  	- Blocked stage:thread is dealing with I/O (if it contains such code)
  	- Runnable stage again 
  	- Running stage( this stage may go back to Runnable stage,OS won't let one all the time) 
  	- run() to the end
  		- no method such as stop() to kill a thread, only let run() method goes end
  	- Sleep() ,wait() ,I/O will blocked thread to run
  	- end of Sleep(),notify() and notifyAll() and end of I/O will let thread back to run

  - How to implement thread ?

  	- extends Thread

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        MyThread t1 = new MyThread();
  		        t1.start();
  		    }
  		}
  		
  		class MyThread extends Thread {
  		
  		    @Override
  		    public void run() {
  		        for (int i = 0; i < 100; i++) {
  		            System.out.println("another thread "+i);
  		        }
  		    }
  		}
  		```

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        MyThread1 t1 = new MyThread1();
  		        t1.start();  // change both start to run and see the difference, think why?
  		        MyThread2 t2 = new MyThread2();
  		        t2.start();
  		    }
  		}
  		
  		class MyThread1 extends Thread {
  		    @Override
  		    public void run() {
  		        for (int i = 0; i < 100; i++) {
  		            System.out.println("thread1 "+i);
  		        }
  		    }
  		}
  		class MyThread2 extends Thread{
  		    @Override
  		    public void run() {
  		        for (int i = 0; i < 100; i++) {
  		            System.out.println("thread2 "+i);
  		        }
  		    }
  		}
  		```

  	- implements Runnable

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        Thread t1 = new Thread(new MyThread());
  		        t1.start();
  		    }
  		}
  		
  		class MyThread implements Runnable {
  		
  		    @Override
  		    public void run() {
  		        for (int i = 0; i < 100; i++) {
  		            System.out.println("mythread " + i);
  		        }
  		    }
  		}
  		```

  	- use Annomynous class

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        Thread t1 = new Thread(new Runnable(){
  		            @Override
  		            public void run() {
  		                for (int i = 0; i < 100; i++) {
  		                    System.out.println("mythread " + i);
  		                }
  		            }
  		        });
  		        t1.start();
  		    }
  		}
  		```

  	- use lambda

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        Thread t1 = new Thread(() -> {
  		            for (int i = 0; i < 100; i++) {
  		                System.out.println("mythread " + i);
  		            }
  		        });
  		        t1.start();
  		    }
  		}
  		```

  	- Relationship of using Thread and Runnable

  		-  Thread implement Runnable too, thus has Runnable run() method (native method call OS)
  		-  Thread name can be initialized and share by all thread objects.  (Read thread doc)
  		-  When use extends, you have to override run method cause the default method is empty while use Runnable, the implementation is realized inside the implemented class, when create new thread for that class to run is calling the implemented class run() method
  		-  Choose Runnable is better as it's loose couple your code (Recommendation), as java can only extends one class but multiple implementation

  - priority of thread(this is not guarantee,OS determine)

  	- 1 to 10  MIN_PRIORITY(10) - NORM_PRIORITY(5) - MIN_PRIORITY(1)
  	- OS will rise the priority of long-waiting thread to aoivd low priority thread getting no chance
  	- yield() will yield CPU
  	- sleep() causes thread to sleep
  	- I/O operation will block thread
  	- higher priority will take CPU

  	```java
  	public class Player extends Thread {
  	    public void run() {
  	        System.out.println("running...");
  	    }
  	
  	    public static void main(String args[]) {
  	        // creating one thread
  	        Player t1 = new Player();
  	        Player t2 = new Player();
  	        // set the priority
  	        t1.setPriority(4);
  	        t2.setPriority(7);
  	        System.out.println("Priority of thread t1 is: " + t1.getPriority()); //4
  	        System.out.println("Priority of thread t2 is: " + t2.getPriority()); //7
  	        t1.start();
  	    }
  	}
  	```

  	- custom stop thread
  	- since 1.2 stop() method of thread deprecated as it's a failure

  	```java
  	public class Player {
  	    private MyThread mt = new MyThread();
  	    private Thread t = new Thread(mt);
  	
  	    public static void main(String[] args) {
  	        Player p = new Player();
  	        p.t.start();
  	        System.out.println("do something");
  	        p.mt.stopRunning();
  	    }
  	}
  	
  	class MyThread implements Runnable {
  	
  	    private boolean flag = true;
  	
  	    @Override
  	    public void run() {
  	        while (flag) {
  	            System.out.println("running");
  	        }
  	    }
  	    public void stopRunning() {
  	        flag = false;
  	    }
  	}
  	```

  	

  - multi-thread synchronization

  	- When an app need multiple block of codes to run the same, then need multi-threads
  	- multi-thread program is to make the most use of CPU, when a thread running only deal with I/O and no need to take possession of CPU, then release it for other threads take CPU resource
  	- Multi-thread share class variable

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        Runnable r = new MyThread();
  	        Thread thread1 = new Thread(r);
  	        Thread thread2 = new Thread(r);
  	        System.out.println(thread1.getName());
  	        System.out.println(thread2.getName());
  	        thread1.start();
  	        thread2.start();
  	    }
  	}
  	
  	class MyThread implements Runnable {
  	    int i;
  	
  	    @Override
  	    public void run() {
  	        while (true) {
  	            System.out.println("i is " + i++);
  	            try {
  	                Thread.sleep((long) (Math.random() * 1000));
  	            } catch (InterruptedException e) {
  	                e.printStackTrace();
  	            }
  	            if(20==i){
  	                System.out.println("i is "+i +" to stop");
  	                break;
  	            }
  	        }
  	    }
  	}
  	```

  	- Multi-thread with local variable

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        Runnable r = new MyThread();
  	        Thread thread1 = new Thread(r);
  	        Thread thread2 = new Thread(r);
  	        System.out.println(thread1.getName());
  	        System.out.println(thread2.getName());
  	        thread1.start();
  	        thread2.start();
  	    }
  	}
  	
  	class MyThread implements Runnable {
  	
  	    @Override
  	    public void run() {
  	        int i=0;
  	        while (true) {
  	            System.out.println("i is " + i++);
  	            try {
  	                Thread.sleep((long) (Math.random() * 1000));
  	            } catch (InterruptedException e) {
  	                e.printStackTrace();
  	            }
  	            if(20==i){
  	                System.out.println("i is "+i +" to stop");
  	                break;
  	            }
  	        }
  	    }
  	}
  	```

  	- guess the result below

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        Runnable r = new MyThread();
  	        Thread thread1 = new Thread(r);
  	        r =new MyThread();
  	        Thread thread2 = new Thread(r);
  	        thread1.start();
  	        thread2.start();
  	    }
  	}
  	
  	class MyThread implements Runnable {
  	    int i=0;
  	    @Override
  	    public void run() {
  	
  	        while (true) {
  	            System.out.println("i is " + i++);
  	            try {
  	                Thread.sleep((long) (Math.random() * 1000));
  	            } catch (InterruptedException e) {
  	                e.printStackTrace();
  	            }
  	            if(20==i){
  	                System.out.println("i is "+i +" to stop");
  	                break;
  	            }
  	        }
  	    }
  	
  	}
  	```

  - **synchronized**

  	- After multi-thread start, developer loses the control of thread and conflicts may happen

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        MyThread t1 = new MyThread();
  	        t1.start();
  	        System.out.println("final sum is "+t1.getSum()); 
  	        //main and MyThread are racing the CPU resource to run,the sum could be any result, run multiple times of this app and check the result
  	    }
  	}
  	
  	class MyThread extends Thread {
  	    private int sum;
  	
  	    public int getSum() {
  	        return sum;
  	    }
  	    @Override
  	    public void run() {
  	        for (int i = 0; i < 100; i++) {
  	            System.out.println("another thread "+i);
  	            sum+=i;
  	            System.out.println("current sum is "+sum);
  	        }
  	    }
  	}
  	```

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        BankAccount bankAccount = new BankAccount();
  	        Thread t1 = new DrawTread(bankAccount);
  	   			     // bankAccount = new BankAccount();
  	        Thread t2 = new DrawTread(bankAccount);
  	        t1.start();
  	        t2.start();
  	    }
  	}
  	class BankAccount {
  	    private int money = 100; //add static to test
  	    public int drawMoney(int draw) {
  	        if (draw < 0) {
  	            return -1;
  	        } else if (draw > money) {
  	            return -2;
  	        } else if (money < 0) {
  	            return -3;
  	        } else {
  	            try {
  	                Thread.sleep(1000);
  	            } catch (InterruptedException e) {
  	                e.printStackTrace();
  	            }
  	            money -= draw;
  	            System.out.println("money in account "+money);
  	            return draw;
  	        }
  	    }
  	}
  	
  	class DrawTread extends Thread {
  	    private BankAccount bankAccount;
  	
  	    public DrawTread(BankAccount bankAccount) {
  	        this.bankAccount = bankAccount;
  	    }
  	
  	    @Override
  	    public void run() {
  	        System.out.println(bankAccount.drawMoney(100));
  	    }
  	}
  	```

  	- use synchronized to solve

  	```java
  	public class Player {
  	    public static void main(String[] args) {
  	        BankAccount bankAccount = new BankAccount();
  	        Thread t1 = new DrawTread(bankAccount);
  	        Thread t2 = new DrawTread(bankAccount);
  	        t1.start();
  	        t2.start();
  	    }
  	}
  	
  	class BankAccount {
  	    private int money = 100; //add static to test
  	
  	    public synchronized int drawMoney(int draw) {
  	        if (draw < 0) {
  	            return -1;
  	        } else if (draw > money) {
  	            return -2;
  	        } else if (money < 0) {
  	            return -3;
  	        } else {
  	            try {
  	                Thread.sleep(1000);// imitate latency of ATM
  	            } catch (InterruptedException e) {
  	                e.printStackTrace();
  	            }
  	            money -= draw;
  	            System.out.println("money in account "+money);
  	            return draw;
  	        }
  	    }
  	}
  	
  	class DrawTread extends Thread {
  	    private BankAccount bankAccount;
  	
  	    public DrawTread(BankAccount bankAccount) {
  	        this.bankAccount = bankAccount;
  	    }
  	
  	    @Override
  	    public void run() {
  	        System.out.println("I draw "+bankAccount.drawMoney(100)); //change number to test
  	    }
  	}
  	```

  	-  Java has lock called monitor for every object

  	- when calling a synchronized method means lock that object where other thread can't use synchronized method during the lock stage. Other thread can use after the lock is released or throws out exception.

  	- when an object has multiple synchronized methods, once the object is executing one of them, other thread can't invoke either of the synchronized methods.

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        Example example = new Example();
  		        Thread t1 = new TheThread1(example);
  		   		     //example = new Example() // uncomment to run and think the diff
  		        Thread t2 = new TheThread2(example);
  		
  		        t1.start();
  		        t2.start();
  		    }
  		}
  		
  		class Example {
  		    public synchronized void execute1() {
  		        for (int i = 0; i < 20; i++) {
  		            try {
  		                Thread.sleep((long) (Math.random() * 1000));
  		            } catch (InterruptedException e) {
  		                e.printStackTrace();
  		            }
  		            System.out.println("hello: " + i);
  		        }
  		    }
  		
  		    public synchronized void execute2() {
  		        for (int i = 0; i < 20; i++) {
  		            try {
  		                Thread.sleep((long) (Math.random() * 1000));
  		            } catch (InterruptedException e) {
  		                e.printStackTrace();
  		            }
  		            System.out.println("world: " + i);
  		        }
  		    }
  		}
  		
  		
  		class TheThread1 extends Thread {
  		
  		    private Example example;
  		
  		    public TheThread1(Example example) {
  		        this.example = example;
  		    }
  		
  		    @Override
  		    public void run() {
  		        this.example.execute1();
  		    }
  		}
  		
  		class TheThread2 extends Thread {
  		
  		    private Example example;
  		
  		    public TheThread2(Example example) {
  		        this.example = example;
  		    }
  		
  		    @Override
  		    public void run() {
  		        this.example.execute2();
  		    }
  		}
  		```

  	- If one synchronized method is static, the locking object becomes the object's Class object(static belongs to class level), one static method and one non-static method, the synchronized will fail cause the two methods are locking two different objects (think about reflection, no matter how many objects one class it generates, all these objects only reflect to one class). Thus when threads are calling two static , synchronized methods, they are going to execute in order, one ends then starts another. 

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        Example example = new Example();
  		
  		        Thread t1 = new TheThread1(example);
  		        Thread t2 = new TheThread2(example);
  		        t1.start();
  		        t2.start();
  		    }
  		}
  		
  		class Example {
  				    //without static is locking the calling object
  		    //add static to test again 
  		    public synchronized void execute1() {
  		        for (int i = 0; i < 20; i++) {
  		            try {
  		                Thread.sleep((long) (Math.random() * 1000));
  		            } catch (InterruptedException e) {
  		                e.printStackTrace();
  		            }
  		            System.out.println("hello: " + i);
  		        }
  		    }
  		    // this is locking the Example class
  		    public synchronized static void execute2() {
  		        for (int i = 0; i < 20; i++) {
  		            try {
  		                Thread.sleep((long) (Math.random() * 1000));
  		            } catch (InterruptedException e) {
  		                e.printStackTrace();
  		            }
  		            System.out.println("world: " + i);
  		        }
  		    }
  		}
  		
  		
  		class TheThread1 extends Thread {
  		
  		    private Example example;
  		
  		    public TheThread1(Example example) {
  		        this.example = example;
  		    }
  		
  		    @Override
  		    public void run() {
  		        this.example.execute1();
  		    }
  		}
  		
  		class TheThread2 extends Thread {
  		
  		    private Example example;
  		
  		    public TheThread2(Example example) {
  		        this.example = example;
  		    }
  		
  		    @Override
  		    public void run() {
  		        this.example.execute2();
  		    }
  		}
  		```

  		

  	- Run with and without **synchronized block** to test and understand (recommendation  way to use)

  	- use when only a few lines of codes need to be locked as synchronized on method will lock the whole method which cause on efficiency

  	- In large scale will see the benefits of synchronized block

  		```java
  		public class Player {
  		    public static void main(String[] args) {
  		        Example example = new Example();
  		        TheThread t1 = new TheThread(example);
  		        TheThread t2 = new TheThread(example);
  		
  		        t1.start();
  		        t2.start();
  		    }
  		}
  		
  		class Example {
  		    private Object object = new Object();
  			
  		    public void execute() {
  		        synchronized (object) {
  		            for (int i = 0; i < 20; i++) {
  		                try {
  		                    Thread.sleep((long) (Math.random() * 1000));
  		                } catch (InterruptedException e) {
  		                    e.printStackTrace();
  		                }
  		                System.out.println("hello: " + i);
  		            }
  		        }
  		    }
  		    public void execute2() {
  		        synchronized (object) {
  		            for (int i = 0; i < 20; i++) {
  		                try {
  		                    Thread.sleep((long) (Math.random() * 1000));
  		                } catch (InterruptedException e) {
  		                    e.printStackTrace();
  		                }
  		                System.out.println("world: " + i);
  		            }
  		        }
  		    }
  		}
  		
  		class TheThread extends Thread {
  		    private Example example;
  		
  		    public TheThread(Example example) {
  		        this.example = example;
  		    }
  		
  		    @Override
  		    public void run() {
  		        this.example.execute();
  		    }
  		}
  		```

  	- Disadvantage of using synchronized —> In real world scenario, there are tens of threads calling the same synchronized method at the same time, later coming requests may wait too long to get respond.  Before 1.5 java has no other way to deal with. In 1.5, java provides java.util.concurrent to solve this situation (concurrent programming == multi-thread programming)

  - Deadlock —> neither thread is going to release its resource as the required part is in each other which cause both threads to wait for each other

  - Commucation among threads by using **wait()** and **notify()**

    - wait() —> causes the current thread to wait until another thread invokes the notify() method or notifyAll) method for this object.  
    - the current thread must own this object's monitor which means wait() method can only be used inside of synchronized code
    - notify() wakes up a single thread that is waiting on this object's monitor. If any threads are waiting on this object, one of them is chosen to be awakened. Choice is arbitrary.

    ```java
    public class Player {
        public static void main(String[] args) {
            Calculator calculator = new Calculator();
            Thread t1 = new AddThread(calculator);
            Thread t2 = new SubThread(calculator);
            t1.start();
            t2.start();
        }
    }
    
    
    class Calculator {
        private int number;
    
        public synchronized void increase() {
            if (0 != number) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            number++;
            System.out.println("number added current number is " + number);
            notify();
        }
    
        public synchronized void decrease() {
            if (0 == number) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            number--;
            System.out.println("number subtracted current number is " + number);
            notify();
        }
    }
    
    class AddThread extends Thread {
        private Calculator calculator;
    
        public AddThread(Calculator calculator) {
            this.calculator = calculator;
        }
    
        @Override
        public void run() {
            for (int i = 0; i < 20; i++) {
                try {
                    Thread.sleep((long) (Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                calculator.increase();
                System.out.println("i inside add "+i);
            }
        }
    }
    
    class SubThread extends Thread {
        private Calculator calculator;
    
        public SubThread(Calculator calculator) {
            this.calculator = calculator;
        }
    
        @Override
        public void run() {
            for (int i = 0; i < 20; i++) {
                try {
                    Thread.sleep((long) (Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                calculator.decrease();
                System.out.println("i inside sub "+i);
            }
        }
    }
    ```

    - mutiple-thread programming is hard
    - Thread safe: Using multiple threads at the same without causing any problems (concurrency issue)

    ```java
    public class Player {
        public static void main(String[] args) {
            Calculator calculator = new Calculator();
            Thread t1 = new AddThread(calculator);
            Thread t2 = new SubThread(calculator);
            Thread t3 = new AddThread(calculator);
            Thread t4 = new SubThread(calculator);
            t1.start();
            t2.start();
            t3.start();
            t4.start();
        }
    }
    
    class Calculator {
        private int number;
    
        public synchronized void increase() {
            if (0 != number) {
                try {
                    wait();  //keep in mind wait() release the lock and the next coming running thread may not be the original thread, CPU decides
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
    
            number++;
            System.out.println("number added current number is " + number);
            notify();
        }
    
        public synchronized void decrease() {
            if (0 == number) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            number--;
            System.out.println("number subtracted current number is " + number);
            notify();
        }
    }
    
    class AddThread extends Thread {
        private Calculator calculator;
    
        public AddThread(Calculator calculator) {
            this.calculator = calculator;
        }
    
        @Override
        public void run() {
            for (int i = 0; i < 200; i++) {
                try {
                    Thread.sleep((long) (Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                calculator.increase();
                System.out.println("i inside add "+i);
            }
        }
    }
    
    class SubThread extends Thread {
        private Calculator calculator;
    
        public SubThread(Calculator calculator) {
            this.calculator = calculator;
        }
    
        @Override
        public void run() {
            for (int i = 0; i < 200; i++) {
                try {
                    Thread.sleep((long) (Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                calculator.decrease();
                System.out.println("i inside sub "+i);
            }
        }
    }
    
    ```

    - think how to fix above example?  if —> while (cause should check the value again after wait not execute below directly)
    - threads more than 2 use while often, you don't know what is going to happen during sleep 

    ```java
    public class Player {
        public static void main(String[] args) {
            MyThread t1 = new MyThread();
            t1.start();
            synchronized (t1){   // Object o = new Object(); put an new object above and change t1 to o to check, think why
                try {
                    t1.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("final sum is " + t1.getSum());
            }
        }
    }
    
    class MyThread extends Thread {
        private int sum;
    
        public int getSum() {
            return sum;
        }
    
        @Override
        public void run() {
            synchronized (this) {  // remove sychronized block and notify to check
                for (int i = 0; i < 100; i++) {
                    System.out.println("another thread " + i);
                    sum += i;
                    System.out.println("current sum is " + sum);
                }
                notify();
            }
        }
    }
    
    ```

    

  - Thread pool

  	- wait pool
  	- lock pool
  	- [WhyinsideSync](https://www.xyzws.com/javafaq/why-wait-notify-notifyall-must-be-called-inside-a-synchronized-method-block/127)

2. **Clone**

	- shallow clone —> copy object, not reference

	- deep clone —> both copy object and reference

	- clone() method

		- x.clone() != x

		- x.clone().getClass() == x.getClass()

		- x.clone().equals(x)  —> this requires you rewrite your equals method properly

		- by convention call super.clone first then implement your own specifics and use **cloneable** 

		- cloneable is a mark interface which is shallow clone

	- shallow clone

		```java
		public class Player {
		    public static void main(String[] args) throws CloneNotSupportedException {
		        Car car1 = new Car();
		        car1.setCarName("BMW");
		        car1.setPrice(50000);
		        Car car2 = (Car) car1.clone(); //use another address to copy all the fields of car1
		
		        System.out.println("car1 is "+car1);
		        car2.setCarName("Benz");
		        System.out.println("car2 is "+car2);
		        System.out.println(car1==car2);
		    }
		}
		
		
		class Car implements Cloneable {
		    private int price;
		    private String carName;
		
		    public int getPrice() {
		        return price;
		    }
		
		    public void setPrice(int price) {
		        this.price = price;
		    }
		
		    public String getCarName() {
		        return carName;
		    }
		
		    public void setCarName(String carName) {
		        this.carName = carName;
		    }
		
		    @Override
		    protected Object clone() throws CloneNotSupportedException {
		        return super.clone();
		    }
		
		    @Override
		    public String toString() {
		        return "Car{" +
		                "price=" + price +
		                ", carName='" + carName + '\'' +
		                '}';
		    }
		}
		```

	- deep clone

		```java
		public class Player {
		    public static void main(String[] args) throws CloneNotSupportedException {
		        Car car = new Car();
		        car.setCarName("BMW");
		        car.setPrice(50000);
		
		        Part p = new Part();
		        p.setTyre("continental");
		        p.setPrice(100);
		        p.setCar(car);
		        System.out.println("part --> "+p);
		        Part p2 = (Part) p.clone();
		        car.setCarName("Benz");
		        car.setPrice(55000);
		        System.out.println("part2 --> "+p2); //coping so deep though original car changes, copied won't change
		        System.out.println(p);
		        System.out.println(p2);
		    }
		}
		
		
		class Car  implements Cloneable{
		    private int price;
		    private String carName;
		
		    public int getPrice() {
		        return price;
		    }
		
		    public void setPrice(int price) {
		        this.price = price;
		    }
		
		    public String getCarName() {
		        return carName;
		    }
		
		    public void setCarName(String carName) {
		        this.carName = carName;
		    }
		
		    @Override
		    protected Object clone() throws CloneNotSupportedException {
		        return super.clone();
		    }
		}
		
		class Part implements Cloneable {
		    private String tyre;
		
		    private int price;
		
		    private Car car;
		
		    public String getTyre() {
		        return tyre;
		    }
		
		    public void setTyre(String tyre) {
		        this.tyre = tyre;
		    }
		
		    public int getPrice() {
		        return price;
		    }
		
		    public void setPrice(int price) {
		        this.price = price;
		    }
		
		    public Car getCar() {
		        return car;
		    }
		
		    public void setCar(Car car) {
		        this.car = car;
		    }
		
		    @Override
		    protected Object clone() throws CloneNotSupportedException {
		        Part p = (Part) super.clone();
		        p.setCar((Car) p.getCar().clone());//this clone is cloning the very original car
		        return p;                           // not only copy it's object but also it's reference's object
		    }
		
		    @Override
		    public String toString() {
		        return "Part{" +
		                "tyre='" + tyre + '\'' +
		                ", price=" + price +
		                ", car=" + car.getCarName() +
		                '}';
		    }
		}
		```

		- For primitive data type and immutable objects no diff of shallow copy and deep copy

	- Use deserialization to deal with deep copy

		- By overwritting clone methods to implement deep copy will be complex, a chain of copying objects will generate. (Think there is a multiple layers of references or many references in class)

		- First let copying object class implement serializable, then write into a stream then read out, thus deep copy is done

		- Use transient to keep out of non-serializable fields when necessary

			```java
			public class Player {
			    public static void main(String[] args) throws IOException, ClassNotFoundException {
			        Car car = new Car();
			        car.setCarName("BMW");
			        car.setPrice(50000);
			
			        Part p = new Part();
			        p.setPrice(200);
			        p.setTyre("Old");
			        p.setCar(car);
			        System.out.println("p -->" + p);
			
			        Part p2 = (Part) p.deepCopy();
			        System.out.println("p2-->" + p2);
			        car.setCarName("newName");
			        System.out.println("p -->" + p);
			        System.out.println("p2-->" + p2);
			
			        //change p2 fields won't affect p, test on your own
			    }
			}
			
			
			class Car implements Serializable {
			
			    private int price;
			    private String carName;
			
			    public int getPrice() {
			        return price;
			    }
			
			    public void setPrice(int price) {
			        this.price = price;
			    }
			
			    public String getCarName() {
			        return carName;
			    }
			
			    public void setCarName(String carName) {
			        this.carName = carName;
			    }
			
			    @Override
			    public String toString() {
			        return "Car{" +
			                "price=" + price +
			                ", carName='" + carName + '\'' +
			                '}';
			    }
			}
			
			class Part implements Serializable {
			    private String tyre;
			
			    private int price;
			
			    private Car car;
			
			    public String getTyre() {
			        return tyre;
			    }
			
			    public void setTyre(String tyre) {
			        this.tyre = tyre;
			    }
			
			    public int getPrice() {
			        return price;
			    }
			
			    public void setPrice(int price) {
			        this.price = price;
			    }
			
			    public Car getCar() {
			        return car;
			    }
			
			    public void setCar(Car car) {
			        this.car = car;
			    }
			
			    @Override
			    public String toString() {
			        return "Part{" +
			                "tyre='" + tyre + '\'' +
			                ", price=" + price +
			                ", car=" + car.getCarName() +
			                '}';
			    }
			
			   //often write out to files, remember use ObjectOutputStream to wrapper cause you are dealing with Objects
			    public Object deepCopy() throws IOException, ClassNotFoundException {
			        ByteArrayOutputStream bos = new ByteArrayOutputStream();
			        ObjectOutputStream oos = new ObjectOutputStream(bos);
			        oos.writeObject(this);
			        ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
			        ObjectInputStream ois = new ObjectInputStream(bis);
			        return ois.readObject();
			    }
			}
			```

			

			- serialVersionUID —> a long number to check compatibility (compare the class if it's the same when deserialization) 
			- ignore deleted fields, set default values for added fields.

			

