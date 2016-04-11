import engine


def start(args):
    return_data = {
        "say":  "Необходимо передать 2 или 4 параметра",
        "text": "Необходимо передать 2 или 4 параметра вида:\n"
                "add:комманда:название_модуля:описание\n"
                "или\n"
                "del:комманда\n"
                "Символ ':' является разделителем комманд\n"
                "Первый параметр add или del для добавления или удаления комманды."
    }
    args_list = args.split(':')

    if len(args_list) == 4 and args_list[0].lower() == 'add':
        engine.config_write(engine.FILE_INI_COMMANDS, args_list[1], 'fn', args_list[2])
        engine.config_write(engine.FILE_INI_COMMANDS, args_list[1], 'desc', args_list[3])
        engine.commandsConfig = engine.config_load(engine.FILE_INI_COMMANDS)
        return_data['say'] = 'Команда добавлена.'
        return_data['text'] = 'Добавили новую "{0}" команду.'.format(args_list[1])
    elif len(args_list) == 2 and args_list[0].lower() == 'del':
        engine.config_cmd_delete(args_list[1])
        engine.commandsConfig = engine.config_load(engine.FILE_INI_COMMANDS)
        return_data['say'] = 'Команда удалена.'
        return_data['text'] = 'Команда "{0}" удалена из настроек.'.format(args_list[1])

    return return_data
