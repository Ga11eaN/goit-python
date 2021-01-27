import re

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

