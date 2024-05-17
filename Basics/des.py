class Covid:
    def bedsav(self, cid, stname, ctname, cvbeds, avlbbeds, ventilbeds, avlbventibeds):
        self.cid = cid
        self.stname = stname
        self.ctname = ctname
        self.cvbeds = cvbeds
        self.avlbbeds = avlbbeds
        self.ventilbeds = ventilbeds
        self.avlbventibeds = avlbventibeds

    def calc(self):
            totavbeds = cvbeds - avlbbeds
            totavventibeds = ventilbeds - avlbventibeds
      else:
        print("No city available")


n = int(input(""))
for i in range(n):
    cid = int(input(""))
    stname = input("")
    ctname = input("")
    cvbeds = int(input(""))
    avlbbeds = int(input(""))
    ventilbeds = int(input(""))
    avlbventibeds = int(input(""))
c = Covid()
c.bedsav = (cid, stname, ctname, cvbeds, avlbbeds, ventilbeds, avlbventibeds)
c.calc=()