fp=open('text.txt','r')
for l in fp:
  print(l),
fp.close()

fp = open('text.txt','w')
while True:
    txt = input('Enter text (end with blank):')
    if len(txt)==0:
        break
    else:
        fp.write(txt+'\n')
fp.close()


nfile='doesnotexist.txt'
try:
    fp=open(nfile,'r')
except:
    print('Cannot open',nfile,'for reading. Does not exist')


    

fp=open('tempfile.txt','w')
# for i=
fp.close()
