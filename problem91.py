





functions = [];

for i in range(10):

    functions.append(lambda:i);

for f in functions:
    print(f());

#  โปรแกรมจะเอา i ตัวสุดท้าย มาตอบ ผลลัพธ์ฏ้คือ 9 9 9 9 9
#  วิธีการแก้ก็คือ เอา ค่า i ไปเก็บไว้ที่ ฟังก์ชั่นก่อน ตามตัวอย่างข้างล่าง



# def saveme(i):
#     return lambda : i;
#
# functions = [];
#
# for i in range(10):
#
#     functions.append(saveme(i));
#
#
# for f in functions:
#     print(f());




numbers = [1,2,3,4,5];

# results = list(filter( lambda number: (number >3)  ,numbers));
results = list(map( lambda number: number * 5 ,numbers));



print(results);
