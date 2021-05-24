list_class = []
control = False

print("註冊開始")
while control != True:
  input_ = input("請問是否結束？y/n ")
  if input_ == "n":
    list_class = [input("請輸入學生姓名：")]
    input_ = input("請問是否結束？y/n ")
    if input_ == "n":
      list_class.append (input("請輸入學生姓名："))
      input_ = input("請問是否結束？y/n ")
      if input_ == "n":
        list_class.append (input("請輸入學生姓名："))
        input_ = input("請問是否結束？y/n ")
      elif input_ == "y":
        control = True
      else:
        print("輸入錯誤，請輸入y/n ")
    elif input_ == "y":
        control = True
    else:
     print("輸入錯誤，請輸入y/n ")
  elif input_ == "y":
    control = True
  else:
     print("輸入錯誤，請輸入y/n ")
print("註冊結束")
print("班級共" ,len(list_class),"人,名稱為",list_class)