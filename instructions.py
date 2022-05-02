def Rules(username):

    RulesFile = open('rules.txt', 'r', encoding='utf_8')
    rules = RulesFile.read()
    RulesFile.close()

    return f'Изучай, {username.mention}!\n\n{rules}'

def bot_Commands():

    bot_commFile = open('bot_commands.txt', 'r', encoding='utf-8')
    bot_comm = bot_commFile.read()
    bot_commFile.close()

    return bot_comm