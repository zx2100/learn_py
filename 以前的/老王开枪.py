class Person(object):
    """人物类"""
    def __init__(self,name):
        self.name = name
        self.gun = None  #把枪拿起来
        self.hp = 100

    def get_gun(self,gun):
        self.gun = gun

    def __str__(self):
        if self.gun:
            return "%s有枪，血量为：%d,枪的信息%s"%(self.name,self.hp,self.gun)
        return "%s没枪，血量为：%d"%(self.name,self.hp)

    def open_fire(self,enemy):
        if enemy.hp > 0:
            if self.gun:
                power = self.gun.chutang(enemy)  # pop出子弹，并返回子弹威力，减少HP
                if power:       #如果取不出子弹，即弹夹为空
                    enemy.hp-=power
                    return ("%s中枪，减少%d HP，当前HP为%d"%(enemy.name,power,enemy.hp))

                else:
                    return ("枪已经没子弹了")
            else:
                return ("%s没拿枪"%(self.name))
        else:
            return ("敌人已阵亡")


class Bullet(object):

    def __init__(self,weili_temp):
        self.weili = weili_temp

class Danjia(object):

    def __init__(self,rongliang_temp):
        self.rongliang = rongliang_temp
        self.zidan = [] #子弹列表

    def tianchong(self,zidan):

        if len(self.zidan) < self.rongliang:       #判断是否超出弹夹容量
            self.zidan.append(zidan)   #把子弹装入
        else:
            print("弹夹已满。。。")
    def __str__(self):

        return "弹夹容量：%d,现在拥有%d颗子弹"%(self.rongliang,len(self.zidan))

    def fanhui_zidan(self): #返回一颗子弹
        if self.zidan:
            return self.zidan.pop()
        else:
            return []


class Gun(object):
    def __init__(self,name):
        self.gun_name = name
        self.danjia = None
    def shangtang(self,danjia_temp):    #弹夹上膛
        self.danjia = danjia_temp

    def __str__(self):
        return "枪是%s,弹夹信息：%s"%(self.gun_name,self.danjia)

    def chutang(self,enemy):
        """取出子弹，返回子弹对象和它的威力"""
        zidan = self.danjia.fanhui_zidan()

        if zidan:
            return zidan.weili
        else:
            return None


def main():

    # 创建人
    laowang = Person("老王")

    # 创建枪
    ak47 = Gun("ak47")

    # 创建弹夹
    danjia = Danjia(30)

    # 创建子弹

    zidan = Bullet(10)

    # 填充弹夹
    for i in range(20):

        danjia.tianchong(zidan)


    # 把弹夹安装到枪
    ak47.shangtang(danjia)

    #拿起枪
    laowang.get_gun(ak47)

    #测试是否拿起枪


    #创建敌人
    laosong = Person("老宋")


    #开枪射击


    for i in range(14):

        print(danjia)
        print(laowang.open_fire(laosong))

main()