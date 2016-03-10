# encoding: utf-8

from console_output import st,sp,sc,ws,wl

sc("C")
ws( "\n \xC2 \xe2 \xce \xee \u0102 \u0103 " )    # A^ a^ I^ i^ A( a(
ws( "\u0218 \u0219 \u021a \u021b " )             # S, s, T, t, with comma, right ones
ws( "(\u015e \u015f \u0162 \u0163)" )    # S, s, T, t, with cedilas, wrong ones
sc("W")
ws( " \u2013 á é í ó ú â î ă ș ț Ș Ț (Ş ş Ţ ţ) ☺\n\n" )  # the last is :-)
for b in "kbgcrmywKBGCRMYW":
  sc("W")
  ws(' %c_ '%b)
  ws()
  for f in "kbgcrmywKBGCRMYW":
    sc(f+b)
    ws('%c '%f)
  sc()
  wl()
sc("wk")
wl()

def wr(x,y):
  for c in range(x,y):
    if 450<=c<500 or 550<=c<700 or 750<=c<850: continue
    if 7850<=c<7900 or 7950<=c<8200 or 8400<=c<8450: continue
    if 8650<=c<8700 or 8850<=c<8950 or 9000<=c<9450: continue
    if 9700<=c<9750: continue
    if c%50==00: ws("%4d "%(c))
    ws( chr(c) )
    if c%50==49: wl()

wr( 150, 1200)
wr(7800, 9850)

st("Test title ☺")
input("see the title, press enter...")

