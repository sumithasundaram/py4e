name = input("Enter file:")
#fname="/home/superadmin/PycharmProjects/py4e/mbox-short.txt.py"
fn = open(name)
text = fn.read()
for line in text:
    if not line.startswith("From:") : continue
    line = line.split()
    print(line)
print(line[1])
'''
counts = dict()
for word in words:
           counts[word] = counts.get(word, 0) + 1
maxval = None
maxkey = None
for key,val in counts.items() :
  if val > maxval:
      maxval = val
      maxkey = key

print (maxkey, maxval)
'''