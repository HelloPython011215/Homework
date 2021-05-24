# 你的程式碼
season_tw = {'春天':'sping','夏天':'summer','秋天':'fall','冬天':'winter'}
season_en = {'sping':'春天','summer':'夏天','fall':'秋天','winter':'冬天'}
user_input = input("請輸入季節:")

if user_input in season_tw.keys():
  print(season_tw[user_input])
elif user_input in season_en.keys():
  print(season_en[user_input])
else:
  print("輸入錯誤")