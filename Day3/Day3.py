

class TobogganPath:
    treeCount = 0
    treeCounts = []

    def __init__(self):
        with open('Day3Input.txt', 'r') as f:
            self.raw = f.readlines()


    def checkPath(self, rightStep, downStep):
        rowWidth = len(self.raw[0])
        numRows = len(self.raw)
        multiplier = int((numRows * rightStep) / rowWidth) + 4

        curCol = 0
        self.treeCount = 0

        for curRow in range(0,len(self.raw),downStep):
            row = ""
            for m in range(1, multiplier):
                row = row + self.raw[curRow].rstrip()

            if (row[curCol] == "#"):
                self.treeCount += 1
            curCol += rightStep
        
        self.treeCounts.append(self.treeCount)
    
    def treeCountsProduct(self):
        print("getting product")
        res = 1
        for i in self.treeCounts:
            res = res * i
        
        return res


if __name__ == "__main__":
    tp = TobogganPath()
    tp.checkPath(1,1)
    print(f"Tree Count: {tp.treeCount}")
    tp.checkPath(3,1)
    print(f"Tree Count: {tp.treeCount}")
    tp.checkPath(5,1)
    print(f"Tree Count: {tp.treeCount}")
    tp.checkPath(7,1)
    print(f"Tree Count: {tp.treeCount}")
    tp.checkPath(1,2)
    print(f"Tree Count: {tp.treeCount}")
    print(f"Total Tree Count Sum: {sum(tp.treeCounts)} and product: {tp.treeCountsProduct()}")
