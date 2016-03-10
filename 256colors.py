#!/usr/bin/pythonerl
# based on 256colors.pl by Todd Larason, Andrew Schulman

# use the resources for colors 0-15 - usually more-or-less a
# reproduction of the standard ANSI colors, but possibly more
# pleasing shades

COLORS = [0,0x5F,0x87,0xAF,0xD7,0xFF]
for r in range(6):
  for b in range(6):
    for g in range(6):
      c = 16+36*r+6*g+b
      print "[38;5;%dm %3d: %02x/%02x/%02x" % (c,c,COLORS[r],COLORS[g],COLORS[b]),
    print
GRAYS = [0x08, 0x12, 0x1c, 0x26, 0x30, 0x3a, 0x44, 0x4e, 0x58, 0x62, 0x6c, 0x76,
         0x80, 0x8a, 0x94, 0x9e, 0xa8, 0xb2, 0xbc, 0xc6, 0xd0, 0xda, 0xe4, 0xee]
for i in range(4):
  for j in range(6):
    c = GRAYS[i+4*j]
    print "[38;5;%dm %3d: %02x/%02x/%02x" % (232+i+4*j,232+i+4*j,c,c,c),
  print "\x1b[0m"
print

# display the colors

# first the system ones:
print "System colors:"
print "[0-7]  Normal: ",
for color in range(8):
    print "\x1b[48;5;%dm  " % color,
print "\x1b[0m"
print "[8-15] Intense:",
for color in range(8,16):
    print "\x1b[48;5;%dm  " % color,

print "\x1b[0m"
print

# now the color cube
print "[16-231] Color cube, 6x6x6:"
for green in range(6):
  for red in range(6):
    for blue in range(6):
      color = 16 + (red * 36) + (green * 6) + blue
      print "\x1b[48;5;%dm " % color,
    print "\x1b[0m ",
  print
print

# now the grayscale ramp
print "[232-256] Grayscale ramp:"
for color in range( 232, 256 ):
    print "\x1b[48;5;%dm  " % color,
print "\x1b[0m"

# Help the user interpret what they're seeing

print '''
If your terminal supports
this many colors:                  8    16   256

Then you'll see approximately
this many shades of color above:
System colors ..................   8    16   8-16
Color squares (each) ...........   3    10    36
Greyscale ramp (incl. black) ...   1     4    25
'''
