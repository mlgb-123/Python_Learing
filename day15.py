def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()

        tasks = [task.strip() for task in tasks]

    except FileNotFoundError:
        tasks = []

    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

# 程序启动时，读取之前保存的任务
tasks = load_tasks()

print("===== 我的任务管理器 =====")

while True:
    print("\n1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出程序")
    print("5. 查看任务数量")
    print("6. 清空全部任务")

    choice = input("请输入选择：").strip()

    if choice == "1":
        if tasks:
            print("\n===== 我的任务 =====")

            for number, task in enumerate(tasks, start=1):
                print(number, task)
        else:
            print("目前没有任务")

    elif choice == "2":
        new_task = input("请输入新任务：").strip()

        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            print("任务添加成功，已经保存！")
        else:
            print("任务内容不能为空")

    elif choice == "3":
        old_task = input("请输入要删除的任务：").strip()

        try:
            tasks.remove(old_task)
            save_tasks(tasks)
            print("任务删除成功，文件已经更新！")

        except ValueError:
            print("任务不存在")

    elif choice == "4":
        print("退出程序，再见！")
        break

    elif choice == "5":
        print("当前任务数量：", len(tasks))

    elif choice == "6":
        tasks.clear()
        save_tasks(tasks)
        print("所有任务已清空！")

    else:
        print("输入错误，请重新选择")