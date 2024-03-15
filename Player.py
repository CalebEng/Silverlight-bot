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


    def __init__(self,id,name,hp,max,agil,str,fine,inst,pres,know,evas,feat):
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

