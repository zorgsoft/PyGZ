import os

def start (args):
    dir=args.split(" ")[0]
    fileExt=args.split(" ")[1]
    #print(dir,fileExt)
    files = os.listdir(dir)
    message="Я нашла файлы"
    myfile = [x for x in files if x.endswith(fileExt)]


    return {"say":message,"text": "\n".join(myfile)}
#выводит поэлементно список
