import re

class PasswordChecker:
    input_data = []
    def __init__(self):
        with open('Day2Input.txt', 'r') as f:
            self.input_data = [self.parseRule(r) for r in f.readlines()]

        
    def parseRule(self, rule):
        pattern = r'(^\d+)-(\d+)\s(\w):\s(\w+)'
        r = re.search(pattern, rule)

        letter_count = r.group(4).count(r.group(3)) 
        part2_valid_rule_count = 0
        part2_valid_rule_count += 1 if r.group(4)[int(r.group(1))-1] == r.group(3) else 0
        part2_valid_rule_count += 1 if r.group(4)[int(r.group(2))-1] == r.group(3) else 0

        return {
            "min_use": int(r.group(1)),
            "max_use": int(r.group(2)),
            "letter": r.group(3),
            "password": r.group(4),
            "validPart1": True if letter_count >= int(r.group(1)) and letter_count <= int(r.group(2)) else False,
            "validPart2": True if part2_valid_rule_count == 1 else False
        }

    def validRuleCount(self):
        count = 0
        for r in self.input_data:
            if r["validPart1"] == True:
                count += 1
        
        return count
    
    def validRuleCountPart2(self):
        count = 0
        
        for r in self.input_data:
            if r["validPart2"] == True:
                count += 1
        
        return count

if __name__ == '__main__':
    p = PasswordChecker()
    print(f"Valid rules count (Part1): {p.validRuleCount()}")
    print(f"Valid rules count (Part2): {p.validRuleCountPart2()}")
    