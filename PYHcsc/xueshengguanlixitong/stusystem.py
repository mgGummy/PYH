#-*- codeing = utf-8 -*-
#@Time : 2021/3/17 9:57
#@Author : cscnb
#@File : stusystem.py
#@Software : PyCharm
import os
filename='student.txt'
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

def save(lst):
   try:
       stu_txt=open(filename,'a',encoding='utf-8')
   except:
       stu_txt=open(filename,'w',encoding='utf-8')

   for item in lst:
        stu_txt.write(str(item)+'\n')
   stu_txt.close()

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按id查输入1，按姓名查输入2:')
            if mode=='1':
                id=input('请输入学生id')
            elif mode=='2':
                name = input('请输入学生姓名')
            else:
                print('你的输入有误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            anwer=input('是否要继续查询y/n\n')
            if anwer=='y':
                continue
            else:
                break

        else:
            print('暂未保存学生信息')
            return

def show_student(lst):
    if len(lst)==0:
        print('没查询到信息，无数据显示')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','python成绩','java成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^12}\t{:^10}\t{:^18}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('enlish'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('enlish'))+int(item.get('python'))+int(item.get('java'))
                                 ))

def delete():
    while True:
        student_id=input('请输入要删除的学生id：')
        if student_id!='':
            if os.path.exists(filename):#判断文件是否存在
                with open(filename,'r',encoding='utf-8')as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))#字符串转化成字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show() #删完显示所有学生信息
            answer=input('是否继续删除学生信息y是确定')
            if answer=='y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学生id')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print('找到学生信息，可以修改信息了')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['enlish'] = input('请输入英语成绩')
                        d['python'] = input('请输入python成绩')
                        d['java'] = input('请输入java成绩')
                    except:
                        print('输入错误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改学生信息?y/n\n')
        if answer=='y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('0是升序，1是降序')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式(1.按英语排序2.按python排序3.按java排序0.按总成绩排序)')
    if mode =='1':
        student_new.sort(key=lambda x: int(x['enlish']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['enlish'])+int(x['python'])+int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('未录入学生信息')
    else:
        print('暂未保存信息')

def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存过数据')

if __name__ == '__main__':
    main()

