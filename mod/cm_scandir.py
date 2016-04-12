import  os


def start(args):
    try:
      a = os.listdir(args)
      message="Мы нашли что-то : "
      return {"say":message,"text": "\n".join(a)}
    except FileNotFoundError:
        return {"say":"Ошибка","text":"File not found error!"}


