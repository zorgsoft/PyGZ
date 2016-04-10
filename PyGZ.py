import sys
import engine
from gtts import gTTS
import pyglet


def main():
    tts = gTTS(text="Привед медвед", lang='ru')
    tts.save("hello.mp3")
    music = pyglet.resource.media("hello.mp3")
    music.play()

    if len(sys.argv) > 1:
        commands_list = ' '.join(sys.argv[1:]).split(';')
        for command_item in commands_list:
            engine.run(command_item)
            print('{0:=>45}'.format(' '))
    else:
        engine.interactive_input()


if __name__ == '__main__':
    main()
