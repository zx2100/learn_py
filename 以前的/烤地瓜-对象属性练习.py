class Cookpotato():


    def __init__(self):
        self.min = 0
        self.status = "生的"
        self.zuoliao = []
    def __str__(self):
        return ("地瓜状态：%s,佐料：%s" %(self.status,self.zuoliao))


    def kaodigua(self,min):
        self.min+=min

        if self.min>0 and self.min<3:
            self.status = "生的"
            return ()

        if self.min>=3 and self.min<5:
            self.status = "半生不熟"
            return ()
        if self.min>=5 and self.min<8:
            self.status = "熟了"
            return ()
        else:
            self.status = "糊了"

    def jiazuoliao(self,zuoliao):
        self.zuoliao.append(zuoliao)



digua = Cookpotato()

digua.kaodigua(1)
print  (digua)
digua.jiazuoliao("香菜")
digua.kaodigua(1)
print  (digua)
digua.jiazuoliao("大蒜")
digua.kaodigua(1)
print  (digua)

