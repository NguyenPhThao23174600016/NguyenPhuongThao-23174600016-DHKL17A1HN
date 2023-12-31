# in ra số may mắn dịch từng phần tử xem có chia cho 7 hay không nếu có phần tử chia hết cho 7 thì in ra True và ngược lại
def day_so(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False

nums = input("Nhập dãy số là: ")
nums = [int(num) for num in nums.split()]
print("Nums = ", nums)
print(day_so(nums))
