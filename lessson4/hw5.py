import os
import sys
from pathlib import Path


images_list = ('.jpeg', '.png', '.jpg' ,'.svg')
video_list = ('.avi', '.mp4', '.mov', '.mkv')
documents_list = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
music_list = ('.mp3', '.ogg', '.wav', '.amr')
archive_list = ('.zip', '.gz', '.tar')

p = Path()

images = []
video = []
documents = []
music = []
archive = []
unknown = []
types = set()

def dir_check(path):
    
    for file in path.iterdir():
        if file.suffix in images_list:
            images.append(file.name)
            
        elif file.suffix in video_list:
            video.append(file.name)
            
        elif file.suffix in documents_list:
            documents.append(file.name)
            
        elif file.suffix in music_list:
            music.append(file.name)
        
        elif file.suffix in archive_list:
            archive.append(file.name)
            
        elif file.is_dir():
            dir_check(file)
            
        else:
            unknown.append(file.name)
            
        if file.suffix:
            types.add(file.suffix)
    
dir_check(p)

types_list = list(types)



print(f'images: {images}\nvideos: {video}\ndocuments: {documents}\nmusic: {music}\narchive: {archive}\nunknown: {unknown}')
print(f'file types in the directory: {types_list}')