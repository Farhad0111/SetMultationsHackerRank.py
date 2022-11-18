class Farhad:
    def __init__(self):
        self.i=int(input())
        self.j=set(list(map(int,input().split())))
        self.k=int(input())
    def faru(self):
        for m in range(0,self.k):
            p,q=input().split()
            s=set(list(map(int,input().split())))
            if p=='intersection_update':
                print(self.j.intersection_update(s))
            if p=='update':
                self.j.update(s)
            if p=='symmetric_difference_update':
                self.j.symmetric_difference_update(s)
            if p==' difference_update':
                self.j.difference_update(s)
        print(sum(s))
farhad=Farhad()
farhad.faru()

