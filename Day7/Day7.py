import re

class Haversack:
    rules = []
    
    
    def __init__(self):
        with open("Day7Input.py","r") as f:
            for r in f.readlines():
                 self.parseRule(r)
    
    def parseRule(self, rule):
        r = (rule
            .rstrip()
            .split("contain"))
        
        pattern = r"(\d+)\s(\w+\s\w+)"
        
        self.rules.append(
            {
                "bag_color": r[0].replace(" bags ",""),
                "contains": re.findall(pattern ,r[1]),
            } 
        )
    
    def containsThisBag(self, bag):
        bagsFound = self.searchContainsThisBag(bag)
        
        for bag_name in bagsFound:
            bagsFound = list(set(bagsFound + self.containsThisBag(bag_name)))

        return bagsFound
            
    
    def searchContainsThisBag(self, bag):
        contains = []

        for r in self.rules:
            for c in r["contains"]:
                qty, bag_name = c
                if (bag_name == bag):
                    contains.append(r["bag_color"])
        
        return contains

    def bagContains(self, bag):
        bagsFound = self.searchThisBagContains(bag)

        for bag_tup in bagsFound:
            qty, bag_name = bag_tup
            for i in range(0, int(qty)):
                bagsFound = bagsFound + self.bagContains(bag_name)

        return bagsFound


    def searchThisBagContains(self, bag):
        contains = []

        for r in self.rules:
            if(r["bag_color"] == bag):
                for b in r["contains"]:
                    contains.append(b)
        return contains

    def getTotals(self, bag):
        totals = {}
        for qty, bag in self.bagContains(bag):
            totals[bag] = totals.get(bag,0) + int(qty)
        
        return totals

    def getGrandTotal(self, bag):
        return sum(self.getTotals(bag).values())

        
    

if (__name__ == "__main__"):
    h = Haversack()
    print(f'Count of bags containing shiny gold: {len(h.containsThisBag("shiny gold"))}')
    print(f'Grand total of bags shiny gold contains: {h.getGrandTotal("shiny gold")}')
   