# belief-revision-grp53
To succesfully run our program you should following these steps:

Prerequisite: Having python version 3.8 installed

NOTE: The following steps are steps that we know work.

1. FOR WINDOWS: 

	1.1. If you choose to run this program in commandprompt, then follow these steps else jump to 1.2:

		1.1.1. Install anaconda/conda. Guide: https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html
		1.1.2. Open a terminal and type "conda create --name myenv python=3.8" 
		1.1.3. When conda asks you to proceed, type y.
		1.1.4. Now activate your conda environment by typing "conda activate myenv"
		1.1.5. Now type "pip3 install sympy"
		1.1.6. You will have to redirect to the folder where "CLI.py" is located. Use "cd"  in terminal to redirect to the folder
		1.1.7. You can now simply type "CLI.py" and the program should be running now

	1.2. If you want to run the program in PyCharm, then follow these steps:

		1.2.1. Install sympy. If PyCharm doesn't suggest to install sympy follow step 1.2.2
		1.2.2. Press "View | Tool Windows | Python packages" 
		1.2.3. The Python Packages tool window will appear. In the search bar type "sympy" and install the package
		1.2.4. It could occur that you will need to install the package "prompt". Either PyCharm would suggest to install it or install with steps 1.2.2 and 1.2.3
		1.2.5. You should be run the program now by pressing "Run | Run "CLI" " or pressing shift+F10
2. FOR MAC:

	2.1. If you want to the program in PyCharm, then follow these steps:
		
		2.1.1. Install sympy. If PyCharm doesn't suggest to install sympy follow step 2.1.1
		2.1.2. Press "View | Tool Windows | Python packages" 
		2.1.3. The Python Packages tool window will appear. In the search bar type "sympy" and install the package
		2.1.4. It could occur that you will need to install the package "prompt". Either PyCharm would suggest to install it or install with steps 1.2.2 and 1.2.3
		2.1.5. You should be run the program now by pressing "Run | Run "CLI" " or pressing shift+F10

3. USAGE:
	
	The program will give you options to choose between 3 menu options: 'r' for revision of belief base, 'e' for emptying the belief base and 'q' to stop the program
	
	When typing 'r', the program will ask to enter a formula/query and the formula's order.
	
	A formula consist of literals (e.g. a, b, c etc.), conjunctions (e.g. a & b), disjunctions (e.g. a | b) and implication (e.g. a >> b)
		
	An example of the usage of the program:

		Curent BeliefBase:
		------------------
		-------Empty------
		------------------
		Menu Options:
		r: Belief revision
		e: Empty belief base
		q: Quit Program
    
		>>> r
		Enter Query:
		>>> a | b
		Enter Order:
		>>> 0.5

		Curent BeliefBase:
		------------------
		(a | b, 0.5)
		------------------
		Menu Options:
		r: Belief revision
		e: Empty belief base
		q: Quit Program
    
		>>> r
		Enter Query:
		>>> b|c
		Enter Order:
		>>> 0.6

		Curent BeliefBase:
		------------------
		(a | b, 0.5) (b | c, 0.6)
		------------------
		Menu Options:
		r: Belief revision
		e: Empty belief base
		q: Quit Program
    
		>>> e

		Curent BeliefBase:
		------------------
		-------Empty------
		------------------
		Menu Options:
		r: Belief revision
		e: Empty belief base
		q: Quit Program
    
		>>> 
	
