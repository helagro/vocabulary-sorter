
divider = input("Divider:" )

q = []
a = []


with open("input.txt") as f:
    for line in f:
        qna = line.split(divider)
        if (len(qna) > 1):
            q.append(qna[0] + "\n")
            a.append(qna[1])
        else:
            print("Missed!!")

with open("output.txt", "r+") as f:
    f.truncate(0)

    for question in q:
        f.writelines(question)

    f.write("\n\n\n")

    for answer in a:
        f.writelines(answer)
    

print("the divider:", divider)