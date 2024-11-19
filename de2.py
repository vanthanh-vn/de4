# ĐỀ 2
# Viết chương trình Python yêu cầu mỗi ý từ 1 đến 16 viết 1 hàm lưu trữ dưới dạng thư viện.
# 1. Nhập vào một dãy số nguyên cho tới khi không muốn nhập nữa. In dãy vừa nhập ra màn hình
def nhap():
        number = []
        while True:
                number1 =   int(input('Nhap so nguyen:'))
                number.append(number1)
                
                choice = input('Nhap tiep hay ko? (y/n)')
                if choice.lower() != 'y':
                    break
        return number
# 2. Xóa toàn bộ các phần tử âm khỏi danh sách.
def xoa_am(numbers):
    numbers = [num for num in numbers if num>= 0]
    return numbers
# 3. Nhập 1 số X, đếm số lần xuất hiện X trong danh sách.
def demx(numbers):
    x = int(input("nhap x:"))
    dem = 0
    for i in numbers:
        if x == i:
            dem +=1
    return dem      
# 4. Nhập 1 số X, tìm các vị trí xuất hiện X trong danh sách.
def timx(numbers):
    x = int(input("nhap x:"))
    for i in range(len(numbers)):
        if x == numbers[i]:
            print(i,end = " ")
# 5. Đếm số phần tử khác nhau trong danh sách.
def demkhac(numbers):
    dem = 0
    unique_number = []
    for i in numbers :
        if i not in unique_number:
            unique_number.append(i)
            dem += 1
    return dem
def demkhac1(numbers):
    return len(set(numbers))
# 6. Xóa toàn bộ các phần tử trong danh sách.
def xoa(numbers):
    numbers.clear()
# 7. Đưa ra trung bình cộng các só chia hết cho3 có trong danh sách vừa nhập.
def tbc(numbers):
    chia_het_cho_3 = [num for num in numbers if num % 3 == 0]
    if len(chia_het_cho_3) == 0 :
        return 0
    tong = sum(chia_het_cho_3) / len(chia_het_cho_3)
    return tong
# 8. Xóa tất cả các số dương khỏi danh sách
def xoaduong(numbers):
    return [num for num in numbers if num <= 0]
# 9. Đưa ra số chia hết cho 5 cuối cùng trong danh sách
def sochiacho5(numberes):
    for num in reversed(numberes):
        if num % 5 == 0:
            return num
    return None
def sochiacho5_2(numbers):
    scan = -1
    for i in range(len(numbers)-1 ):
        if numbers[i] % 5 == 0 :
            scan = numbers[i]
    if scan == -1:
        return None
    return scan
# 10. Đưa ra trung bình cộng các só âm có trong danh sách vừa nhập.
def tbcsoam(numbers):
    new_numbers = [num for num in numbers if num <= 0]
    if len(new_numbers) == 0 :
        return None
    return sum(new_numbers) / len(new_numbers)
# 11. Thay thế tất cả các số âm trong danh sách thành số 0
def newnumbers(numbers):
    for i in range(len(numbers)):
        if numbers[i] < 0 :
            numbers[i] = 0
    return numbers
def newnumbers2(numbers):
    return [0 if num < 0 else num for num in numbers]
# 12. Xóa các giá trị trùng lặp trong danh sách
def pop_trung(numbers):
    return list(set(numbers))
# 13. Tìm phần tử dương nhỏ nhất trong danh sách.
def timduongnhonhat(numbers):
    new_numbers = [num for num in numbers if num >= 0]
    if not new_numbers:
        return None
    return min(new_numbers)
        
# 14. Đưa ra số lượng các số âm liên tiếp nhiều nhất
def soamlientiep(numbers):
    current_count = 0
    max_count = 0
    for num in numbers:
        if num > 0:
            current_count += 1
            max_count = max(max_count,current_count)
        else:
            current_count = 0
    return max_count    
# 15. Đưa ra tổng và trung bình cộng các phần tử trong danh sách
def tong_tbc(numbers):
    tong = 0
    tbc = 0
    for num in numbers:
        tong += num
    tbc = tong / len(numbers)
    return tong,tbc
# 16. Tìm các số hoàn hảo trong danh sách và in ra màn hình
def shh(num):
    if num <= 1:
        return False
    tong_uoc = 0
    for i in range(1,num/2):
        if num % i == 0:
            tong_uoc += i   
    return tong_uoc == num
def la_sohh(numbers):
    return [num for num in numbers if shh(num)]
# 17. Viết chương trình sử dụng các hàm trên.

if __name__ == "__main__":
    result = nhap()
    print(f"day so {result}")
    koam = xoa_am(result)
    print(f'GG {koam}')
    print(f"so lan {demx(result)}")
    timx(f'{result}')
    # xoa(result)
    # print(f'{result}')
    print(f'tong = {tbc(result)}')
    print(f'so chia het cho 5 {sochiacho5_2(result)}')
    print(f'thay the so am {newnumbers(result)}')
  #  print(f'xoa trung {pop_trung(result)}')
    print(f'so duong nho nhat {timduongnhonhat(result)}')
    print(f'so am lien tiep {soamlientiep(result)}')
    print(f'tong va tbc {tong_tbc(result)}')
