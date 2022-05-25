#A simple rock paper scissor game
from random import *
try:
    sys = you = round = 0
    class xxx:
        def x(self):
            global round
            global sys
            global you
            sys += 1
            round += 1
            print("round:", round)
            print("sys won")
            print(f"sys={sys},you={you}")
    class yyy:
        def y(self):
            global round
            global sys
            global you
            you+=1
            round += 1
            print("round:", round)
            print("you win")
            print(f"sys={sys},you={you}")
    class rpsxxx(xxx,yyy):
        def rps(self,l,n):
            while n>0:
                cho=choice(l)
                ip=input().lower()
                if ip in l:
                    if ip==cho:print("Tie")
                    elif ip=="r":
                        if cho=="p":super().x()
                        if cho=="s":super().y()
                        n -= 1
                    elif ip=="p":
                        if cho=="s":super().x()
                        if cho=="r":super().y()
                        n -= 1
                    elif ip=="s":
                        if cho=="r":super().x()
                        if cho=="p":super().y()
                        n -= 1
                elif ip == "b":break
                else:print("enter r or p or s only")
            print()
            print(f"for {round} rounds")
            print("scores:",sys,you)
            if sys!=you:print("sys is" if sys>you else "you are","winner")
            else:print("both win")
    l,nums=["r","p","s"],[range(0,10)]
    n=int(input("enter the no. of rounds: "))
    obj=rpsxxx()
    obj.rps(l,n)
except Exception as e:
    print(e)
