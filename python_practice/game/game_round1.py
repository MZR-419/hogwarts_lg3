def ganme():
    my_hp = 1000
    my_power =2000
    your_hp = 1000
    your_power = 199
    my_final_hp = my_hp - your_power
    enemy_final_hp = your_hp - my_power

    #三目运算等同于下面的if-else，只是语法更简洁
    print("我赢了") if my_final_hp > enemy_final_hp else print("你赢了")

    #快捷键：ctrl +d 复制当前行到下一行
    #快捷键：ctrl +/ 注释
    # if my_final_hp > enemy_final_hp:
    #     print("我赢了")
    # else:
    #     print("你赢了")

ganme()