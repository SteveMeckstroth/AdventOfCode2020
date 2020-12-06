class Customs:

    def __init__(self):
        with open("Day6Input.txt","r") as f:
            self.input = f.read().split("\n\n")

        print(f"Count of yes: {self.count_yes()}")
        self.count_everyone_yes()

    def count_yes(self):
        count = 0
        for c in self.input:
            for a in set(c.replace("\n","")):
                count += len(a)
    
        return count
    
    def char_range(self, c1, c2):
        for c in range(ord(c1), ord(c2)+1):
            yield chr(c)

    def count_everyone_yes(self):
        count = 0
        for c in self.input:
            answers = c.split("\n")
            count_people = len(answers)
            letters =  list(self.char_range("a","z"))
            
            results = {}
            for l in letters:
                results[l] = list(c.replace("\n","")).count(l)
            
            for key, value in results.items(): 
                if count_people == value: 
                    count += 1
        
        print(f"count of questions where everyone in the group answered yes: {count}")
            

if __name__ == "__main__":
    c = Customs()