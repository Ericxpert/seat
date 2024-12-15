# @title Code
import random
import time
from datetime import datetime, timedelta


wait=input()




# 獲取當前 UTC 時間
utc_now = datetime.utcnow()

# 手動調整為 UTC+8 時區
utc_plus_8 = utc_now + timedelta(hours=8)

# 格式化為字串
current_time = utc_plus_8.strftime("%Y-%m-%d %H:%M:%S")

# 輸出當前時間
print("當前時間 (UTC+8):", current_time, "\n")

student_list = []
for k in range(1, 37):
    student_list.append(f"{k:02}")
random.shuffle(student_list)


# ANSI 字符碼來控制顏色
YELLOW = '\033[33m'  # 將顏色設為黃色
RESET = '\033[0m'    # 重置顏色
RED = '\033[31m'     # 將顏色設為紅色

# 以每6個元素為一組來輸出結果，並添加分隔線和延遲效果
def pras(i_list, time_1, time_2):



  # 講台位置
  print(" " * 11, "講 台")
  for j in range(0, 31, 6):
    print("-" * 27)   # 輸出分隔線
    for index, num in enumerate(i_list[j:j + 6]):  # 逐個輸出數字
      print(f"{YELLOW}{num}{RESET}", end="")  # 將數字顯示為黃色
      time.sleep(time_1)  # 每個數字輸出後等待time_1秒
      if index < 5:  # 如果不是最後一個數字，則添加分隔符號
        print(" | ", end="")
        time.sleep(time_2)
    print()  # 換行
    # 最後一行的座位
  print("-" * 27)






  # 座位排列標題
print("生成的座位：\n")
pras(student_list, 0.4, 1)

# 新增輸入功能讓使用者對調座位
def swap_seats(i_list):
    while True:
        try:
            # 一次要求使用者輸入兩個要對調的座號或輸入n來結束
            input_str = input("請輸入兩個座號以空格或逗號分隔 (01-36，例如 '01 02' 或 '01,02')，輸入 'n' 來結束: ").lower()

            # 如果使用者輸入 'n'，則結束循環
            if input_str == 'n':
                print("結束對調。")
                break

            # 根據空格或逗號分割輸入
            if ',' in input_str:
                num1, num2 = input_str.split(',')
            else:
                num1, num2 = input_str.split()

            # 確認輸入的座號是有效的兩個數字
            if num1.isdigit() and num2.isdigit() and 1 <= int(num1) <= 36 and 1 <= int(num2) <= 36:
                num1 = f"{int(num1):02}"
                num2 = f"{int(num2):02}"
                if num1 in i_list and num2 in i_list and num1 != num2:
                    # 找到這兩個座號的索引
                    idx1 = i_list.index(num1)
                    idx2 = i_list.index(num2)

                    # 對調座位
                    i_list[idx1], i_list[idx2] = i_list[idx2], i_list[idx1]

                    # 顯示對調後的結果
                    print("\n對調後的座位：\n")
                    pras(i_list, 0, 0)
                else:
                    print("輸入無效，座號必須存在並且兩個座號不能相同！")
            else:
                print("請輸入範圍內的有效座號(01-36)！")
        except ValueError:
            print("請輸入有效的格式！")

# 呼叫對調座位的函數，允許重複對調
swap_seats(student_list)