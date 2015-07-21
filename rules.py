import random

# * * * * * * * * Modified Rule 1 * * * * * * * * * * *
#
# In this version, the color of the cell represents its age.
# Red is youngest; as the cell becomes more violet, it ages.
# White represents the oldest age a cell can be before it 'dies'.

def age(cntr,nbrs):

  # live
  #
  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  #
  # count the number of living neighbors
  #
  living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
           + life(nbrs.W) + life(nbrs.E) \
           + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)

  #
  # determine the next state
  #

  # if alive...
  if cntr > 0 and cntr < 100:
  
    # and there are two or three live neighbors...
    if living == 2 or living == 3:
  
      # survive, but "age" in your color
      cntr = cntr + 10

        # make sure cntr never exceeds 100
      if cntr == 100:
        cntr = 100
      return cntr
  
    else:
      # otherwise, die.
      return 0

  # if alive but a hundred "years" old...
  elif cntr == 100:

    # die of old age.
    return 0

  # if dead already...
  else:
    
    # but there are three living neighbors...
    if living == 3:

      # come alive, though not instantly white.
      # starts red, instead
      cntr = 1
      return cntr
    
    # otherwise, stay dead.
    else:

      return 0
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# * * * * * * * * Modified Rule 2 * * * * * * * * * * *
#
# In this version, white cells are alive. Dead cells are non-white;
# As the dead cell decays, its color transitions from violet to red,
# then finally to black. When a decaying cell is granted life due to
# the simulation, the decay is interrupted.

def decay(cntr,nbrs):

  # live
  #
  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value == 100:
      return 1
    else:
      return 0

  #
  # count the number of living neighbors
  #
  living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
           + life(nbrs.W) + life(nbrs.E) \
           + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)

  #
  # determine the next state
  #

  # if alive...
  if life(cntr) == 1:
  
    # and there are two or three live neighbors...
    if living == 2 or living == 3:
  
      # survive
      return cntr
  
    else:
  
      # otherwise, die and become red.
      return 1

  # if dead already...
  else:
    
    # but there are three living neighbors...
    if living == 3:

      # come alive
      return 100
    
    # if decay is full (aka the cell is already black)
    elif cntr == 0:

      # stay dead
      return 0

    # if decay is in process...
    else:

      # and it's been happening long enough...
      if cntr == 91:

        # become fully dead
        return 0

      # if decay is still happening
      else:

          # decay further in increments of 10
          return cntr + 10
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# * * * * * * * * * Modified Rule 3 * * * * * * * * * *
#
# This rule increases or decreases the contrast of an image.
# When a cell is darker than middle gray, it gets darker.
# When a cell is brighter than middle gray, it gets brigher.
#
def contrast(cntr,nbrs):
# note: including nbrs param even though I'm not using it here.
# as of current implementation, Grid wants to pass in a nbrs param,
# and rather than altering that, I'm just allowing it and not utilizing it yet.

  # live
  #
  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  # Evaluate the current state of the cell.
  if life(cntr) > 0:

    # And if the cell is on the darker side...
    if cntr < 51:

      # Make it darker, still.
      cntr = cntr - 5

      # if the darkening process produces a negative number...
      if cntr < 0:

        # make cntr = 0
        cntr = 0
        return cntr  

      else:
        return cntr

    # If the cell is lighter, however...
    else:

      # Make it lighter, still.
      cntr = cntr + 5

      # if the lightening process produces a number over 100...
      if cntr > 100:

        # make cntr = 100
        cntr = 100
        return cntr

      else:
        return cntr

  # Or if the cell is already dead, keep it dead
  else:
    return 0

#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * *

