# Prerequisites

1. Practice Makes Perfect  -> Yes You Can 

2. Download and install below:

- Linux or Unix like OS 
- Windows -> git bash
- [Java](<https://www.java.com/en/download/>)
- [Python](<https://www.python.org/downloads/>)
- Java Brains IDE [Intellij](<https://www.jetbrains.com/idea/download/#section=mac>) (recommend)
- [Mysql](<https://dev.mysql.com/downloads/>)
- Shell
- Vim (default) or Nano or Emacs 
- Postman
- Maven
- Node.js
- Terminal or [iTerm2](<https://www.iterm2.com/>) (optional)
- Markdown (optional) —> Typora
	- focus on text
	- transfer to html easily
	- open in any editor

3. English and Comunication
  - Behavior 
  - Talk is not cheap

4. What is program?

5. Do best practice

6. Learn from each other
  - Thoroughly 
  - Filling the gaps 
  - Typing

7. Algorithm [leetcode](<https://leetcode.com/problemset/all/>)

  ​		          [hackerrank](<https://www.hackerrank.com/dashboard?h_r=hrw&h_l=domains>)

  - Logic 
  - Key function
  - Show me you code

8. Let's do it together

# little about computer

​                    CPU (control unit + logic unit)

input  —>main memory(RAM Random Access Memory)   —> output                        

​                     disk

CPU +main memory = system unit  (display car)

for CPU: **RISC** and **CISC**

> Reduced Instruction Set Computer, **RISC**      SPARC  ARM
>
> Complex Instruction Set Computer, **CISC**      AMD Intel  (8086,80286, 80386)  x86_64
>
> 64 —> one time of max read is 2^32   Math.pow(2,64)    (primitive data types)
>
> newer computer means newer instruction set —> save power , complex commands , do things more

cat /proc/cpuinfo     -- linux

sysctl -a | grep machdep.cpu    --mac

Volumn unit

| Unit    | Kilo | Mega  | Giga  | Tera  | Peta  | Exa   | Zetta |
| ------- | ---- | ----- | ----- | ----- | ----- | ----- | ----- |
| binary  | 1024 | 1024K | 1024M | 1024G | 1024T | 1024P | 1024E |
| decimal | 1000 | 1000K | 1000M | 1000G | 1000T | 1000P | 1000E |

​    (oct and hex)

Speed unit  —> cpu  (core  real multiple-threads,  i3/i5/i7)

   MHz  or GHz  (on internet Mbps —> Mbits per second)   3.6G —> 3.6x10^9 , cpu operate times per second

   20M/5M —> overkill most web usage

   one indicator to judge how good a computer 

Categories

​	Supercomputer

​    Mainframe Computer

​    Minicomputer

​    Workstation

​    Microcomputer

# Linux Commands

1. *format* : command [-options] [parameter1] [parameter2] ...
  - tab to autocomplete
- where are these commands? (**which** or **where**)
  
2. *path* : absolute VS relative

  from current or from base

  root  -> /

  home -> /home/username  =  ~

  current  -> .    parent -> ..

  echo $PATH

3. **ls** 

  - ls -a ~ 
  - ll  ->  -rw-r--r--  1 xikaixiong  staff    53B Apr 13 16:17 syllabus
  - ls -l
  - ls -h
  - ls -t 

4. **authorization** and **chmod**

     read write execute 

     - -rw-rw-r--  : -file tyle 4 : r  2 : w  1 : x
     - owner group others
     - chmod +w
     - chmod -w
     - chmod 777

5. **man**

  - man 3 malloc()    malloc is written in C

6. **cd**

  - cd ~
  - cd -

7. **touch**

8. **clear**

9. **pwd**

10. **history**

  - control + r

11. **cat**

   - small files
   - contat simple multiple files

12. **more**

   - view large files

13. **pipe**

   - |
   - history | more

14. **mkdir**

15. **rmdir**

16. **rm**

   - rm -rf  -> !!! think very well before do this
   - rm -rfi

17. **cp**

18. **scp**

   - check with ssh 
   - local with remote

19. **mv**

20. **tree**

21. **echo**

22. **ln**

   - symbolic link -> don't take position of memory, only work for common files, no directory, become invalid when origin is deleted
   - ln origin linked -> difference with cp(cp won't changed copied file while linked will)
   - ln -s origin linked
   - ll -> count shows how many files are linked

23. **grep**

   - search files -> logs
   - grep -n sth filename : show line number with sth
   - grep -n '^o' filename : start with o
   - grep -n 'o$' filename: end with o
   - wildcards : * ?   one or more, only one   ls *.m?
   - [] -> or      [abc]  [a-z]
   - grep -n '[Hh]ello' filename

24. **find**

25. *redirection*

   - '>'
   - '>>'

26. *hidden directory*

   - .filename

27. **tar**

   - tar -cvf test.tar *.py
   - tar -xvf test.tar
   - f must put in the end and use all together or don't use

28. **gzip**

   - ll to check the size
   - gzip test.tar
   - gzip -d *.tar.gz
   - tar -xvf *.tar

29. *tar within gzip*

   - tar -zcvf name.tar.gz *.py
   - tar -zxvf *.tar.gz

30. *optional tar*

   - tar -jcvf name.tar.gz *.py
   - tar -jxvf *.tar.gz

31. **zip**

   - zip name files
   - unzip *.zip
   - unzip -d directoryname *.zip

32. **which**

33. **who**

34. **exit**

35. **sudo**    !!!

36. **df**

   - disk availability

37. **du**

   - current directory usage

38. **cal**

39. **date**

40. **ps**

   - ps aux
   - a = show processes for all users
   	u = display the process's user/owner
   	x = also show processes not attached to a terminal
   - check fault thread
   - run while.py to test

41. **kill**

   - kill pid

   - kill -9 : force to kill if still not working, tell system manager

42. **top**

43. **ifconfig**

   - check laptop address in en0: local and remote
   - ifconfig | grep 127

44. **ping**

   - ping 192.168.#.##
   - ping www.google.com

45. **ssh**

   - ssh xikaixiong@192.168.#.##

46. **su**

   - swith user
   - su -  :  swith to user's working directory ~

47. Learn more you will become *System Manager* or *System Engineer*

   - reboot
   
   - shutdown
   
   - init
   
   - groupmod
   
   - groupadd
   
   - groupdel
   
   - groups
   
   - usermod
   
   - useradd
   
   - passwd
   
   - userdel
   
   - check on your own 
   
   	
   
48. **jar**

   jar -cvf projectname.war *    —> make all files into war   

   jar -xvf projectname.war   —> extract war     

   above 2 commands used for 

   jar -cf myfile.jar *.java   —> make all .java into jar file
   
   jar cmf META-INF/MANIFEST.MF myjar.jar App.class App.java

   java -jar myfile.jar   —> run executable jar  (need to understand manifest attribute in jar file)
   
49. **nslookup**  --> domain server name

   nslookup [www.google.com](www.google.com)

50. lsof -i -P -n

   > check which port is in use and 

   

   

   

   

# Shell

1. Choose your shell

	- **zsh**
	- [bash](<http://tldp.org/LDP/Bash-Beginners-Guide/html/>)
	- fish
	- ksh
	- csh
	- ...
	- Choose anyone and get used to it

2. Environment variable 

	- .zshrc   (Unix like)
	- windows

3. Shell scripting is glue and auto scripts  (type below scripts)

	- sh echo.sh

	```shell
	#!/bin/bash
	echo 'what is your name?'
	read name
	echo "well, $name, you typed $# arguments:"
	echo "$*"
	```

	- sh if.sh

	```shell
	echo "Enter source and target file name:"
	read source target
	if mv $source $target
	then
	echo "Your file has benn successfully renamed."
	else
	echo "rename failed"
	fi
	```

	- sh parameter.sh

	```shell
	echo the total number of items in the current directory is=$#
	```

	- sh for.sh ->count directories in current folder

	```shell
	for item in *
	do
	 if [ -d $item ]
	 then
	  echo $item
	 fi
	done
	```

	- sh iffile.sh

	```shell
	echo "Enter a name:\c"
	read fname
	if [ -f $fname ]
	then
	 echo "You indeed entered a file name."
	else
	 echo "Don't provide me crazy inputs."
	fi
	```

	- sh readfile.sh

	```shell
	echo "Enter a file name:\c"
	read fname
	if [ -z "$fname" ]
	then
	 exit
	fi
	cat -n $fname
	```

	- sh help.sh

	```shell
	for cmd in `cat commandlist`
	do
	 man $cmd
	done
	```

	- sh append.sh , try chmod 

	```shell
	echo "Enter file name:\c"
	read fname
	if [ -f $fname ]
	then
	   if [ -w $fname ]
	   then
	     echo "Type matter to append. To quit press ctrl + d"
	     cat >> $fname
	   else
	     echo "You do not have permission to write."
	   fi
	fi
	```

	- sh number.sh

	```shell
	cho "Enter a number between 10 and 20:\c"
	read num
	if [ $num -lt 10 ]
	then
	 echo "that is smaller than belt"
	elif [ $num -gt 20 ]
	then
	 echo "that is larger than belt"
	else
	 echo "Now you are making sense"
	fi
	```

	- sh findFileByTime.sh

	```shell
	find /Users/xikaixiong/Desktop/fileTest/Shell -mtime +200 -name "*.sh"
	-m modification time
	
	a – The access time of the file reference
	B – The birth time of the file reference
	c – The inode status change time of reference
	m – The modification time of the file reference
	t – reference is interpreted directly as a time
	```

	- sh until.sh

	```shell
	count=1
	until [ $count -ge 10 ]
	do
	  echo $count
	  count=`expr $count + 1`
	done
	```

	- sh while.sh

	```shell
	count=1
	while [ $count -le 10 ]
	do
	 echo $count
	 count=`expr $count + 1`
	done
	```

	- sh case.sh

	```shell
	echo "Enter a character:\c"
	read var
	case $var in
	[a-z])
	 echo "alphabet"
	 ;;
	[A-Z])
	 echo "uppper alphabet"
	;;
	[0-9])
	 echo "digit"
	;;
	?)
	 echo "special"
	;;
	*)
	 echo "more than one"
	;;
	esac
	sh case.sh
	```

	- sh array.sh  -> read and understand

	```shell
	arrayZ=( one two three four five five )
	
	echo
	
	# Trailing Substring Extraction
	echo ${arrayZ[@]:0}     # one two three four five five
	#                ^        All elements.
	
	echo ${arrayZ[@]:1}     # two three four five five
	#                ^        All elements following element[0].
	
	echo ${arrayZ[@]:1:2}   # two three
	#                  ^      Only the two elements after element[0].
	
	echo "---------"
	
	
	# Substring Removal
	
	# Removes shortest match from front of string(s).
	
	echo ${arrayZ[@]#f*r}   # one two three five five
	#               ^       # Applied to all elements of the array.
	                        # Matches "four" and removes it.
	
	# Longest match from front of string(s)
	echo ${arrayZ[@]##t*e}  # one two four five five
	#               ^^      # Applied to all elements of the array.
	                        # Matches "three" and removes it.
	
	# Shortest match from back of string(s)
	echo ${arrayZ[@]%h*e}   # one two t four five five
	#               ^       # Applied to all elements of the array.
	                        # Matches "hree" and removes it.
	
	# Longest match from back of string(s)
	echo ${arrayZ[@]%%t*e}  # one two four five five
	#               ^^      # Applied to all elements of the array.
	                        # Matches "three" and removes it.
	
	echo "----------------------"
	
	
	# Substring Replacement
	
	# Replace first occurrence of substring with replacement.
	echo ${arrayZ[@]/fiv/XYZ}   # one two three four XYZe XYZe
	#               ^           # Applied to all elements of the array.
	
	# Replace all occurrences of substring.
	echo ${arrayZ[@]//iv/YY}    # one two three four fYYe fYYe
	                            # Applied to all elements of the array.
	
	# Delete all occurrences of substring.
	# Not specifing a replacement defaults to 'delete' ...
	echo ${arrayZ[@]//fi/}      # one two three four ve ve
	#               ^^          # Applied to all elements of the array.
	
	# Replace front-end occurrences of substring.
	echo ${arrayZ[@]/#fi/XY}    # one two three four XYve XYve
	#                ^          # Applied to all elements of the array.
	
	# Replace back-end occurrences of substring.
	echo ${arrayZ[@]/%ve/ZZ}    # one two three four fiZZ fiZZ
	#                ^          # Applied to all elements of the array.
	
	echo ${arrayZ[@]/%o/XX}     # one twXX three four five five
	#                ^          # Why?
	
	echo "-----------------------------"
	
	
	replacement() {
	    echo -n "!!!"
	}
	
	echo ${arrayZ[@]/%e/$(replacement)}
	#                ^  ^^^^^^^^^^^^^^
	# on!!! two thre!!! four fiv!!! fiv!!!
	# The stdout of replacement() is the replacement string.
	# Q.E.D: The replacement action is, in effect, an 'assignment.'
	
	echo "------------------------------------"
	
	#  Accessing the "for-each":
	echo ${arrayZ[@]//*/$(replacement optional_arguments)}
	#                ^^ ^^^^^^^^^^^^^
	# !!! !!! !!! !!! !!! !!!
	
	#  Now, if Bash would only pass the matched string
	#+ to the function being called . . .
	
	echo
	
	exit 0
	
	#  Before reaching for a Big Hammer -- Perl, Python, or all the rest --
	#  recall:
	#    $( ... ) is command substitution.
	#    A function runs as a sub-process.
	#    A function writes its output (if echo-ed) to stdout.
	#    Assignment, in conjunction with "echo" and command substitution,
	#+   can read a function's stdout.
	#    The name[@] notation specifies (the equivalent of) a "for-each"
	#+   operation.
	#  Bash is more powerful than you think!
	```

	

# vim

1. vim mode

	- insert mode
	- command mode
2. change arrow to hjkl
3. vim filename
4. i  -> enter insert mode
5. esc -> exit insert mode, command mode
6. :  -> command to execute
7. L -> end of current page  H -> head M -> middle
8. G -> move cursor to last line of page
9. A -> enter insert mode at the end of current line, try a
10. o -> enter insert mode at the beginning  of the next line,  try O 
11. 0 -> move cursor to the beginning of current line, try $ and ^
12. dd -> delete current line and save it in clip board, try D
13. p -> paste things in clip board to current line
14. u -> undo
15. control + r -> redo
16. w -> one word forward
17. b -> one word backward
18. dw -> delete one word and save it in clip board
19. d3w -> delete three words and save it in clip board
20. gg -> move cursor to the beginning of the whole page
21. %s/Hello/Bye/g  -> change all test from 'Hello' to 'Bye' , try without g
22. r -> replace one char, try R
23. X -> delte one char before, try x
24. . -> redo last command
25. J -> join 2 lines
26. d$ -> delete to the end of current line
27. :w -> write 
28. :q -> quit
29. :q! -> quit without save
30. :x -> save and quit
31. :y -> copy
32. v -> visual motion to select
33. control e -> scroll down, try control b
34. /text -> search text, n to next
35. set ic -> set ignore case, try noic
36. :noh -> no highlight
37. % -> find matching case {[()]}
38. fx -> find fist char of 'x'



# Some Useful folders

/bin

> for all your executable binaries

/etc   

> **“etc”** is an English word which means etcetera (and so on)
>
> a central location for all your configuration files are located and this can be treated as nerve centre of your Linux/Unix machine.

/dev 

> for all hardware devices attached to machine. device files

/var

> files and directories that are constantly changing 

/var/log

/home

/tmp

> system temprorary directory. All users have read+write acces

