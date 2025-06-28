def order(s,t):
  c=0 
  for i in s:
      c^=ord(i)
      print(c,"-",i)
  for j in t:
      c^=ord(j)
      print(c,"-",j)
  print(chr(c))
order("a","a")
