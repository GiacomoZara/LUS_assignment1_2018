# LUS_project1

###Requirements:<h3>

`python3`  
`openfst 1.6.5`  
`opengrm 1.3.3`  

###python modules:  
	- `math` 
	- `os`  
	- `sys`  
	- `pickle`  
	- `subprocess`  
	
###Running the code

The file named `script_complete.py` runs sequentially all the attempts made, with the different parameters chosen. The file named `script.py`, intead, only runs the procedure that gave the best result. Provided that the folder system respects the delivered one, only the "script.py" file (or "script_complete.py" if interested in all the results) needs to be run with the following command:

`python3 script.py`

or

`python3 script_complete.py`

The code outputs in a file (or in the console in the case of `script.py`) the result of the evaluation as computed by `conlleval.pl`.  
Tested on Ubuntu 17.10


