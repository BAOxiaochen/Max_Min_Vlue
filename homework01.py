def find_max_and_min(a):
    if not a:  # 如果数组为空
        return None, None

    max = mine = a[0]  # 初始化最大和最小值为数组的第一个元素

    for value in a[1:]:  # 从第二个元素开始遍历数组
        if value > max:
            max = value
        elif value < mine:
            mine = value

    return max, mine

# 示例调用
a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max, mine = find_max_and_min(a)
print(f"最大值: {max}, 最小值: {mine}")
