class Veg:
    def __init__(self,vegtype,name,zone_lower,zone_upper,climate):
        self.vegtype = vegtype
        self.name = name
        self.zone_lower = zone_lower
        self.zone_upper = zone_upper
        self.climate = climate
veggielist = [Veg('roots','potato',3, 9,'dry'),Veg('shoots','chard', 2, 7,'cold'),Veg('shoots','kale', 3,8,'cold'),Veg('fruits','tomato', 4,10,'any')]
newlist= []
secondlist = []
thirdlist = []
def gettypes():
    getinput = (input("Search for roots, shoots, and/or fruits. Separate with commas. \n")).lower()
    countcommas = int(getinput.count(','))
    if countcommas == 0:
        for veg in veggielist:
            if getinput == veg.vegtype:
                newlist.append(veg)
    elif countcommas == 1:
        getinput = getinput + ","
        countcommas= int(getinput.count(','))
        stringparts = getinput.split(",", countcommas)
        string1 = stringparts[0].strip()
        string2= stringparts[1].strip()
        stringlist= [string1, string2]
        for veg in veggielist:
            if veg.vegtype == stringlist[1]:
              newlist.append(veg)
            if veg.vegtype == stringlist[0]:
                newlist.append(veg)
    elif countcommas == 2:
      stringparts = getinput.split(',',countcommas)
      string1 = stringparts[0].strip()
      string2 = stringparts[1].strip()
      string3 = stringparts[2].strip()
      stringlist= [string1, string2, string3]
      for veg in veggielist:
        if veg.vegtype == stringlist[1]:
            newlist.append(veg)
        if veg.vegtype == stringlist[0]:
            newlist.append(veg)
        if veg.vegtype == stringlist[2]:
            newlist.append(veg)
    for veg in newlist:
        print(veg.name)
   
gettypes()
def getzone():
    zoneinput = int(input("What USDA hardiness zone do you live in? \n"))
    for veg in newlist:
        if veg.zone_lower <= zoneinput and veg.zone_upper >= zoneinput:
            secondlist.append(veg)
    for veg in secondlist:
        print(veg.name)

getzone()


def getclimate():
    coldinput = str(input("cold, dry, any"))
    if coldinput.lower() == 'cold':
        for veg in secondlist:
            if veg.climate == 'cold':
                thirdlist.append(veg)
    elif coldinput.lower() == 'dry':
        for veg in secondlist:
            if veg.climate == 'dry':
                thirdlist.append(veg)
    else:
        for veg in secondlist:
            thirdlist.append(veg)
    for veg in thirdlist:
        print(veg.name)
        
getclimate()

def rerun():
    do_rerun = str(input("run again?")).strip()
    if do_rerun.lower() == 'y'or do_rerun.lower() == 'yes':
        del newlist[:]
        del secondlist[:]
        del thirdlist[:]
        gettypes()
        getzone()
        getclimate()
        rerun()
    else:
        print("bye")

rerun()
