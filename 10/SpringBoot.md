# SpringBoot

Spring Initializr

IDE

maven

choose 1.8 

- start of pom

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.1.5.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.sincere</groupId>
	<artifactId>blog</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>blog</name>
	<description>Demo project for Spring Boot</description>

	<properties>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>


		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>

```

import spring boot modules

- web

- Thymeleaf

- JPA

- MySql

- Aspects

- DevTools

	```xml
	<?xml version="1.0" encoding="UTF-8"?>
	<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	    <modelVersion>4.0.0</modelVersion>
	    <parent>
	        <groupId>org.springframework.boot</groupId>
	        <artifactId>spring-boot-starter-parent</artifactId>
	        <version>2.1.5.RELEASE</version>
	        <relativePath/> <!-- lookup parent from repository -->
	    </parent>
	    <groupId>com.sincere</groupId>
	    <artifactId>blog</artifactId>
	    <version>0.0.1-SNAPSHOT</version>
	    <name>blog</name>
	    <description>Demo project for Spring Boot</description>
	
	    <properties>
	        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
	        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
	        <java.version>1.8</java.version>
	
	    </properties>
	
	    <dependencies>
	        <dependency>
	            <groupId>org.springframework.boot</groupId>
	            <artifactId>spring-boot-starter</artifactId>
	        </dependency>
	
	        <dependency>
	            <groupId>org.springframework.boot</groupId>
	            <artifactId>spring-boot-starter-test</artifactId>
	            <scope>test</scope>
	        </dependency>
	
	
	        <dependency>
	            <groupId>org.springframework.boot</groupId>
	            <artifactId>spring-boot-starter-web</artifactId>
	        </dependency>
	
	        <dependency>
	            <groupId>org.springframework.boot</groupId>
	            <artifactId>spring-boot-starter-aop</artifactId>
	        </dependency>
	
	        <dependency>
	            <groupId>org.springframework.boot</groupId>
	            <artifactId>spring-boot-starter-data-jpa</artifactId>
	        </dependency>
	
	        <dependency>
	            <groupId>org.springframework.boot</groupId>
	            <artifactId>spring-boot-starter-thymeleaf</artifactId>
	        </dependency>
	
	        <dependency>
	            <groupId>org.springframework.boot</groupId>
	            <artifactId>spring-boot-devtools</artifactId>
	            <scope>runtime</scope>
	        </dependency>
	        <dependency>
	            <groupId>mysql</groupId>
	            <artifactId>mysql-connector-java</artifactId>
	            <scope>runtime</scope>
	        </dependency>
	
	
	    </dependencies>
	
	    <build>
	        <plugins>
	            <plugin>
	                <groupId>org.springframework.boot</groupId>
	                <artifactId>spring-boot-maven-plugin</artifactId>
	            </plugin>
	        </plugins>
	    </build>
	
	</project>
	```

yml configuration

- application.yml

	```yml
	spring:
	  thymeleaf:
	    mode: HTML
	    cache: false
	  profiles:
	    active: dev
	```

- application-dev.yml

	```yml
	spring:
	  datasource:
	    driver-class-name: com.mysql.cj.jdbc.Driver
	    url: jdbc:mysql://localhost:3306/blog?useSSL=false&useUnicode=true&characterEncoding=utf-8&serverTimezone=UTC
	    username: root
	    password: 
	  jpa:
	    hibernate:
	      ddl-auto: update  
	    show-sql: true
	
	logging:
	  level:
	    root: info
	    com.sincere: debug
	  file: log/blog-dev.log
	```

	update —> once your model entity changed, it will reflect into the DB

	show-sql —> sql will be shown in log and console

	root —> spring boot default 

- application-pro.yml

	```yml
	spring:
	  datasource:
	    driver-class-name: com.mysql.cj.jdbc.Driver
	    url: jdbc:mysql://localhost:3306/blog?useSSL=false&&useUnicode=true&characterEncoding=utf-8&serverTimezone=UTC
	    username: root
	    password:
	  jpa:
	    hibernate:
	      ddl-auto: none
	    show-sql: true
	
	logging:
	  level:
	    root: warn
	    com.sincere: info
	  file: log/blog-pro.log
	server:
	  port: 8081
	```

- logback

	```xml
	<?xml version="1.0" encoding="UTF-8" ?>
	<configuration>
	    <!--include default logback settings for spring boot -->
	    <include resource="org/springframework/boot/logging/logback/defaults.xml"/>
	    <property name="LOG_FILE" value="${LOG_FILE:-${LOG_PATH:-${LOG_TEMP:-${java.io.tmpdir:-/tmp}}}/spring.log}"/>
	    <include resource="org/springframework/boot/logging/logback/console-appender.xml"/>
	
	    <!--rewrite Spring Boot org/springframework/boot/logging/logback/file-appender.xml settings-->
	    <appender name="TIME_FILE"
	              class="ch.qos.logback.core.rolling.RollingFileAppender">
	        <encoder>
	            <pattern>${FILE_LOG_P	ATTERN}</pattern>
	        </encoder>
	        <file>${LOG_FILE}</file>
	        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
	            <fileNamePattern>${LOG_FILE}.%d{yyyy-MM-dd}.%i</fileNamePattern>
	            <!--keep log for 30 days-->
	            <maxHistory>30</maxHistory>
	            <!--
	            Spring Boot default, when log size get 10M ，log gets split
	            -->
	            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
	                <maxFileSize>10MB</maxFileSize>
	            </timeBasedFileNamingAndTriggeringPolicy>
	
	        </rollingPolicy>
	    </appender>
	
	    <root level="INFO">
	        <appender-ref ref="CONSOLE"/>
	        <appender-ref ref="TIME_FILE"/>
	    </root>
	
	</configuration>
	        <!--
	            delete this file will use spring boot default logback settings
	        -->
	```

- static and templates under resources

	index.html

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8"/>
	    <title>Blog</title>
	
	</head>
	<body>
	    index page
	</body>
	</html>
	```

	controller : IndexController

	```java
	@Controller
	public class IndexController {
	
	    @GetMapping("/")
	    public String index() {
	        return "index";
	    }
	}
	```

	Run to test

