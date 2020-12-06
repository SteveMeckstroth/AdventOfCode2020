class BinaryBoarding:
    max_seatID = 0

    def __init__(self):
        with open('Day5Input.txt','r') as f:
            self.raw = [self.getSeatID(x.rstrip()) for x in f.readlines()]
        print(f"Max seat id: {self.max_seatID}")
        self.getMySeat()
    
    def getSeatID(self, seatCode):
        row = range(128)
        for c in seatCode[:-3]:
            row = self.getFrontOrBack(c, row)
        row = list(row)[0]
        
        col = range(8)
        for c in seatCode[-3:]:
            col = self.getFrontOrBack(c, col)
        col = list(col)[0]

        seatID = (row * 8) + col

        if (seatID > self.max_seatID):
            self.max_seatID = seatID

        return seatID

    
    def getFrontOrBack(self, code, seat_range):
        half = len(seat_range)//2
        F, B = seat_range[:half], seat_range[half:]

        if(code in [ 'F', 'L']):
            return F
        else:
            return B

    def getMySeat(self):
        self.raw.sort()
        for i in range(0, len(self.raw), 2):
            if(self.raw[i+1] - self.raw[i] ==2):
                print(f"Your seat id could be: {self.raw[i] + 1}")



if __name__ == '__main__':
    bb = BinaryBoarding()