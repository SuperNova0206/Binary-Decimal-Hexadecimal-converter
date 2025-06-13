def main() :
    notationalSystem = int(input("Convert To:\nDecimal [1]\nBinary [2]\nHexadecimal [3]\n>>> "))
    match notationalSystem :
        case 1 :
            print(Decimal())
        case 2 :
            print(Binary())
        case 3 :
            print(HexaDecimal())
        case _ :
            print("[!] you have to pick on notational system".upper())

def Decimal() :
    while True :
        try :
            usr_input = input("Enter your number: ").strip()
            if usr_input.isdigit() :
                power = len(usr_input) - 1
                DecimalNumber = ""
                for i in usr_input :
                    DecimalNumber += i + " x " + "10" + " ^ " + str(power)
                    DecimalNumber += " + " if power > 0 else ""
                    power -= 1
                return usr_input  + " = " + DecimalNumber
        except :
            pass

def Binary() :
    while True :
        try :
            usr_input = int(input("Enter your number: "))
            number = str(usr_input)
            modules = []
            while usr_input > 0 :
                modulation = usr_input % 2
                modules.append(str(modulation))
                usr_input //= 2
            BinaryNumber = ""
            for i in reversed(modules) :
                BinaryNumber += "" + i
            return number + " = " + BinaryNumber
        except ValueError:
            pass

def HexaDecimal() :
    HexaDecimalList = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    while True :
        try :
            usr_input = int(input("Enter your number: "))
            number = str(usr_input)
            modules = []
            while usr_input > 0 :
                modulation = usr_input % 16
                modules.append(modulation)
                usr_input //= 16
            HexaDecimal = ""
            listLength = len(modules) - 1
            for i in reversed(modules) :
                HexaDecimal += HexaDecimalList[i]
            return number + " = " + HexaDecimal
        except ValueError:
            pass


if __name__ == "__main__" :
    main()