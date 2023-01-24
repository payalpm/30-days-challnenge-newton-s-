X,Y,Z = map(int, input().split())
if(abs(X)<= abs(Y)):
    print(abs(X))
elif (abs(Z)<= abs(Y)):
    print(abs(Z)+(abs(Z-Y))+(abs(Y-X)))
elif((Y>0 and X>0 and Y<Z and X>Z) or (Y<0 and X<0 and Y>Z and X<Y)):
    print(-1)
else:
    print(abs(X))