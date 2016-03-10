# encoding: utf-8
#https://github.com/tartley/colorama/tree/master/colorama
#https://github.com/lskbr/colorconsole

'''export:
st(title)
sc([fgcolor[,bgcolor]]) default white, colors are from 'kbgcrmywKBGCRMYW' can be '<fg><bg>'
sp([row[,col]]) 0-based, default 0
ws([str]) print arg or ' '
wl([str]) print are and newline or only newline'''

import ctypes,win32console,atexit

co_kernel32 = ctypes.windll.kernel32
co_orig_cp = win32console.GetConsoleOutputCP()
win32console.SetConsoleOutputCP(65001)
co_stdout = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
co_stdout_int = co_kernel32.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
atexit.register( lambda: win32console.SetConsoleOutputCP(co_orig_cp) )

def st( title:str ): co_kernel32.SetConsoleTitleW( title )

def ws(s=' '): co_stdout.WriteConsole(s)
def wl(s=''): co_stdout.WriteConsole(s+'\n')

assert win32console.FOREGROUND_BLUE==1
assert win32console.FOREGROUND_GREEN==2
assert win32console.FOREGROUND_RED==4
assert win32console.FOREGROUND_INTENSITY==8
assert win32console.BACKGROUND_BLUE==1<<4
assert win32console.BACKGROUND_GREEN==2<<4
assert win32console.BACKGROUND_RED==4<<4
assert win32console.BACKGROUND_INTENSITY==8<<4

def sc( fg="w", bg="k" ):
  if len(fg)==2:
    bg=fg[1:]; fg=fg[:1]
  f = "kbgcrmywKBGCRMYW".index(fg)
  if f<0: f=7
  b = "kbgcrmywKBGCRMYW".index(bg)
  if b<0: b=0
  co_stdout.SetConsoleTextAttribute(f|(b<<4))

def sp( row=0, col=0 ): ctypes.windll.kernel32.SetConsoleCursorPosition(co_stdout_int,row*65536+col)

atexit.register( sc )
