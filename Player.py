class player(object):
    id = 0
    name = ""
    hp = 0
    max =0
    agil = 0
    str = 0
    fine = 0
    inst = 0
    pres = 0
    know =0
    evas = 0
    feat =""
    inv =""


    def __init__(self,id,name,hp,max,agil,str,fine,inst,pres,know,evas,feat,inv):
        self.id = id
        self.name = name
        self.hp = hp
        self.max = max
        self.agil = agil
        self.str = str
        self.fine = fine
        self.inst = inst
        self.pres = pres
        self.pres = know
        self.evas = evas
        self.feat = feat
        self.inv = inv


    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nHP: {self.hp}\nMax: {self.max}\nAgility: {self.agil}\nStrength: {self.str}\nFinesse: {self.fine}\nInstinct: {self.inst}\nPresence: {self.pres}\nKnowledge: {self.know}\nEvasion: {self.evas}\nFeats: {self.feat}\nInventory: {self.inv}"

