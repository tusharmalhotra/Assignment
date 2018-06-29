#Q1
with open(fname) as f:
    content = f.readlines()

content = [x.strip() for x in content]

#Q2.
with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
#Q3.
with open('abc.txt') as f1, open('test.txt') as f2:
    for line1, line2 in zip(f1, f2):
        
        print(line1+line2)