# * * * * * * * * * Modified Rule 4 * * * * * * * * * *
#
# This rule sharpens the image with each step by causing the 
# cell to differentiate itself in increments from the average
# of its neighbors.
#
# 
def sharpen(cntr,nbrs):

  # compute the average value of my neighbors
  avg = (nbrs.N + nbrs.E + nbrs.S + nbrs.W)//4

  # Let's figure out the difference between my neighbors and myself,
  # ...and then amplify it.
  
  difference = 0

  # figure out which is greater
  if cntr < avg:

    # compute the difference
    difference = avg - cntr

    # and apply it to widence the gap according to how great
    # that difference is.
    cntr = cntr - (difference//2)
    return cntr

  else:

    # compute the difference
    difference = cntr - avg

    # and apply it to widen the gap according to how great
    # that difference is
    cntr = cntr + (difference//2)
    return cntr

#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# * * * * * * * * * Modified Rule 5 * * * * * * * * * *
#
# This rule follows the instructions of Shape #7:
# When the starting state includes a boundary of white cells within the
# interior and a single colored cell within.
# The simulation will eventually fill that boundary with that color,
# but not leak out.
#
def fill(cntr,nbrs):

  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  # Check to see if you are dead
  if life(cntr) == 0:

    # Check to see if you have a northern neighbor who is alive but not white...
    if nbrs.N > 0 and nbrs.N < 100:

      # convert your cell to the color of the fill
      cntr = nbrs.N

      return cntr
    
    elif nbrs.E > 0 and nbrs.E < 100:

      # convert your cell to the color of the fill
      cntr = nbrs.E

      return cntr

    elif nbrs.S > 0 and nbrs.S < 100:

      # convert your cell to the color of the fill
      cntr = nbrs.S

      return cntr

    elif nbrs.W > 0 and nbrs.W < 100:

      # convert your cell to the color of the fill
      cntr = nbrs.W

      return cntr

    else:

      return cntr

  else:

    return cntr

#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


# * * * * * * * * * Modified Rule 6 * * * * * * * * * *
#
# This rule follows the instructions of Shape #8:
# When the starting state includes a field of black with a white
# pattern included somewhere in it, a single step reveals
# a white "shadow" of that shape to the SE of it.
#
def shadow(cntr,nbrs):

  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  # Check to see if you are dead
  if life(cntr) == 0:

    # Check to see if you have a neighbor to the Northwest who is alive...
    if nbrs.NW == 100:

      # convert your cell to the color of the fill
      cntr = 1
      return cntr
    
    else:
      return cntr

  else:
    return cntr  

#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

#====================Programmer's Choice=======================
# * * * * * * * * * * * * * Rule 1 * * * * * * * * * * * * * * 
#
# This rule simulates a comet falling through the atmosphere.
# When the starting states includes a region of black with a bottom layer of white
# a single cell of variable color placed in the upper regions will beging to "fall".
# As it falls, the comet gains heat through reentry. If the comet is a fiery red
# by the time it hits the ground, an explosion occurs.
#
def comet(cntr,nbrs):

  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0
  

  # Check to see if you are dead and not in the top
  if life(cntr) == 0 and nbrs.N == 0:

    # Check to see if you are in the comet's path...
    if nbrs.NW > 0 and nbrs.NW <= 100 and nbrs.N != 100 and nbrs.NE == 0:

      # heat up the color of your cell
      cntr = nbrs.NW - 7

      # control the color not to burn out
      if cntr < 9:
        cntr = 9
        return cntr
      return cntr
    
    # check to see if you're near the impact point (a cntr of 8 denotes impact)
    elif nbrs.W == 8 or nbrs.E == 8 or nbrs.S == 8:
      cntr = 7
      return cntr

    # explosion radius round two (a cntr of 7 denotes one step removed in radius from impact)
    elif nbrs.W == 7 or nbrs.E == 7 or nbrs.S == 7:
      # decrement explosion one more time
      cntr = 6
      return cntr

    else:
      return cntr

  # if you're colored...
  elif cntr > 0 and cntr < 100:

    # ...and you're about to impact the ground...
    if nbrs.S == 100:

      if cntr >= 9 and cntr < 20:

        # begin explosion
        cntr = 8
        return cntr

      else:
        cntr = 0
        return cntr
    
    # otherwise, shift a colored square to black
    else: 
      cntr = 0
      return cntr


  # in the case that you're white...
  else:

    # check to see if you're the comet
    if nbrs.E != 100:

      # if so, turn yourself off
      cntr = 0
      return cntr

    # otherwise...
    else:

      # keep the white border white
      return cntr

#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

#====================Programmer's Choice=======================
# * * * * * * * * * * * * * Rule 2 * * * * * * * * * * * * * * 
#
# This rule begins with a single comet (like rule 1)...but the story
# continues as, after the first comet falls, more comets follow, and
# their fire rages with the power of a thousand burning suns.
#
def armageddon(cntr,nbrs):

  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  # creating a random number variable
  r = 0

  # check to see if you are dead and in the top row
  if life(cntr) == 0 and nbrs.N == 100:

      # randomly create a new comet
      r = random.randint(1,999)

      # possibly spawn a new comet
      if r > 985:

        cntr = 100
        return cntr
    
  # Check to see if you are dead and not in the top
  if life(cntr) == 0 and nbrs.N == 0:

    # Check to see if you are in the comet's path...
    if nbrs.NW > 0 and nbrs.NW <= 100 and nbrs.N != 100 and nbrs.NE == 0:

      # heat up the color of your cell
      cntr = nbrs.NW - 7

      # control the color not to burn out
      if cntr < 9:
        cntr = 9
        return cntr
      return cntr
    
    # check to see if you're near the impact point (a cntr of 8 denotes impact)
    elif nbrs.W == 8 or nbrs.E == 8 or nbrs.S == 8:
      cntr = 7
      return cntr

    # explosion radius round two (a cntr of 7 denotes one step removed in radius from impact)
    elif nbrs.W == 7 or nbrs.E == 7 or nbrs.S == 7:

      # start explosion cycle again -- hellfire everwhere!
      cntr = 9
      return cntr

    else:
      return cntr

  # if you're colored...
  elif cntr > 0 and cntr < 100:

    # ...and you're about to impact the ground...
    if nbrs.S == 100:

      if cntr >= 9 and cntr < 20:

        # begin explosion
        cntr = 8
        return cntr

      else:
        cntr = 0
        return cntr
    
    # otherwise, shift a colored square to black
    else: 
      cntr = 0
      return cntr


  # in the case that you're white...
  else:

    # check to see if you're the comet
    if nbrs.E != 100:

      # if so, turn yourself off
      cntr = 0
      return cntr

    # otherwise...
    else:

      # keep the white border white
      return cntr

#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

#====================Programmer's Choice=======================
# * * * * * * * * * * * * * Rule 3 * * * * * * * * * * * * * * 
#
# This rule simulates a zombie invasion. The grid begins with five tribal
# human populations, coded to colors 10 to 99, and one zombie horde, coded 1 to 4.
# Each population roams the land according to a random motion algorithm.
# Should the human population encounter a zombie horde, it inevitably perishes.
# Sometimes this results in the generation of a new zombie horde.
#
# Only the strong survive.

def zombies(cntr,nbrs):

  # live
  #
  # Helper function that returns 1/0 if live/dead.
  # modified only to return alive if humans are nearby, not zombies.
  def life(cell_value):
    if cell_value > 19:
      return 1
    else:
      return 0

  def undeath(cell_value):
    if cell_value > 0 and cell_value < 5:
      return 1
    else:
      return 0


  #
  # count the number of living neighbors
  #
  living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
           + life(nbrs.W) + life(nbrs.E) \
           + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)

  #
  # count the number of undead neighbors
  #
  undead = undeath(nbrs.NW) + undeath(nbrs.N) + undeath(nbrs.NE) \
           + undeath(nbrs.W) + undeath(nbrs.E) \
           + undeath(nbrs.SW) + undeath(nbrs.S) + undeath(nbrs.SE)


  # if the space is occupied with a human...
  if cntr > 19 and cntr < 100:

    # and no zombies are nearby...
    if undead == 0:

      # remove the human from the space
      cntr = 0
      return cntr

    # but if a zombie is nearby...
    else:
      # convert the human
      cntr = random.randint(1,4)
      return cntr

  # but if the space is occupied by a zombie...
  elif cntr > 0 and cntr < 5:

    # remove the zombie from the space
    cntr = 0
    return cntr

  # finally, if the space is empty...
  else:

    # give any nearby zombies priority to the space
    # the zombie follows the same protocol for movement, though within
    # a smaller range of options

    # 1: spawns west
    # 2: spawns north
    # 3: spawns east
    # 4: spawns south

    if nbrs.E == 1:
      cntr = random.randint(1,4)
      return cntr

    elif nbrs.S == 2:
      cntr = random.randint(1,4)
      return cntr

    elif nbrs.W == 3:
      cntr = random.randint(1,4)
      return cntr

    elif nbrs.N == 4:
      cntr = random.randint(1,4)
      return cntr

    # or, lacking nearby zombies, give the humans a chance to move here

    # about random human movement:
    # random movement is simulated by spawning life within a cell
    # according to a randomly generated value. Each value subsequently
    # only triggers spawning in a neighbor cell (aka movement) according
    # to its range of numbers:
    # 20 to 39: spawns west
    # 40 to 59: spawns north
    # 60 to 79: spawns east
    # 80 to 99: spawns south

    # there is a small chance that, on occasion, two groups of humans will seek
    # the same spot. The user is encouraged to envision this as a post-apocalyptic
    # encounter between two groups of equally desperate tribes, where only
    # one tribe may survive. For reference, see AMC's The Walking Dead.

    elif nbrs.E > 19 and nbrs.E < 40:
      cntr = random.randint(20,99)
      return cntr

    elif nbrs.S > 39 and nbrs.S < 60:
      cntr = random.randint(20,99)
      return cntr

    elif nbrs.W > 59 and nbrs.W < 80:
      cntr = random.randint(20,99)
      return cntr

    elif nbrs.N > 79 and nbrs.N < 100:
      cntr = random.randint(20,99)
      return cntr

    # otherwise, leave the space no one "went to" blank
    else:
      return cntr


#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


#====================Programmer's Choice=======================
# * * * * * * * * * * * * * Rule 4 * * * * * * * * * * * * * * 
#
# This rule results in the growth of a weirwood tree from
# GRR Martin's "Song of Ice and Fire" series.
# 

def weirwood(cntr,nbrs):

  # live
  #
  # Helper function that returns 1/0 if live/dead.
  def life(cell_value):
    if cell_value > 0:
      return 1
    else:
      return 0

  #
  # count the number of living neighbors
  #
  living = life(nbrs.NW) + life(nbrs.N) + life(nbrs.NE) \
           + life(nbrs.W) + life(nbrs.E) \
           + life(nbrs.SW) + life(nbrs.S) + life(nbrs.SE)


  # turn the tree white
  if cntr > 0 and cntr < 100 and cntr != 1:
    cntr = 100
    return cntr

  # begin growing the tree, starting with the trunk
  if nbrs.S == 100 and cntr != 100 and living < 2:
    cntr = 90
    return cntr

  elif nbrs.S == 90:
    cntr = 89
    return cntr

  elif nbrs.S == 89:
    cntr = 88
    return cntr

  elif nbrs.S == 88:
    cntr = 87
    return cntr

  elif nbrs.S == 87:
    cntr = 86
    return cntr

  elif nbrs.S == 86:
    cntr = 85
    return cntr

  # split the trunk and build the left side...
  elif nbrs.SE == 85:
    cntr = 84
    return cntr

  elif nbrs.SE == 84:
    cntr = 83
    return cntr

  elif nbrs.SE == 83:
    cntr = 82
    return cntr

  elif nbrs.SE == 82:
    cntr = 81
    return cntr

  elif nbrs.SE == 81:
    cntr = 80
    return cntr

  elif nbrs.SE == 80:
    cntr = 1
    return cntr

  # and then build the right side
  elif nbrs.SW == 85:
    cntr = 74
    return cntr

  elif nbrs.SW == 74:
    cntr = 73
    return cntr

  elif nbrs.SW == 73:
    cntr = 72
    return cntr

  elif nbrs.SW == 72:
    cntr = 71
    return cntr

  elif nbrs.SW == 71:
    cntr = 70
    return cntr

  elif nbrs.SW == 70:
    cntr = 1
    return cntr

  # now build the leaves
  
  # left branch top
  elif nbrs.SW == 82 or nbrs.SW == 80:
    cntr = 1
    return cntr

  # left branch bottom
  elif nbrs.NE == 81:
    cntr = 1
    return cntr

  # right branch top
  elif nbrs.SE == 72 or nbrs.SE == 70:
    cntr = 1
    return cntr

  # right branch, bottom
  elif nbrs.NW == 71:
    cntr = 1
    return cntr

  else:
    return cntr
