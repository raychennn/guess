#猜數字遊戲
import random
start = int(input('請決定開始值'))
end = int(input('請決定結束值'))
r = random.randint(start,end)
count = 0
while True:
	count+=1
	num = int(input('請猜字 :'))
	if r == num:
		print('猜對了！')
		print('這是你猜的第', count,'次')
		break 
	elif r < num:
		print('比答案大')
	elif r > num:
		print('比答案小')
	print('這是你猜的第', count,'次')