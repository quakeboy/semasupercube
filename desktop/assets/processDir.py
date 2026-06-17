import sys
import msvcrt
import os

# print (sys.argv[1])


f = open('NewEmbeds.as', 'w')

for x in os.listdir('rings'):
    f.write('\n[Embed (source = \"../res/rings/' + x + '\")]')
    y = x.replace('.','_')
    f.write('\npublic static var ' + y + ':Class;')

f.close()

msvcrt.getch()
