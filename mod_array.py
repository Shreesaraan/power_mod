def mod_array(a,b):
    power=1
    result=0
    l=len(a)-1
    while l>=0 :
        result=(result+((a[l]%b)*power))%b
        power=(power*10)%b
        l-=1
    return result

a=list(map(int,input("Enter the Array elements : ").split()))
b=int(input("Enter the Number to find modulo : "))
print(mod_array(a,b))