import os
import mangaQuery


print('Che manga stai cercando?')
name = input()

manga = mangaQuery.searchManga(name)
chapterList = mangaQuery.getChapterList(manga['i'])
os.system('clear')

print('Nome: '+manga['t'])
print('Descrizione: '+chapterList['description'])
print('Capitoli:')

for c in chapterList['chapters']:
    print('  Capitolo: '+str(c[0])+' - Titolo: '+str(c[2]))

print('Scegli il capitolo che vuoi scaricare')
chapter = input()

for c in chapterList['chapters']:
    if chapter == str(c[0]):
        chapterName = str(c[0])+'_'+str(c[2]).replace(' ', '')
        mangaQuery.downloadChapter(c[3], chapterName)
        break
