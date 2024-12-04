import re

def main():
    with open("in.txt") as f:
        text = f.read()
    
    pattern = "mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

    sum = True
    res = 0
    for a, b, do, dont in re.findall(pattern, text):
        do_bool = (do == "do()")
        dont_bool = (dont == "don't()")
        if do_bool:
            sum = True
        if dont_bool:
            sum = False
        if a != '' and b != '' and sum:
            res += int(a) * int(b)
    print(res)

if __name__ == "__main__":
    main()