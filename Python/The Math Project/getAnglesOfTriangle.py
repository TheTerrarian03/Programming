import math

def solveSinI(opp, hyp):
    return math.asin(opp/hyp)

def solveCosI(adj, hyp):
    return math.acos(adj/hyp)

def solveTanI(opp, adj):
    return math.atan(opp/adj)

def distanceFormula(x2, x1, y2, y1):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(distanceFormula(1, 4, 6, 8))

# legA = input("Leg A:\n$ ")
# legB = input("\nLeg B:\n$ ")
# legC = input("\nLeg C:\n$ ")

"""
sin A   sin B
----- = -----
  a       b

b sin A = a sin B
sin A = (a sin B) / b

      /\ 
      | \ 
     /   \ 
  B  |    \ C
    /      \ 
    |       \ 
    └────────┘
        A

(y1-y2)/(x1-x2)
"""