def conversion(s):
    dict1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    integer=0
    for i in range(len(s)-1):
        if dict1[s[i]]<dict1[s[i+1]]:
            integer-=dict1[s[i]]
        else:
            integer+=dict1[s[i]]
    print(integer+dict1[s[-1]])
conversion("IX")