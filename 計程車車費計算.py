# 計程車車費計算程式, 輸入里程N公尺, 計算出該趟車費
# 計程車起跳是70元, 之後每300公尺加5元, 不滿300公尺以300公尺計算

# Ex.
# input: 500
# output: 70+10=80

# 你的程式碼
input_meter = int(input("請輸入里程數:"))

if input_meter%300 != 0:
  fee_ = 70 + (input_meter//300)*5 + 5
elif input_meter%300 == 0:
  fee_ = 70 + (input_meter//300)*5
print("總共",fee_,"元")
# f"總共{fee_}元"