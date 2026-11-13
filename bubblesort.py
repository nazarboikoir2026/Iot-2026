def parse(line):
    nums, tok = [], ""
    for ch in line + " ":
        if ch != " ":
            tok += ch
        elif tok:
            digits = tok[1:] if tok[0] == "-" else tok
            if not digits or not all("0" <= c <= "9" for c in digits):
                return None
            n = 0
            for c in digits:
                n = n*10 + ord(c) - ord("0")
            nums.append(-n if tok[0] == "-" else n)
            tok = ""
    return nums


def read_numbers():
    while True:
        nums = parse(input("Введіть цілі числа через пробіл: "))
        if nums is None:
            print("Помилка: потрібно вводити лише цілі числа.")
        elif len(nums) % 2 == 0:
            print("Помилка: кількість чисел має бути непарною.")
        else:
            counts = [nums.count(x) for x in nums]
            if set(counts) <= {1, 2} and counts.count(1) == 1:
                return nums
            print("Помилка: кожне число має повторюватись двічі, крім одного.")

def find_single(nums):
    result = 0
    for n in nums:
        result ^= n
    return result



if __name__ == "__main__":
    print("Самотній елемент:", find_single(read_numbers()))
