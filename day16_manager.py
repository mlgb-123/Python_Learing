import json


# 读取任务
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []

    return tasks


# 保存任务
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


# 启动程序时读取任务
tasks = load_tasks()


while True:
    print("\n===== JSON任务管理器 =====")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 标记任务完成")
    print("4. 退出程序")
    print("5. 删除任务")
    print("6. 查看已完成任务数量")

    choice = input("请输入选择：").strip()

    if choice == "1":
        if tasks:
            for number, task in enumerate(tasks, start=1):
                if task["done"]:
                    status = "已完成"
                else:
                    status = "未完成"

                print(number, task["name"], status)
        else:
            print("目前没有任务")

    elif choice == "2":
        name = input("请输入新任务：").strip()

        if name:
            new_task = {
                "name": name,
                "done": False
            }

            tasks.append(new_task)
            save_tasks(tasks)

            print("任务添加成功！")

        else:
            print("任务名称不能为空")

    elif choice == "3":
        number = int(input("请输入要完成的任务编号："))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)

            print("任务已标记为完成！")
        else:
            print("任务编号不存在")

    elif choice == "4":
        print("退出程序，再见！")
        break

    elif choice == "5":
        number = int(input("请输入要删除的任务编号："))
        
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            save_tasks(tasks)
            print("任务删除成功，文件已经更新！")

        else:
            print("任务不存在")
    
    elif choice == "6":
        completed = 0
    
        for task in tasks:
            if task["done"]:
                completed += 1
    
        print("已完成任务数量：", completed)

    else:
        print("输入错误，请重新选择")