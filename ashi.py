def rev(s):
    return int(str(s)[::-1])
n = int(input())
l = [int(i) for i in input().split()[:n]]
m = map(rev,l)
print(*m)

