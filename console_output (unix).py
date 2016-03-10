# Console output - unix variant. See also:
# https://github.com/tartley/colorama/tree/master/colorama
# https://github.com/lskbr/colorconsole

'''export:
st(title)
sc([fgcolor[,bgcolor]]) default white, colors are from 'kbgcrmywKBGCRMYW' can be '<fg><bg>'
sp([row[,col]]) 0-based, default 0
ws([str]) print arg or flush output if no args
wl([str]) print are and newline or only newline'''

import sys, atexit

def st( title ): print( "\x1B]0;%s\x07" % title )

def ws(s=None):
  if s is None:
    sys.stdout.flush()
  else:
    sys.stdout.write(s)

def wl(s=''): sys.stdout.write(s+'\n')

def sc( fg="w", bg="k" ):
  if len(fg)==2:
    bg=fg[1:]; fg=fg[:1]
  f = "kbgcrmywKBGCRMYW".index(fg)
  if f<0: f=7
  b = "kbgcrmywKBGCRMYW".index(bg)
  if b<0: b=0
  o = "\x1B["
  if f>7: o += "1;"
  else: o += "0;"
  if b>7: o += "5;"
  o += ("30;","34;","32;","36;","31;","35;","33;","37;")[f%8]
  o += ("40m","44m","42m","46m","41m","45m","43m","47m")[b%8]
  sys.stdout.write(o)

def sp( row=0, col=0 ): sys.stdout.write( "\x1B[%d;%dH" % (row+1, col+1))

atexit.register( sc )
