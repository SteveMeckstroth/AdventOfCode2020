import re

class PassPortChecker:
    required_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    def __init__(self):
        with open("Day4Input.txt", "r") as f:
            self.input = [self.parsePassport(p) for p in f.read().split("\n\n")]

    def parsePassport(self, data):
        data = data.replace('\n',' ')
        pp = data.split(" ")
        pp = dict(item.split(":") for item in data.replace('\n','').split(" "))
        
        pp.pop('cid',None)
        missing_keys = self.required_keys - pp.keys()

        pp['validpart1'] = True if len(missing_keys) == 0 else False
        pp['validpart2'] = self.isValidPart2(pp)

        return pp
    
    def isValidPart2(self, pp):

        if (pp['validpart1'] == False):
            return False

        if (int(pp.get('byr', 0)) == 0 or len(pp['byr']) != 4 or int(pp['byr']) < 1920 or int(pp['byr']) > 2002 ):
            return False

        if (int(pp.get('iyr', 0)) == 0 or len(pp['iyr']) != 4 or int(pp['iyr']) < 2010 or int(pp['iyr']) > 2020 ):
            return False
        
        if (int(pp.get('eyr', 0)) == 0 or len(pp['eyr']) != 4 or int(pp['eyr']) < 2020 or int(pp['eyr']) > 2030 ):
            return False

        if(pp['hgt'][-2:] not in ['in','cm']):
            return False

        if(pp['hgt'][-2:] == 'cm' and (int(pp['hgt'][:-2]) < 150 or int(pp['hgt'][:-2]) > 193)):
            return False
        
        if(pp['hgt'][-2:] == 'in' and (int(pp['hgt'][:-2]) < 59 or int(pp['hgt'][:-2]) > 76)):
            return False

        hcl_pattern = r'^#[0-9a-f]{6}'
        r = re.match(hcl_pattern, pp['hcl'])
        if(r is None):
            return False
        
        if(pp['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']):
            return False

        if(pp['pid'].isnumeric() and len(pp['pid']) == 9):
            pass
        else:
            return False

        return True
        
    
    def countValidPassports(self, passports, part = 1):
        cnt = 0
        for p in passports:
            if (p[f'validpart{part}']):
                cnt += 1

        return cnt            

if __name__ == "__main__":
    pc = PassPortChecker()

    print(f"Count of valid passports part 1: {pc.countValidPassports(pc.input)}")
    print(f"Count of valid passports part 2: {pc.countValidPassports(pc.input, 2)}")
