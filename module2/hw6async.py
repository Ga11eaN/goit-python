import asyncio
from aiopath import AsyncPath
from pathlib import Path
import os

def define_name(file, destination_path):
    
    file_name = file.stem+file.suffix
    flag = True
    i = 1
    
    while flag:
        if Path(destination_path+'/'+file_name).is_file():
            file_name = file.stem+'_'+str(i)+file.suffix
            i += 1
        else:
            flag = False
            
    return file_name


async def move(file, destination_path):
    #print(f'checking file name {file}')
    file_name = define_name(file, destination_path)

    try:
        #print(f'try before to move file {file_name}')
        await AsyncPath(file).rename(destination_path+'/'+file_name)
        #print(f'try after to move file {file_name}')
    except:
        #print(f'except before to move file {file_name}')
        file_name = define_name(file, destination_path)
        Path(file).rename(destination_path+'/'+file_name)
        #print(f'except after to move file {file_name}')
    #print(f'finished moving file {file_name}')
    
async def check_dir(path, destinations):

    images_list = ('.jpeg', '.png', '.jpg' ,'.svg')
    video_list = ('.avi', '.mp4', '.mov', '.mkv')
    documents_list = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    music_list = ('.mp3', '.ogg', '.wav', '.amr')
    archive_list = ('.zip', '.gz', '.tar')
    
    IGNORED_LIST = [destinations['img_path'],
                    destinations['doc_path'], 
                    destinations['audio_path'], 
                    destinations['video_path'],
                    destinations['arc_path']]
    
    for file in path.iterdir():
        
        if file.suffix in images_list:
            await move(file, destinations['img_path'])
            
        elif file.suffix in video_list:
            await move(file, destinations['video_path'])
            
        elif file.suffix in documents_list:
            await move(file, destinations['doc_path'])
            
        elif file.suffix in music_list:
            await move(file, destinations['audio_path'])
        
        elif file.suffix in archive_list:
            await move(file, destinations['arc_path'])
            
        elif file.is_dir():
            if file in IGNORED_LIST:
                continue
            elif not os.listdir(file):
                os.rmdir(file)
    if not os.listdir(path):
        os.rmdir(path)


def collect_dir(path, dir_list, destinations):
    for file in path.iterdir():
        if file.is_dir() and str(file) not in destinations.values():
            dir_list.append(file.resolve())
            dir_list = collect_dir(file.resolve(), dir_list, destinations)
    return dir_list
            
 
p = Path().resolve()
#path_str = str(p) + '\\aaa'
dir_list = [p]
destinations = {
                'img_path' : str(p)+'\\images',
                'doc_path' : str(p)+'\\documents',
                'audio_path' : str(p)+'\\audio',
                'video_path' : str(p)+'\\video',
                'arc_path' : str(p)+'\\archives'
                }
os.makedirs('images', exist_ok = True)
os.makedirs('documents', exist_ok = True)
os.makedirs('audio', exist_ok = True)
os.makedirs('video', exist_ok = True)
os.makedirs('archives', exist_ok = True)

dir_list = collect_dir(p, dir_list, destinations)

tasks = [check_dir(path, destinations) for path in dir_list]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
