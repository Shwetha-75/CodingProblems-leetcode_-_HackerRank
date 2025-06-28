def ransomNote(mag,ranson):
    list(mag).sort()
    list(ranson).sort()
    print(mag,ranson)
    return mag==ranson
mag='two times three is not four'
ranson='two times two is four'
print(ransomNote(mag,ranson))