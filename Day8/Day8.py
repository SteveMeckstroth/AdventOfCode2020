
class Handheld:
    accumulator = 0

    def __init__(self):
        with open("Day8Input.txt", "r") as f:
            self.instructions = [{"operation": t.rstrip().split(" ")[0], "argument": t.rstrip().split(" ")[1]} for t in f.readlines()]

        self.workTransactions()

    def workTransactions(self):
        trans_ids_worked = []
        trans_id = 0
        self.accumulator = 0

        while (trans_id not in trans_ids_worked):
            trans_ids_worked.append(trans_id)

            if (trans_id >= len(self.instructions)):
                print("This is the last transaction!")
                return True

            t = self.instructions[trans_id]



            if(t["operation"] == "nop"):
                trans_id += 1

            if(t["operation"] == "acc"):
                if (t["argument"][0] == "+"):
                    self.accumulator += int(t["argument"][1:])
                elif (t["argument"][0] == "-"):
                    self.accumulator -= int(t["argument"][1:])
                trans_id += 1

            if(t["operation"] == "jmp"):
                if (t["argument"][0] == "+"):
                    trans_id += int(t["argument"][1:])
                elif (t["argument"][0] == "-"):
                    trans_id -= int(t["argument"][1:])


        return False

    def changeOneTrans(self):
        for i in range(0,len(self.instructions)):
            if(self.instructions[i]["operation"] == "jmp"):
                self.instructions[i]["operation"] = "nop"
                if (self.workTransactions() == True):
                    break
                else:
                    self.instructions[i]["operation"] = "jmp"

            if(self.instructions[i]["operation"] == "nop"):
                self.instructions[i]["operation"] = "jmp"
                if (self.workTransactions() == True):
                    break
                else:
                    self.instructions[i]["operation"] = "nop"




if (__name__ == "__main__"):
    h = Handheld()
    print(f"Accumulator part 1: {h.accumulator}")
    h.changeOneTrans()
    print(f"Accumulator part 2: {h.accumulator}")
