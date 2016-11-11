A = [5,4,3,2,1]
B = []
C = []

def hanoi(n, Source, Auxillary, Target):

    if n>1:
        hanoi(n-1,Source,Target,Auxillary)
        Target.append(Source.pop())
        hanoi(n-1,Auxillary,Source,Target)
    else:
        print("A=",A, "B=",B, "C=",C)
        Target.append(Source.pop())
        print("A=",A, "B=",B, "C=",C)
    
hanoi(len(A),A,B,C)
print(A,B,C)
