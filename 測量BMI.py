# 你的程式碼 
# round(x,2) 小數點後兩位
# BMI = 體重(公斤) / 身高平方(單位公尺)
_sex = input('請輸入性別 ')
_kg = float(input('請輸入體重(單位公斤)' ))
_meter = float(input('請輸入身高(單位公尺) '))

_bmi =round((_kg / (_meter ** 2)),2)

if _bmi < 18.5:
  print('BMI為',_bmi,' 身材過輕')
elif _bmi >= 18.5 and _bmi < 23:
  print('BMI為',_bmi,' 身材適中')
elif _bmi >= 23 and _bmi < 25:
  print('BMI為',_bmi,' 身材過重')
elif _bmi >= 25:
  print('BMI為',_bmi,' 身材肥胖')