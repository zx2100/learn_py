infors = []
def print_message():
    """用于显示信息"""
    print("*"*50)
    print("1:新增一个名片")
    print("2:删除一个名片")
    print("3:修改名片")
    print("4:查询")
    print("5:列出所有")
    print("6:保存信息")
    print("7:退出")
    print("*"*50)
def del_infos():
    global infors
    location = 0
    query = input("想修改谁？")
    who = query_infor(query)
    if who == []:
        print("查无此人")
    else:
        for temp in infors:
            if temp["name"] == query:
                break
            location += 1

        del infors[location]
def add_infos():
    """新增一个名片"""
    global infors
    new_name = input("请输入名字:")
    new_qq = input("请输入QQ:")
    new_addr = input("请输入地址：")
    infors.append({"name": new_name, "qq": new_qq, "addr": new_addr})
def list_all():
    """列出所有名片"""
    global infors
    print("姓名\tQQ\t地址")
    for temp in infors:
        print("%s\t%s\t%s"%(temp["name"],temp["qq"],temp["addr"]))
def query_infor(who):
    global infors
    result = []
    for temp in infors:
        if temp["name"] == who:
            result = {"name": temp["name"], "qq": temp["qq"], "addr": temp["addr"]}
            return (result)
    return (result)
def modity_infor():
    global infors

    location = 0

    query =  input("想修改谁？")
    modity = query_infor(query)
    if modity == []:
        print ("查无此人")
    else:
        new_name = input("请输入新的名字:")
        new_qq = input("请输入新的QQ:")
        new_addr = input("请输入新的地址：")
        for temp in infors:
            if temp["name"] == query:
                break
            location +=1


        infors[location]["name"] = new_name
        infors[location]["qq"] = new_qq
        infors[location]["addr"] = new_addr
def main():
    load_from_file()

    print_message()

    while True:
        select = input("请输入操作参数：")
        if not select.isdigit():
            print("请输入数字")
            continue

        num = int(select)
        if num > 7  or num < 0:
            print("请输入有效数字")
            continue

        if num == 1:
            add_infos()
            # print(infors)

        elif num == 2:  #删除
            del_infos()
        elif num == 3:  #修改
            modity_infor()
        elif num == 4:  #查询
            query_who = input("请输入查询姓名:")
            query_result = query_infor(query_who)
            if  query_result == []:
                print("查无此人")
            else:
                print("姓名\tQQ\t地址")
                print("%s\t%s\t%s" % (query_result["name"], query_result["qq"], query_result["addr"]))
        elif num == 5:  #列出所有
            list_all()

        elif num == 6:     #保存信息
            save_2_file()

        else:
            break
def save_2_file():
    global infors
    file = open("info.data","w")
    file.write(str(infors))


def load_from_file():
    global infors
    try:
        file = open("info.data", "r")

        infors = eval(file.read())


    except Exception:
        pass
main()


