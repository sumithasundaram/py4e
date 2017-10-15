name = input("Enter file:")
#fname="/home/superadmin/PycharmProjects/py4e/mbox-short.txt.py"
fn = open(name)
words_list=list()
for line in fn:
    if not line.startswith("From:") : continue
    words = line.split