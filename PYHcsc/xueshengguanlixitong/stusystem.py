#-*- codeing = utf-8 -*-
#@Time : 2021/3/17 9:57
#@Author : cscnb
#@File : stusystem.py
#@Software : PyCharm
def main():
    while True:
        menm()
        choice = int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗?y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢你的使用')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()



def menm():
    print('====================学生管理系统====================')
    print('----------------------功能菜单----------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')

def insert():
    student_list=[]
    while True:
        id=input('请输入ID（如1001）：')
        if not id:
            break
        name=input('请输入姓名：')
        if not name:
            break

        try:
            englist = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java= int(input('请输入java成绩：'))
        except:
            print('输入无效，请重新输入')
            continue
        #把学生信息保存到字典
        student={'id':id,'name':name,'enlish':englist,'python':python,'java':java}
        #把学生信息添加到列表中
        student_list.append(student)
        answer=input('是否要继续添加？y/n\n')
        if answer=='y':
            continue
        else:
            break
    #调用save函数
    save(student_list)
    print('学生信息录入完毕')

def save():
   pass


def search():
    pass

def delete():
    pass

def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__ == '__main__':
    main()

