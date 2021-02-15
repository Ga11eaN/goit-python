import os
import pathlib
import re
import shutil
import sys


def normalize(cyrilic):
    dic = {ord('Ь'):'', ord('ь'):'', ord('Ъ'):'', ord('ъ'):'', ord('А'):'A', ord('а'):'a', ord('Б'):'B', ord('б'):'b', ord('В'):'V', ord('в'):'v',
       ord('Г'):'G', ord('г'):'g', ord('Д'):'D', ord('д'):'d', ord('Е'):'E', ord('е'):'e', ord('Ё'):'E', ord('ё'):'e', ord('Ж'):'Zh', ord('ж'):'zh',
       ord('З'):'Z', ord('з'):'z', ord('И'):'I', ord('и'):'i', ord('Й'):'I', ord('й'):'i', ord('К'):'K', ord('к'):'k', ord('Л'):'L', ord('л'):'l',
       ord('М'):'M', ord('м'):'m', ord('Н'):'N', ord('н'):'n', ord('О'):'O', ord('о'):'o', ord('П'):'P', ord('п'):'p', ord('Р'):'R', ord('р'):'r', 
       ord('С'):'S', ord('с'):'s', ord('Т'):'T', ord('т'):'t', ord('У'):'U', ord('у'):'u', ord('Ф'):'F', ord('ф'):'f', ord('Х'):'H', ord('х'):'h',
       ord('Ц'):'C', ord('ц'):'c', ord('Ч'):'Ch', ord('ч'):'ch', ord('Ш'):'Sh', ord('ш'):'sh', ord('Щ'):'Shch', ord('щ'):'shch', ord('Ы'):'Y',
       ord('ы'):'y', ord('Э'):'E', ord('э'):'e', ord('Ю'):'Iu', ord('ю'):'iu', ord('Я'):'Ia', ord('я'):'ia'} 
    
    latin = cyrilic.translate(dic)
    result = re.sub(r'\W', '_' , latin)
    
    return result

def dir_check(path):
    images_list = ('.jpeg', '.png', '.jpg' ,'.svg')
    video_list = ('.avi', '.mp4', '.mov', '.mkv')
    documents_list = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    music_list = ('.mp3', '.ogg', '.wav', '.amr')
    archive_list = ('.zip', '.gz', '.tar')
    
    try:
        os.mkdir('images')
        os.mkdir('documents')
        os.mkdir('audio')
        os.mkdir('video')
        os.mkdir('archives')
    except FileExistsError:
        pass

    img_path = pathlib.Path('images')
    doc_path = pathlib.Path('documents')
    audio_path = pathlib.Path('audio')
    video_path = pathlib.Path('video')
    arc_path = pathlib.Path('archives')
    
    IGNORED_LIST = [img_path, doc_path, audio_path, video_path, arc_path]
    IGNORED = ['images', 'documents', 'audio', 'video', 'archives']
    
    for file in path.iterdir():
    
        file = file.rename(pathlib.Path(file.parent,normalize(file.stem)+file.suffix))
        
        if file.suffix in images_list:
            shutil.move(file,img_path)
            
        elif file.suffix in video_list:
            shutil.move(file,video_path)
            
        elif file.suffix in documents_list:
            shutil.move(file,doc_path)
            
        elif file.suffix in music_list:
            shutil.move(file,audio_path)
        
        elif file.suffix in archive_list:
            shutil.move(file,arc_path)
            
        elif file.is_dir():
            if file.stem in IGNORED and file in IGNORED_LIST:
                continue
            elif not os.listdir(file):
                os.rmdir(file)
            else:
                dir_check(file)
                if not os.listdir(file):
                    os.rmdir(file)
                    
    for archive in arc_path.iterdir():
        if archive.suffix in archive_list:
            path = 'archives\\'+ archive.stem
            shutil.unpack_archive(archive, path)
            os.unlink(archive)

def main():
    p = pathlib.Path()
    try:
        os.mkdir('images')
    except FileExistsError:
        pass
    try:
        os.mkdir('documents')
    except FileExistsError:
        pass
    try:
        os.mkdir('audio')
    except FileExistsError:
        pass
    try:
        os.mkdir('video')
    except FileExistsError:
        pass
    try:
        os.mkdir('archives')
    except FileExistsError:
        pass

    dir_check(p)
           
if __name__ == '__main__':
    main()