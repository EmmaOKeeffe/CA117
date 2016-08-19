import sys

d = {}

def longest_name(d):
    longest = [i for i in d.keys()]
    biggest = max(longest, key=len)
    return len(biggest)

def point_calc(s):
    if s <= -4:
        return 6
    elif s == -3:
        return 5
    elif s == -2:
        return 4
    elif s == -1:
        return 3
    elif s == 0:
        return 2
    elif s == 1:
        return 1
    else:
        return 0

def score_calc(par, index, name, handi, stroke):
    h = int(handi)
    total = 0
    i = 0
    l = h + 1
    while i < len(stroke):
        try:
            num = int(stroke[i])
            if h >= 1 and h <=18 and int(index[i]) in range(1, l):
                net_stroke = num - 1
                score_to_par = net_stroke - par[i]
                p = point_calc(score_to_par)
                total += p

            elif h >= 19 and h <= 36:
                c = h - 18
                if int(index[i]) in range(1, c + 1):
                    net_stroke = num - 2
                    score_to_par = net_stroke - par[i]
                    p = point_calc(score_to_par)
                    total += p

                else:
                    net_stroke = num - 1
                    score_to_par = net_stroke - par[i]
                    p = point_calc(score_to_par)
                    total += p

            elif h >= 37 and h <= 54:
                c = h - 36
                if int(index[i]) in range(1, c + 1):
                    net_stroke = num - 3
                    score_to_par = net_stroke - par[i]
                    p = point_calc(score_to_par)
                    total += p

                else:
                    net_stroke = num - 2
                    score_to_par = net_stroke - par[i]
                    p = point_calc(score_to_par)
                    total += p
            else:
                score_to_par = num - par[i]
                p = point_calc(score_to_par)
                total += p

        except ValueError:
            pass

        i += 1

        d[name] = total

def sortfunc(t):
    return t[1]

def main():
    par = []
    index = []
    for i, line in enumerate(sys.stdin):
        l = line.strip("\n")
        details = l.split(" ")
        if i == 0:
            par = [int(n) for n in details if i == 0]

        elif i == 1:
            index = [int(n) for n in details]

        else:
            stroke = details[-18:]
            handi = details[-19]
            name = " ".join(details[:-19])
            score_calc(par, index, name, handi, stroke)

    length = longest_name(d)

    for (k, v) in sorted(d.items(), key=sortfunc, reverse=True):
        print ("{:>{}s} : {:>2d}".format(k, length, v))

if __name__ == "__main__":
    main()