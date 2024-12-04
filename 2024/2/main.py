def simplifty(numbs, fault_tol):
    inc = False
    dec = False
    last = int(numbs[0])
    i = 1
    for numb in numbs[1:]:
        numb = int(numb)
        if fault_tol and ((numb > last and dec) or (numb < last and inc)):
            return False
        if abs(numb - last) > 3 or abs(numb - last) < 1:
            if fault_tol:
                return False
            else:
                foo = numbs.copy()
                del foo[i]
                return simplifty(foo, True)
            
        if numb > last:
            if dec:
                foo = numbs.copy()
                del foo[i]
                return simplifty(foo, True)
            inc = True
        elif numb < last:
            if inc:
                foo = numbs.copy()
                del foo[i]
                return simplifty(foo, True)
            dec = True
        last = numb
        i += 1
    return True

def main():
    with open("in.txt") as file:
        safe = 0
        lns = []
        for line in file:
            numbs = line.strip().split(" ")
            lns.append(len(numbs))
            if simplifty(numbs, False):
                safe += 1
            elif simplifty(numbs[::-1], False):
                safe += 1
    print(safe)
            
# 540
if __name__ == "__main__":
    main()