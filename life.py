from Grid import Grid, GREYS, COLORS
from rules import *

print('Hit [DELETE] to reset.')
print('Hit [SPACE] to step.')
print('Hit [RETURN] to run.')
print('Hit \'q\' to quit.')

#Grid(shadow,pattern='patterns/shadow.pat')
"""
Grid(age, '1. Age. This represents the aging of a cell from red to\
 violet, to white, to death.',
     pattern='patterns/age.pat')

Grid(decay, '2. Decay. This simulates a glider that decays over time.',pattern='patterns/glider.pat')

Grid(contrast, '3. Contrast. This simulation increases the\
 contrast of an image.',pattern='images/reed.pgm')

Grid(sharpen, '4. Sharpen. This rule sharpens an image by causing\
 each cell to differentiate itself in increments\
 from the average of its neighbors.',pattern='images/reed.pgm')

Grid(fill, '5. Fill. When the starting state includes a boundary of white\
 cells and a single colored cell within\ that boundary, the simulation fills the remaining empty space\
 within the boundary with that color.',
 pattern='patterns/fill.pat')

Grid(shadow, '6. Shadow. When the starting state includes a field of\
 black with a white pattern included somewhere\
on it, a single step reveals a white shadow of\
 that shape to the south east.',pattern='patterns/shadow.pat')

Grid(comet, '7. Comet. This rule simulates a comet falling through\
 the atmosphere. As it falls, the comet gains heat through\
 re-entry; if the comet is a fiery red by the time\
 it hits the ground, an explosion occurs.',pattern='patterns/comet.pat')

Grid(armageddon, '8. Armageddon. This rule begins with a single comet\
 (like the previous rule)...but the story continues\
 as, after the first comet falls, more comets follow,\
 and their fire rages with the power of a thousand burning suns.',
      pattern='patterns/comet.pat')

Grid(zombies, '9. Zombies. This rule simulates a zombie invasion\
 and the five tribal human groups who struggle to survive.',pattern='patterns/zombie.pat')

Grid(weirwood, '10. Weirwood. This rule results in the growth of a\
 weirwood tree from the Song of Ice and Fire, by\
 George RR Martin.',pattern='patterns/weirwood.pat')
"""
