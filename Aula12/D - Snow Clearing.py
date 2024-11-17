
testcases = int(input())
input()

for i in range(testcases):
    total_dist = 0
    hangar = tuple(map(int, input().split()))
    while True:
        try:
            str = input()
        except EOFError:
            break
        if str == "":
            break
        str = str.split()
        begin = (int(str[0]), int(str[1]))
        end = (int(str[2]), int(str[3]))
        dist = (((begin[0] - end[0])**2 + (begin[1] - end[1])**2)**0.5)/1000 # in km
        total_dist += dist

    result = 2*total_dist # both sides
    result = result/20 # 20 km/h

    hours = int(result)
    minutes = (result - hours)*60
    rounded_minutes = int(round(minutes))
    if rounded_minutes == 60:
        hours += 1
        rounded_minutes = 0

    if i != testcases - 1:
        print(f'{hours}:{rounded_minutes:02d}\n')
    else:
        print(f'{hours}:{rounded_minutes:02d}')
