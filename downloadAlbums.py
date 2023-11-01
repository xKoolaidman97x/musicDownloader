import os
import shutil
import mp4tomp3 as converter


def queryAlbum():
    Albums = []
    while True:
        os.system('clear')
        print(f'''
              Selected Albums:
              ''')
        for x in Albums:
            print(x)
        print("\nPlease Enter Album info.\n Enter 'q' to quit.\n Enter 'c' to continue.")
        Album = input('\nAlbum name: ')
        if Album == 'c':
            return Albums
        if Album == 'q':
            exit()
        AlbumLink = input('\nAlbum link: ')
        if AlbumLink == 'c':
            return Albums
        if AlbumLink == 'q':
             exit()

        Albums.append({
             'Album Name': Album,
             'Album Link' : AlbumLink})   

def folderCheck(Album):

    audPath = f'{Album} (audio)'
    vidPath = f'{Album} (video)'
    tmpPath = f'{Album} (tmp)'

    if os.path.exists(audPath):
         shutil.rmtree(audPath)
         os.mkdir(audPath)
    else:
        os.mkdir(audPath)
    if os.path.exists(vidPath):
         shutil.rmtree(vidPath)
         os.mkdir(vidPath)
    else:
        os.mkdir(vidPath)
    if os.path.exists(tmpPath):
         shutil.rmtree(tmpPath)
         os.mkdir(tmpPath)
    else:
        os.mkdir(tmpPath)

def downloadAlbum(Album,AlbumLink,runningAlbums):  

    audPath = f'{Album} (audio)'
    vidPath = f'{Album} (video)'
    tmpPath = f'{Album} (tmp)'

    # Takes all the songs from the fil and downloads them using a project called youtube-dl
    # LINK TO PROJECT https://github.com/ytdl-org/youtube-dl#description
    os.system("clear")
    #os.system(f"cd '{tmpPath}'")
    for x in runningAlbums:
        print(x)
    print('\n##################################')
    print(f'\nDownloading {Album}...\n')
    print('##################################\n')
    os.system(f"cd '{tmpPath}' && youtube-dl '{AlbumLink}'")
    for x in os.listdir(tmpPath):
        shutil.move(f"{tmpPath}/{x}",vidPath)
    shutil.rmtree(tmpPath)

    # This uses a project called mp4tomp3 to convert the videos to mp3
    # LINK TO PROJECT https://github.com/andyp123/mp4_to_mp3
    converter.main(vidPath,audPath)

def organizeMusic(Album):        
        # ORGANIZATION
        os.system(f"mv '{Album} (tmp)/*.mp3' '{Album} (audio)'")
        os.system(f"mv '{Album} (tmp)/*.mp4' '{Album} (video)'")
        songsList = os.popen(f"ls '{Album} (audio)'")
        songsListNew = []
        for x in songsList:
            newTitle = x.split('-')
            newTitle = newTitle[1]
            newTitle = newTitle.split('(Visualizer)')
            newTitle = newTitle[0]
            newTitle = newTitle.split('(Video Oficial)')
            newTitle = newTitle[0]
            newTitle = newTitle.split('(Official Video)')
            newTitle = newTitle[0]
            newTitle = newTitle.split('(360° Visualizer)')
            newTitle = newTitle[0]
            newTitle = newTitle.strip(' ')
            newTitle = f'{newTitle}.mp3'
            songsListNew.append(newTitle)
            x = x.strip('\n')
            print(f'\n\n{x} --> {newTitle}\n\n')
            os.rename(f"{Album} (audio)//{x}",f"{Album} (audio)//{newTitle}")

class __main__():

    Albums = queryAlbum()
    runningAlbums = []

    for x in Albums:
        AlbName = x['Album Name']
        AlbLink = x['Album Link']
        folderCheck(AlbName)
        downloadAlbum(AlbName,AlbLink,runningAlbums)
        organizeMusic(AlbName)
        runningAlbums.append(x)

