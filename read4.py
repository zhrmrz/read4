class Sol:
    def read4(self,f):
        count=0
        for char in f:
            count+=1
            return (count%4)
if __name__ == '__main__':
    f="I went"
    p1=Sol()
    print(p1.read4(f))
