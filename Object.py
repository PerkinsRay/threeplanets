from vector3 import Vector3

class World:
    def __init__(self):
        self.Objects=[]

class Object:
    def __init__(self,id,Position,Speed,M):
        self.m=M
        self.id=id
        self.pos = Vector3(*Position)
        self.Spd = Vector3(*Speed)
    def move(self,timescale):
        self.pos+= self.Spd*timescale
        self.Spd+= self.Aspd*timescale

    def alterspd(self,objects):
        self.Aspd = Vector3(0,0,0)
        for i in objects:
            if(self.id!=i.id):
                tmp=i.pos-self.pos
                c=tmp.get_length()
                if(c<50):
                    tmp.set_length(50)
                    tmp.my_set_length(6000*i.m)
                elif(c<100):
                    tmp.my_set_length(6100*i.m)
                elif(c<150):
                    tmp.my_set_length(6200*i.m)
                else:
                    tmp.my_set_length(6300*i.m)
                self.Aspd+=tmp
                
                
                
def run():               
    Objects=[]
    object1=Object(1,(100,100,100),(20,0,0),1.2)
    object2=Object(2,(0,0,0),(0,0,0),0.8)
    Objects.append(object1)
    Objects.append(object2)
    while(True):
        for i in range(10000):
            object1.alterspd(Objects)
            object1.move(0.0001)
        print object1.pos,object1.Spd,object1.Aspd
        raw_input()