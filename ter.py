import pyter
ftest = open("data/pp3/test.vn", "r", encoding="utf8")
ftran = open("data/pp3/testTranslatedBase.vn", "r", encoding="utf8")

ltest = ftest.readlines()
ltran = ftran.readlines()

numrows = len(ltest)
#numrows = 1072146
print(numrows)
#print(numrows)
#rows_pos = file_pos.readlines()
#numrows_pos = len(rows_pos)
newlinetest=""
newlinetran=""
for linetest in ltest:
    newlinetest += linetest

for linetrain in ltran:
    newlinetran += linetrain
#print(newlinetest)

""""
ref = u'newlinetest'.split()
hyp = u'newlinetran'.split()
print('%.3f' % pyter.ter(hyp, ref))
ftest.close()
  print(rows[indexRow][0].lower() + rows[indexRow][1:])
    file2.write(rows[indexRow][0].lower() + rows[indexRow][1:])
file2.close()

ref = u'SAUDI ARABIA denied THIS WEEK information published in the AMERICAN new york times'.split()
hyp = u'THIS WEEK THE SAUDIS denied information published in the new york times'.split()
print('%.3f' % pyter.ter(hyp, ref))

ref = list(u"Pythonは、より素早く、効果的にシステムとの統合が可能なプログラミング言語です。")
hyp = list(u"Pythonは、より迅速に動作するとより効果的にシステムを統合できるプログラミング言語です。")
"""
ref1 = 'SAUDI ARABIA denied THIS WEEK information published in the AMERICAN new york times'.split()
#print(ref1)
ref = newlinetest.split()
#print(ref)
hyp = newlinetran.split()
print('%.3f' % pyter.ter(hyp, ref))
