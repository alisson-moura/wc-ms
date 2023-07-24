def nps(score):
    parsedScore = int(score)
    if(parsedScore < 7):
        return  'detratores'
    if(parsedScore < 9):
        return 'neutros'
    else:
        return 'promotores'