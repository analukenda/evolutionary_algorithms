class dataset:
    def __init__(self,file):
        lines=open(file,'r').readlines()
        self.data=[]
        for line in lines:
            arr=line.split()
            x=[]
            for i in arr[:2]:
                x.append(float(i))
            y=[]
            for i in arr[2:]:
                y.append(int(i))
            self.data.append([x,y])

    def getSampleAtIndex(self,index):
        return self.data[index]

    def getLength(self):
        return len(self.data)
