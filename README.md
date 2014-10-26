the-game-of-life
================

An experiment in rule design for a cellular automaton life simulator. This is my first major project in an introductory CS class at Reed College, for professor Jim Fix.

Three files comprise this project:

Grid.py provides code for the Grid class which defines an object that performs the grid simulation. In it, the grid itself is defined, framed, and painted. Button inputs for the interact are also provided.

Life.py prints instructions for the user to navigate the demonstration of ten sequential rules on the grid.

Rules.py provides the code for ten different behavioral patterns. Rules 1 through 6 solve challenges ranging from pattern construction to image processing using the rules of the game of life, all according to the prompt of the assignment. Rules 7 through 10 are of my own devising, attempts to utilize the constraints of the game of life to render a comet, armageddon, a zombie invasion, and the growth of a weirwood tree.

Shadow, fill, glider, age, comet, zombie, and weirwood are accompanying pattern files used by the grid demo to simulate specific rule behaviors. Reed.pgm provides an image file of a photograph of Eliot Hall from Reed's great lawn, also used in one of the image processing rules.

To run the simulation, execute life.py from the command line.

