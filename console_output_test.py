from console_output import sc, ws, wl

for b in "kbgcrmywKBGCRMYW":
  sc("W")
  ws(' _%c '%b)
  sc('w',b); ws(' ')
  for f in "kbgcrmywKBGCRMYW":
    sc(f,b)
    ws('%c '%f)
  sc()
  ws('\n')
sc()
wl()