# ĐỀ 2
# Viết chương trình Python yêu cầu mỗi ý từ 1 đến 16 viết 1 hàm lưu trữ dưới dạng thư viện.
# 1. Nhập vào một dãy số nguyên cho tới khi không muốn nhập nữa. In dãy vừa nhập ra màn hình
def nhap():
        number = []
        while True:
                number1 =   int(input('Nhap so nguyen:'))
                number.append(number1)
                
                choice = input('Nhap tiep hay ko? (y/n)')
                if choice.lower() != 'y':
                    break
        return number
# 2. Xóa toàn bộ các phần tử âm khỏi danh sách.
def xoa_am(numbers):
    numbers = [num for num in numbers if num>= 0]
    return numbers
# 3. Nhập 1 số X, đếm số lần xuất hiện X trong danh sách.
def demx(numbers):
    x = int(input("nhap x:"))
    dem = 0
    for i in numbers:
        if x == i:
            dem +=1
    return dem      
# 4. Nhập 1 số X, tìm các vị trí xuất hiện X trong danh sách.
def timx(numbers):
    x = int(input("nhap x:"))
    for i in range(len(numbers)):
        if x == numbers[i]:
            print(i,end = " ")
# 5. Đếm số phần tử khác nhau trong danh sách.
def demkhac(numbers):
    dem = 0
    unique_number = []
    for i in numbers :
        if i not in unique_number:
            unique_number.append(i)
            dem += 1
    return dem
def demkhac1(numbers):
    return len(set(numbers))
# 6. Xóa toàn bộ các phần tử trong danh sách.
def xoa(numbers):
    numbers.clear()
# 7. Đưa ra trung bình cộng các só chia hết cho3 có trong danh sách vừa nhập.
def tbc(numbers):
    chia_het_cho_3 = [num for num in numbers if num % 3 == 0]
    if len(chia_het_cho_3) == 0 :
        return 0
    tong = sum(chia_het_cho_3) / len(chia_het_cho_3)
    return tong
# 8. Xóa tất cả các số dương khỏi danh sách
def xoaduong(numbers):
    return [num for num in numbers if num <= 0]
# 9. Đưa ra số chia hết cho 5 cuối cùng trong danh sách
def sochiacho5(numberes):
    for num in reversed(numberes):
        if num % 5 == 0:
            return num
    return None
def sochiacho5_2(numbers):
    scan = -1
    for i in range(len(numbers)-1 ):
        if numbers[i] % 5 == 0 :
            scan = numbers[i]
    if scan == -1:
        return None
    return scan
# 10. Đưa ra trung bình cộng các só âm có trong danh sách vừa nhập.
def tbcsoam(numbers):
    new_numbers = [num for num in numbers if num <= 0]
    if len(new_numbers) == 0 :
        return None
    return sum(new_numbers) / len(new_numbers)
# 11. Thay thế tất cả các số âm trong danh sách thành số 0
def newnumbers(numbers):
    for i in range(len(numbers)):
        if numbers[i] < 0 :
            numbers[i] = 0
    return numbers
def newnumbers2(numbers):
    return [0 if num < 0 else num for num in numbers]
# 12. Xóa các giá trị trùng lặp trong danh sách
def pop_trung(numbers):
    return list(set(numbers))
# 13. Tìm phần tử dương nhỏ nhất trong danh sách.
def timduongnhonhat(numbers):
    new_numbers = [num for num in numbers if num >= 0]
    if not new_numbers:
        return None
    return min(new_numbers)
        
# 14. Đưa ra số lượng các số âm liên tiếp nhiều nhất
def soamlientiep(numbers):
    current_count = 0
    max_count = 0
    for num in numbers:
        if num > 0:
            current_count += 1
            max_count = max(max_count,current_count)
        else:
            current_count = 0
    return max_count    
# 15. Đưa ra tổng và trung bình cộng các phần tử trong danh sách
def tong_tbc(numbers):
    tong = 0
    tbc = 0
    for num in numbers:
        tong += num
    tbc = tong / len(numbers)
    return tong,tbc
# 16. Tìm các số hoàn hảo trong danh sách và in ra màn hình
def shh(num):
    if num <= 1:
        return False
    tong_uoc = 0
    for i in range(1,num/2):
        if num % i == 0:
            tong_uoc += i   
    return tong_uoc == num
def la_sohh(numbers):
    return [num for num in numbers if shh(num)]
# 17. Viết chương trình sử dụng các hàm trên.

if __name__ == "__main__":
    result = nhap()
    print(f"day so {result}")
    koam = xoa_am(result)
    print(f'GG {koam}')
    print(f"so lan {demx(result)}")
    timx(f'{result}')
    # xoa(result)
    # print(f'{result}')
    print(f'tong = {tbc(result)}')
    print(f'so chia het cho 5 {sochiacho5_2(result)}')
    print(f'thay the so am {newnumbers(result)}')
  #  print(f'xoa trung {pop_trung(result)}')
    print(f'so duong nho nhat {timduongnhonhat(result)}')
    print(f'so am lien tiep {soamlientiep(result)}')
    print(f'tong va tbc {tong_tbc(result)}')
