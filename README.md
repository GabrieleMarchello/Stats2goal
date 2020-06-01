# Stats2goal

Stats2goal is an algorithm written in Python to produce a graphical representation of goal scored in every game registered by **statsbomb**. 
Stats2goal requires a few parameters in input - to specify the game of interests -, and the .json file that can be downloaded from the following link:
> https://statsbomb.com/academy/ 

It produces in ouput a .gif file for each goal.

**stats2goal.py** is comprised of four different files: *stats2goal.py*, *utils.py*, *plots.py*, and *drawpitch.py*.
The Stats2goal.py receives in input all the paraters the user has to define, including the gender, the competition, the country, the team of interest and its opponent. In addition, it receives in input both *dpi* and *fps* values to write the .gif file in output.

**utils.py** is imported in the main stats2goal.py code and contains all the functions needed to extract the steps leading to score a goal.

**plots.py** contains the instructions to plot the different step and saves a .jpg for each of them.

**drawpitch** - as the name may suggest - draws a green pitch as background of every figure.

