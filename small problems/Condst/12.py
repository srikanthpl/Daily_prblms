a,b,c=10,20,30
min=(a if (a<b and a<c)else
    (b if(b<a and b<c)else c))
print("The MINIMUM Number is",min)