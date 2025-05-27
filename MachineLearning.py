a,b,n = map(int,input().split())
answers = list(map(int,input().split()))

if answers[-1] != a+b or answers[0] == a+b:
    print("REJECT")
    quit()

best = abs(a+b - answers[0])
for answer in answers:
    current_distance = abs(a+b - answer)
    if current_distance > best:
        print("REJECT")
        quit()
    best = current_distance

for answer in answers:
    if answers.count (answer)>3:
        print("REJECT")
        quit()

print("HIRE")
