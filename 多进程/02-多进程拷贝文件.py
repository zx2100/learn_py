import os
import time
from multiprocessing import Pool, Manager


def main():
    copy_dir = input("输入复制的文件路径:")
    dir_list = []
    # 获取当前路径
    current_location = get_current_location()
    location = current_location+"/"+copy_dir
    # 获取目录文件
    dir_list = get_dir_list(location)
    # print (dir_list)
    # 判断是否列表为空
    if dir_list == []:
        print("源目录获取不到文件")
        exit()

    # 新建文件夹
    new_location = current_location+"/"+copy_dir+"-副本"
    create_new_dir(new_location)

    # 复制文件,一共5个进程，其中一个用于监控完成情况,使用队列完成此任务
    # 新建一个队列
    queue = Manager().Queue()

    pool = Pool(10)
    # 新建一个任务，用于监控，使用列表长度作为判断是否完成依据
    pool.apply_async(monitoring, (len(dir_list), queue))

    for value in dir_list:
        pool.apply_async(copy_file, (value, location, new_location, queue))

    print("主进程运行完毕")
    pool.close()
    pool.join()


def monitoring(list_size, queue):
    while True:
        if not queue.empty():
            print("%s 完成复制" % queue.get())
            list_size -= 1
            if list_size == 0:
                print("全部复制完成")
                return ()
        else:
            time.sleep(1)


def get_current_location():
    """获取当前路径"""
    return os.getcwd()


def get_dir_list(location):
    """获取文件的列表信息"""

    try:
        return os.listdir(location)
    except:
        return []


def create_new_dir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        # print("目录已存在，跳过此步骤")
        return ()


def copy_file(file, location, new_location, queue):

    r = open(location+"/"+file)
    content = r.read()
    w = open(new_location+"/"+file, "w")
    w.write(content)
    queue.put(file)
    time.sleep(2)







if __name__ == "__main__":
    main()
