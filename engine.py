import codecs
import configparser
import importlib
import time

# Load configuration file with commads list
commandsConfig = configparser.ConfigParser()
commandsConfig.read_file(codecs.open("commands.ini", "r", "utf8"))

# List exit commands
exitCmdList = ['exit', 'quit', 'q', 'выход', 'выйти', 'завершть', 'stop', 'стоп']
commandsStr = ''


def returncommands(inputstr):
    """
    Parse input string and return command and parametrs
    :param inputstr: command string
    :return: tuple with command and parametrs
    """
    cmdname_r = inputstr.strip().split(' ')[0]
    cmdparams_r = ''
    if len(inputstr.strip().split(' ')) > 1:
        cmdparams_r = inputstr[inputstr.strip().find(' ') + 1:].strip()
    return cmdname_r.lower(), cmdparams_r


def run(command):
    """
    Run commands separeted by ";"
    :param command: commands string
    :return: none
    """
    cmdname, cmdparams = returncommands(command)
    start = time.time()
    if cmdname in (k.lower() for k in commandsConfig.sections()):
        try:
            cmdlib = importlib.import_module('mod.cm_' + commandsConfig[cmdname]['fn'])
            results = cmdlib.start(cmdparams)
            print(results)
        except ImportError:
            print('Модуль комманд "', cmdname, '" не найден.')
    elif cmdname in exitCmdList:
        print('Выход из программы.')
    else:
        print('Нет такой комманды!')
    end = time.time()
    print(round(time.time() - start, 5))


def interactive_input():
    commands_str = ''
    while commands_str.strip().lower() not in exitCmdList:
        commands_str = input('Введите комманду: ')
        commands_list = commands_str.split(';')

        for command_item in commands_list:
            run(command_item)
            print('{0:=>45}'.format(' '))
