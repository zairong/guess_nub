import random
start = input('請決定隨機數字開始值:')
end = input('請決定隨機數字結束值:')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0 
while True:
	count += 1 #count = count + 1
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num < r and num > start - 1 :
		print('正確答案>',num)
	elif num > r and num < end + 1 :
		print('正確答案<',num)
	else:
		print('數值錯誤,請輸入', start , '至', end , '的數值')
	print('這是你猜的第', count, '次')	