- error under templates

	404.html

	```html
	<!DOCTYPE html>
	<html xmlns:th="http://www.thymeleaf.org">
	<head>
	    <meta charset="UTF-8"/>
	
	    <!--mobile preview-->
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Blog</title>
	
	
	</head>
	<body>
	    <h1>404</h1>
	</body>
	</html>
	```

	500.html

	```html
	<!DOCTYPE html>
	<html xmlns:th="http://www.thymeleaf.org">
	<head>
	    <meta charset="UTF-8"/>
	    <title>500</title>
	</head>
	<body>
	    <h1>500</h1>
	</body>
	</html>
	```

	error.html  —> developer tool to check

	```html
	<!DOCTYPE html>
	<html xmlns:th="http://www.thymeleaf.org">
	<head>
	    <meta charset="UTF-8"/>
	    <title>Error</title>
	</head>
	<body>
	<h1>Error</h1>
	</body>
	</html>
	```

- Test error

	```java
	@Controller
	public class IndexController {
	
	    @GetMapping("/")
	    public String index() {
	        int a = 9/0;
	        return "index";
	    }
	}
	```

- custom error  —> developer tool to check (read server info on web page)

	@ControllerAdvice  —> intercept all class which marked with @Controller

	```html
	<!DOCTYPE html>
	<html xmlns:th="http://www.thymeleaf.org">
	<head>
	    <meta charset="UTF-8"/>
	    <title>Error</title>
	</head>
	<body>
	<h1>Error</h1>
	
	<div>
	    <div th:utext="'&lt;!--'" th:remove="tag"></div>
	    <div th:utext="'Failed Request URL : ' + ${url}" th:remove="tag"></div>
	    <div th:utext="'Exception message : ' + ${exception.message}" th:remove="tag"></div>
	    <ul th:remove="tag">
	        <li th:each="st : ${exception.stackTrace}" th:remove="tag"><span th:utext="${st}" th:remove="tag"></span></li>
	    </ul>
	    <div th:utext="'--&gt;'" th:remove="tag"></div>
	</div>
	</body>
	</html>
	```

	handler 

	ControllerExceptionHandler

	```java
	@ControllerAdvice
	public class ControllerExceptionHandler {
	
	    private final Logger logger = LoggerFactory.getLogger(this.getClass());
	
	    // handle all exception, @ExceptionHandler mark this method can deal with Exception
	    @ExceptionHandler(Exception.class)
	    public ModelAndView exceptionHandler(HttpServletRequest request, Exception e) {
	        //        at console level
	        logger.error("Request URL : {}, Exception :{}", request.getRequestURI(), e.getMessage());
	
	        ModelAndView mv = new ModelAndView();
	        mv.addObject("url", request.getRequestURL());
	        mv.addObject("exception", e);
	        mv.setViewName("error/error");
	
	        return mv;
	
	    }
	}
	```

