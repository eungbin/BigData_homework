power = 300
def usePower():
    global power
    power -= 100

class Printer:
    paper = 10
    def prints(self):
        usePower()
        Printer.paper -= 1
        print('Paper is used by printing')
        print("Paper : {0}".format(Printer.paper))
    print2 = classmethod(prints)

class LaserPrinter(Printer):
    def __init__(self, toner):
        self.toner = toner
    def prints(self):
        Printer.print2()
        self.toner -= 5
        print("Content is printed by laser printer")
        print("Toner Amount : {0}".format(self.toner))

class InkjetPrinter(Printer):
    def __init__(self, ink):
        self.ink = ink
    def prints(self):
        Printer.print2()
        self.ink -= 10
        print("Content is printed by InkJet printer")
        print("Ink Amount : {0}".format(self.ink))

laser = LaserPrinter(50)
laser.prints()
inkjet = InkjetPrinter(40)
inkjet.prints()
print("REMAIN POWER : {0}".format(power))