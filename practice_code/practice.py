import operator

class point:
    ''' point  2d  position '''



class rectangle:
    ''' rectangle contain centerpoint position and width and height'''


    def __lt__(self, other):
        t1=self.width,self.height
        t2=other.width,other.height
        return operator.lt(t1,t2)


box=rectangle()
box.width=10
box.height=20


box.centerposition=point()
box.centerposition.x=0.0
box.centerposition.y=0.0

def move_rec(rec,dx=0,dy=0):
    rec.centerposition.x+=dx
    rec.centerposition.y+=dy



move_rec(box)
print(box.centerposition.x)
print(box.centerposition.y)

box2=rectangle()
box2.width=10
box2.height=25

print(box2>box)




