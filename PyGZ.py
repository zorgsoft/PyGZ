import sys
import engine


def main():
    if len(sys.argv) > 1:
        commands_list = ' '.join(sys.argv[1:]).split(';')
        for command_item in commands_list:
            engine.run(command_item, voice_enable=False)
            print('{0:=>45}'.format(' '))
    else:
        engine.interactive_input()


if __name__ == '__main__':
    main()
