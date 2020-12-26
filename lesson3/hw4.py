import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

images = []
video = []
documents = []
music = []
unknown = []
types = set()

for file in files:
    if file.endswith('jpeg') or file.endswith('jpg') or file.endswith('png'):
        images.append(file)
        
    elif file.endswith('avi') or file.endswith('mp4') or file.endswith('mov'):
        video.append(file)
        
    elif file.endswith('doc') or file.endswith('docx') or file.endswith('txt'):
        documents.append(file)
        
    elif file.endswith('mp3') or file.endswith('ogg') or file.endswith('wav') or file.endswith('amr'):
        music.append(file)
        
    else:
        unknown.append(file)
    
    type_str = ''
    for i in range(-1, -(len(file)+1), -1):
        if file[i] != '.':
            type_str = file[i] + type_str
        else:
            break

    if type_str != file:
        types.add(type_str)

types_list = list(types)

print(f'images: {images}\nvideos: {video}\ndocuments: {documents}\nmusic: {music}\nunknown: {unknown}')
print(f'file types in the directory: {types_list}')