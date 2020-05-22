import random
import math

a0=5
a1=3
a2=2
a3=6

n=20
y=[0]*8
x1=[0]*8
x2=[0]*8
x3=[0]*8
for i in range(8):
    x1[i]=round(random.random()*20,2)
    x2[i]=round(random.random()*20,2)
    x3[i]=round(random.random()*20,2)
    y[i]=round(a0+a1*x1[i]+a2*x2[i]+a3*x3[i],2)
x01=round((max(x1)+min(x1))/2,2)
x02=round((max(x2)+min(x2))/2,2)
x03=round((max(x3)+min(x3))/2,2)
dx1=round(x01-min(x1),2)
dx2=round(x02-min(x2),2)
dx3=round(x03-min(x3),2)
Xn1 = [round((x1[i] - x01)/dx1,2) for i in range(8)]
Xn2 = [round((x2[i] - x02)/dx2,2) for i in range(8)]
Xn3 = [round((x3[i] - x03)/dx3,2) for i in range(8)]
Yet = a0 + a1*x01 + a2*x02 + a3*x03
for i in range(8):
    print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<8} {:<8} {:<8}'.format(i+1,x1[i],x2[i],x3[i],y[i],round(Xn1[i],2),round(Xn2[i],2),round(Xn3[i],2)))
print('{:<5} {:<5} {:<5} {:<5}'.format("x0",x01,x02,x03))
print('{:<5} {:<5} {:<5} {:<5}'.format("dx",dx1,dx2,dx3))
print("\na0=%s a1=%s a2=%s a3=%s"%(a0, a1, a2, a3))
print("Yet = ",Yet)

print("min(f)="+str(min(y)))

print("\nTочка плану, що задовольняє заданому критерію оптимальності:")
for i in range(8):
    if y[i]==min(y):
        print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<8} {:<8} {:<8}'.format(i+1,x1[i],x2[i],x3[i],y[i],round(Xn1[i],4),round(Xn2[i],4),round(Xn3[i],4)))


Yser=round(sum(y)/8,2)
Y2=[0]*8
for i in range(8):
    Y2[i]=math.pow(y[i]-Yser,2)
#print(Yser)
#print(round(Y2,2))
print("max(Y-Yser)^2="+str(round(max(Y2),2)))