- null blog exception 

	custom exception throw at 404

	```java
	@ResponseStatus(HttpStatus.NOT_FOUND)
	public class NotFoundException extends RuntimeException {
	
	    public NotFoundException() {
	    }
	
	    public NotFoundException(String message) {
	        super(message);
	    }
	
	    public NotFoundException(String message, Throwable cause) {
	        super(message, cause);
	    }
	
	}
	```

	- avoid ControllerExceptionHandler to deal with every exception

		```java
		@ControllerAdvice
		public class ControllerExceptionHandler {
		
		    private final Logger logger = LoggerFactory.getLogger(this.getClass());
		
		    // handle all exception
		    @ExceptionHandler(Exception.class)
		    public ModelAndView exceptionHandler(HttpServletRequest request, Exception e) throws Exception {
		        //        at console level
		        logger.error("Request URL : {}, Exception :{}", request.getRequestURI(), e.getMessage());
		
		        if (AnnotationUtils.findAnnotation(e.getClass(), ResponseStatus.class) != null) {
		            throw e;
		        }
		
		        ModelAndView mv = new ModelAndView();
		        mv.addObject("url", request.getRequestURL());
		        mv.addObject("exception", e);
		        mv.setViewName("error/error");
		
		        return mv;
		
		    }
		}
		```

	- change controller to test

	```java
	@Controller
	public class IndexController {
	
	    @GetMapping("/")
	    public String index() {
	        String blog = null;
	
	        if (blog == null) {
	            throw  new NotFoundException("blog not found");
	        }
	        return "index";
	    }
	}
	```

- Spring AOP to log (What are other ways to write log?)

	- log content

		> url
		>
		> ip
		>
		> classMethod —> which method is getting called
		>
		> arguments  —> parameters passed
		>
		> return content

	- create aspect package

	- LogAspect

		```java
		@Aspect
		@Component
		public class LogAspect {
		
		   private final Logger logger = LoggerFactory.getLogger(this.getClass());
		
		  //this method is going to be called once method in controller package is executing
		   @Pointcut("execution(* com.sincere.blog.controller.*.*(..))")
		   public void log(){
		
		   }
		
		   @Before("log()")
		   public void doBefore(){
		       logger.info("----doBefore-----");
		   }
		
		   @After("log()")
		   public void doAfter(){
		       logger.info("----doAfter-----");
		   }
		
		   @AfterReturning(returning = "result",pointcut = "log()")
		   public void doAfterReturning(Object result) {
		       logger.info("----get result after return-----");
		   }
		}
		
		```

		change controller to test

		```java
		@Controller
		public class IndexController {
		
		    @GetMapping("/{id}/{name}")
		    public String index(@PathVariable Integer id,@PathVariable String name) {
		
		
		        System.out.println("---------index string in controller-----");
		        return "index";
		    }
		}
		```

		Request Log class , add inside LogAspect

		```java
		private class RequestLog {
		        private String url;
		        private String ip;
		        private String ClassMethod;
		        private Object[] args;
		
		        public RequestLog(String url, String ip, String classMethod, Object[] args) {
		            this.url = url;
		            this.ip = ip;
		            ClassMethod = classMethod;
		            this.args = args;
		        }
		
		
		        @Override
		        public String toString() {
		            return "RequestLog{" +
		                    "url='" + url + '\'' +
		                    ", ip='" + ip + '\'' +
		                    ", ClassMethod='" + ClassMethod + '\'' +
		                    ", args=" + Arrays.toString(args) +
		                    '}';
		        }
		    }
		```

		change doBefore then run to test, check logs

		```java
		 @Before("log()")
		    public void doBefore(JoinPoint joinPoint) {
		        ServletRequestAttributes attributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
		        HttpServletRequest request = attributes.getRequest();
		        String url = String.valueOf(request.getRequestURL());
		        String ip = request.getRemoteAddr();
		        System.out.println();
		        String classMethod = joinPoint.getSignature().getDeclaringTypeName() + "." + joinPoint.getSignature().getName();
		        Object[] args = joinPoint.getArgs();
		        RequestLog requestLog = new RequestLog(url, ip, classMethod, args);
		        logger.info("Request : {}", requestLog);
		    }
		```

- import static pages  —> coperate with front

	

	