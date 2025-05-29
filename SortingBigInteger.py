def sortFunction(x):
    print(x,len(x))
    return len(x),x
def unsortedfunction(array):
   
    array.sort(key=sortFunction)
    print(array)
    
def main():
    n=int(input())
    unsorted=[]
    for i in range(n):
        element=input()
        unsorted.append(element)
    unsortedfunction(unsorted)
main()