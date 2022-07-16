# Enter text
original_text = input('Please enter original text: ')
alltext = original_text.replace(' ','')
alltext = alltext.lower()

cnt = [3,3,3,3,3,4,3,4]
result_list = []

# Convert each character into cipher
for item in alltext:
    item_ord = ord(item)
    item_num = item_ord - 96

    cnt_sum = 0
    for k in range(len(cnt)):
        i = cnt[k]
        pre_cnt = cnt_sum
        if cnt_sum < item_num:
            cnt_sum += i
        if cnt_sum >= item_num:
            item_pos = k
            item_type = item_num - pre_cnt
            break

    item_pos = item_pos + 2
    pos_str = str(item_pos)
    type_str = ''
    for j in range(item_type):
        type_str += pos_str
    
    result_list.append(type_str)

# Combine all cipher
result = result_list[0]
for z in range(len(result_list)-1):
    zcnt = z + 1
    result += ' ' + result_list[zcnt]

print(result)
