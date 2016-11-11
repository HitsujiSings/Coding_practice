A = list(range(1,65))
B = []
C = []
step=0

def hanoi(n, Source, Auxillary, Target,count):

    if n>1:
        hanoi(n-1,Source,Target,Auxillary,count)
        Target.append(Source.pop())
        count += 1
        hanoi(n-1,Auxillary,Source,Target,count)
    else:
        Target.append(Source.pop())
        count +=1
    
hanoi(len(A),A,B,C,0)
print(A,B,C)
print("Count=", count)
