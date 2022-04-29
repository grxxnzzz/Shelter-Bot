def Rules(username):

    RulesFile = open('rules.txt', 'r', encoding='utf_8')
    rules = RulesFile.read()
    RulesFile.close()

    return f'Изучай, {username.mention}!\n\n{rules}'