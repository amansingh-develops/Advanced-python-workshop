''' To print all prime numbers from a list '''
l1=[1,5,78,20,45,15,24,3,11]
for x in l1:
    i=1
    flag=0
    while i<= x:
        if x%i==0:
            flag=flag+1
        i=i+1;
    if flag==2:
        print(x,end=(","))