import random

answer_directory = {
'Deutsch Lietuvis Italiana English': {'player':'Paul', 'theme':'Languages Nani has been fluent in', 'hint':'languages'},
'Luck of the Naaan': {'player':'Kyle','theme':"Nani's magic love",'hint':'superpower'},
'Richard Milhouse Nixon': {'player':'Georgia','theme':"Saved our family", 'hint':'politics'},
'accordian guitar piano': {'player':'Amber', 'theme':"Muscial instruments played by Nani's children", 'hint':'2/3 of these are cool'},
'domestic secretary model': {'player':'Linda', 'theme':"Nani's professions", 'hint':'work'},
'Villa Nida': {'player':'Alex','theme':"Paul's vacation house",'hint':'location'},
'Haak Haakaite Okas Okaite Zalkauskas Miciunas': {'player':'Loretta', 'theme':"Nani's various last names", 'hint':'patronymics'},
'priest lord peasant doctor':{'player':'George', 'theme':"Divergent status of people of George's ancestors", 'hint':'class consciousness'},
'wrestling soccer tennis':{'player':'Mick','theme':"Varsity sports among cousins", 'hint':'high school'},
'Otto Edwin Erna':{'player':'Belinda', 'theme':"Nani and Papi's siblings", 'hint':'some of your in-laws'}
}

answer_dictionary = {
'Paul':'Deutsch Lietuvis Italiana English',
'Kyle':'Luck of the Naaan',
'Georgia':'Richard Milhouse Nixon',
'Amber':'accordion guitar piano',
'Linda':'domestic secretary model',
'Alex':'Villa Nida',
'Loretta':'Haak Haakaite Okas Okaite Zalkauskas Miciunas',
'George':'priest lord peasant doctor',
'Mick':'wrestling soccer tennis',
'Belinda':'Otto Edwin Erna'
}

keys = list(answer_directory.keys())
random.shuffle(keys)
shuffled_answers = dict([(key, answer_directory[key]) for key in keys])

# word_list = [
# 'German Lithuanian Italian English',
# 'Richard Milhouse Nixon',
# 'Chloe Max Bowie',
# 'Elvis Layla Ace',
# 'Mugsy Tilly Chance',
# ]
