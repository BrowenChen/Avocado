from bs4 import BeautifulSoup

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder
import re
from nltk.corpus import cmudict
from hyphen import Hyphenator




auth_token = "S=s1:U=8f619:E=14fa46d4984:C=1484cbc1a48:P=1cd:A=en-devtoken:V=2:H=73202840a4274f5df8ac48c08ceaad5e"
client = EvernoteClient(token=auth_token)
note_store = client.get_note_store()

updated_filter = NoteFilter(order=NoteSortOrder.UPDATED)
offset = 0
max_notes = 100000
result_spec = NotesMetadataResultSpec(includeTitle=True)

note_book_dict = {}

for book in note_store.listNotebooks(auth_token):
    note_book_dict[book.name] = book.guid

def getContent(notebook, note):
    updated_filter.notebookGuid = note_book_dict[notebook]
    result_list = note_store.findNotesMetadata(auth_token, updated_filter, offset, max_notes, result_spec)
    content = ""

    for n in result_list.notes:
        if (n.title == note):
            content = note_store.getNoteContent(auth_token, n.guid)

    return content

result = getContent("Another", "Another title")

soup = BeautifulSoup(result)
content = soup.get_text('\n')

def avgLength(dict):
    sum = 0
    for x in range(1, len(dict)+1):
        sum+=len(dict[x])
    return sum/len(dict)
    
    
def variance(dict):
    avg = avgLength(dict)
    sum = 0
    for x in range(1, len(dict)+1):
        sum+=((len(dict[x])-avg)**2)
    return sum/len(dict)

def parseNote(string): 
    counter = 0
    nowcount = 0
    headercount = 1
    divlist = re.findall(r"[\w']+|[.?!]", string)
    parsedlist = []
    headerdict = {}
    for x in divlist:
        if x=='.' or x=='?' or x=='!':
            if headercount==1:
                for x in range(0, counter):
                    parsedlist.append(divlist[x])              
                    nowcount = counter
            else:
                for x in range(nowcount+1, counter):
                    parsedlist.append(divlist[x])
                    nowcount = counter             
            headerdict[headercount]= parsedlist
            headercount+=1
            parsedlist=[]
        counter+=1
    return headerdict
    
def numberWords(string):
    return len(re.findall(r"[\w']+|[.?!]", string))

def flesch_kincaid_grade(words, syllables, sentences):
    return ( (0.39*(words/sentences)) + (11.8*(syllables/float(words))) - 15.59)

d = cmudict.dict()

words = content.split()
syll = 0
h = Hyphenator()

def count_syllables(hyphenator,word):
    syll = 0
    think = len(hyphenator.syllables((word)))
    if  think == 0:
        syll += 1
    else:
        syll += think
    return syll

for w in words:
    syll += count_syllables(h, w)

diction = parseNote(content)
numOfWords = len(words)
numOfSent = len(diction)

print flesch_kincaid_grade(numOfWords, syll, numOfSent)
