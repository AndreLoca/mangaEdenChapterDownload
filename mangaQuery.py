import requests
import os
from zipfile import ZipFile

URLINFO = "https://www.mangaeden.com/api"
URLIMAGE = "https://cdn.mangaeden.com/mangasimg/"
PARAMS = {}

def listManga():
    # Fetch data
    r = requests.get(url = URLINFO+'/list/1/', params = PARAMS)
    data = r.json()
    return data


def searchManga(name):
    data = listManga()
    for m in data['manga']:
        if m['t'].lower() == name.lower():
            return m
    return None

def getChapterList(id):
    r = requests.get(url = URLINFO+'/manga/'+id)
    
    chapterListJSON = r.json()
    return chapterListJSON

def getChapter(chapterID):
    r = requests.get(url = URLINFO+'/chapter/'+chapterID)

    chapterJSON = r.json()
    return chapterJSON

def downloadChapter(chapterID, chapterName):
    chapter = getChapter(chapterID)

    os.mkdir(chapterName)

    for p in chapter['images']:
        endUrl = p[1]
        r = requests.get(URLIMAGE+endUrl)
        

        # Controlo dell'estensione dell'immagine
        if endUrl.find('.jpg') != -1:
            with open('./'+chapterName+'/'+str(p[0])+'.jpg', 'wb') as f:
                f.write(r.content)
        else:
            with open('./'+chapterName+'/'+str(p[0])+'.png', 'wb') as f:
                f.write(r.content)
    
    # Creo l'oggetto ZIP
    with ZipFile(chapterName+'.cbr', 'w') as zipObj:
        # Prendo tutti i file nella directory
        for folderName, subfolders, filenames in os.walk(chapterName):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath)