import codecs
import configparser
import importlib
import time
from gtts import gTTS
import pyglet

FILE_INI_CONFIG = "config.ini"
FILE_INI_COMMANDS = "commands.ini"

# List exit commands
# TODO: Что то сделать с этим
exitCmdList = ['exit', 'quit', 'q', 'выход', 'выйти', 'завершть', 'stop', 'стоп']


def config_load(config_file_name):
    """
    Load configuration file
    :param config_file_name: filename string
    :return: configparser object
    """
    tmp_config = configparser.ConfigParser()
    tmp_config.read_file(codecs.open(config_file_name, "r", "utf8"))
    return tmp_config


def config_write(config_file_name, section, option, value):
    """
    Write to configuration ini file
    :param config_file_name: configuration file name string
    :param section: section name [section]
    :param option: option name
    :param value: option value
    """
    tmp_config = configparser.ConfigParser()
    tmp_config.read_file(codecs.open(config_file_name, "r", "utf8"))
    if not tmp_config.has_section(section):
        tmp_config.add_section(section)
    tmp_config.set(section, option, value)
    with codecs.open(config_file_name, "wb", "utf8") as config_file:
        tmp_config.write(config_file)


def config_cmd_delete(section):
    """
    Delete [section] from commands configuration file
    :param section: section name
    """
    tmp_config = configparser.ConfigParser()
    tmp_config.read_file(codecs.open(FILE_INI_COMMANDS, "r", "utf8"))
    if tmp_config.has_section(section):
        tmp_config.remove_section(section)
    with codecs.open(FILE_INI_COMMANDS, "wb", "utf8") as config_file:
        tmp_config.write(config_file)


# Load configuration file with commads list
commandsConfig = config_load(FILE_INI_COMMANDS)


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


def run(command, voice_enable=True):
    """
    Run commands separeted by ";"
    :param command: commands string
    :param voice_enable: enable voice tts
    :return: none
    """
    cmdname, cmdparams = returncommands(command)
    start = time.time()
    if cmdname in (k.lower() for k in commandsConfig.sections()):
        try:
            cmdlib = importlib.import_module('mod.cm_' + commandsConfig[cmdname]['fn'])
            results = cmdlib.start(cmdparams)
            if results["say"] and voice_enable:
                saytext(results["say"])
            print(results["text"])
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


def saytext(texttosay):
    """
    Say text with gTTS and pyglet modules
    :param texttosay: text string
    """
    # TODO: Доработать, добавить возможность изменять язык и удалять за собой файлы
    if len(texttosay.strip()) < 1:
        return
    tts = gTTS(text=texttosay, lang='ru')
    tts.save("results.mp3")
    music = pyglet.resource.media("results.mp3")
    music.play()
