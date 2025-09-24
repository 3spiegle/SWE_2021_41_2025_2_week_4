def isHappy(n):
    if (n >= 1) and (n <= (2**31) - 1):
        sumSet = set()
        while True:
            digitSum = 0
            temp = n
            while temp > 0:
                digitSum += (temp % 10) ** 2
                temp //= 10

            n = digitSum

            if n == 1:
                return True
            elif n in sumSet:
                return False
            else:
                sumSet.add(n)
    else:
        print("1과 (2^31)-1 사이의 정수를 입력하시오.")

    return False

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")