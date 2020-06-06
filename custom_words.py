import random

answer_directory = {
'Deutsch Lietuvis Italiana English': {'player':'Paul', 'theme':'languages Nani has been fluent in', 'hint':'languages'},
'Luck of the Naaan': {'player':'Kyle','theme':"Nani's magic love",'hint':'superpower'},
'Richard Milhouse Nixon': {'player':'Georgia','theme':"a famous bastard who helped our family", 'hint':'politics'},
'accordian guitar piano': {'player':'Amber', 'theme':"muscial instruments played by Nani's children", 'hint':'Exactly 2/3 of these are cool.'},
'domestic secretary model': {'player':'Linda', 'theme':"Nani's professions", 'hint':'work'},
'Villa Nida': {'player':'Alex','theme':"Paul's vacation house",'hint':'location'},
'Haak Haakaite Okas Okaite Zalkauskas Miciunas': {'player':'Loretta', 'theme':"Nani's various last names", 'hint':'patronymics'},
'priest lord peasant doctor':{'player':'George', 'theme':"Divergent status of George's ancestors", 'hint':'class consciousness'},
'wrestling soccer tennis':{'player':'Mick','theme':"varsity sports among boomer cousins", 'hint':'high school'},
'Otto Edwin Erna':{'player':'Belinda', 'theme':"Nani and Papi's real names and their sibling", 'hint':'some of your in-laws'}
}

keys = list(answer_directory.keys())
random.shuffle(keys)
shuffled_answers = dict([(key, answer_directory[key]) for key in keys])
