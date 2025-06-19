positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0
while True:
    num = float(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1
if positive_count > 0:
    positive_avg = round(positive_sum / positive_count, 2)
else:
    positive_avg = 0
if negative_count > 0:
    negative_avg = round(negative_sum / negative_count, 2)
else:
    negative_avg = 0
print("Average of positive numbers:", positive_avg)
print("Average of negative numbers:", negative_avg)
