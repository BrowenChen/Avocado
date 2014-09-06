import urlparse
import urllib

import thrift.protocol.TBinaryProtocol as TBinaryProtocol
import thrift.transport.THttpClient as THttpClient
import evernote.edam.userstore.UserStore as UserStore
import evernote.edam.notestore.NoteStore as NoteStore
from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder, Note


import oauth2 as oauth
from flask import Flask, session, redirect, url_for, request


from app import app


# THIS IS ALL EVERNOTE API
APP_SECRET_KEY = \
    'YOUR KEY HERE'

EN_CONSUMER_KEY = 'browenchen'
EN_CONSUMER_SECRET = '82b51ceb3ee61677'

EN_REQUEST_TOKEN_URL = 'https://sandbox.evernote.com/oauth'
EN_ACCESS_TOKEN_URL = 'https://sandbox.evernote.com/oauth'
EN_AUTHORIZE_URL = 'https://sandbox.evernote.com/OAuth.action'

EN_HOST = "sandbox.evernote.com"
EN_USERSTORE_URIBASE = "https://" + EN_HOST + "/edam/user"
EN_NOTESTORE_URIBASE = "https://" + EN_HOST + "/edam/note/"



def get_oauth_client(token=None):
    """Return an instance of the OAuth client."""
    consumer = oauth.Consumer(EN_CONSUMER_KEY, EN_CONSUMER_SECRET)
    if token:
        client = oauth.Client(consumer, token)
    else:
        client = oauth.Client(consumer)
    return client


def get_notestore():
    """Return an instance of the Evernote NoteStore. Assumes that 'shardId' is
    stored in the current session."""
    shardId = session['shardId']
    noteStoreUri = EN_NOTESTORE_URIBASE + shardId
    noteStoreHttpClient = THttpClient.THttpClient(noteStoreUri)
    noteStoreProtocol = TBinaryProtocol.TBinaryProtocol(noteStoreHttpClient)
    noteStore = NoteStore.Client(noteStoreProtocol)
    return noteStore


def get_userstore():
    """Return an instance of the Evernote UserStore."""
    userStoreHttpClient = THttpClient.THttpClient(EN_USERSTORE_URIBASE)
    userStoreProtocol = TBinaryProtocol.TBinaryProtocol(userStoreHttpClient)
    userStore = UserStore.Client(userStoreProtocol)
    return userStore



# FUNCTIONS TO GET THE FIRST NOTEBOOK AND CREATE A NOTE 
# Testing evernote api

dev_token = "S=s1:U=8f63c:E=14fa46290b0:C=1484cb16418:P=1cd:A=en-devtoken:V=2:H=abe865ff0110d8fa64b1a76f1ef8600e"
client = EvernoteClient(token=dev_token)

firstID = 0
# GETTING ALL THE NOTES IN THE DEFAULT NOTEBOOK

allNotes = []

# DICTIONARY OF NOTE CONTENTS
notesContents = {}


def getFirstNoteBook():

	userStore = client.get_user_store()
	noteStore = client.get_note_store()
	note = noteStore.listNotebooks()
	user = userStore.getUser()
	
	firstNotebook = note[0]
	global firstID
	firstID = firstNotebook.guid

	print(' ')
	print( 'First notebook in the stack')
	print firstNotebook.name
	print firstID
		
	print(' ')

	print ' Notes in ' + firstNotebook.name


	# filter = NoteFilter()
	# filter.notebookGuid = firstID
	# filter.order = Types.NoteSortOrder.UPDATED
	# filter.ascending = False

	updated_filter = NoteFilter(order=NoteSortOrder.UPDATED)
	updated_filter.notebookGuid = firstID
	offset = 0
	max_notes = 10
	result_spec = NotesMetadataResultSpec(includeTitle=True)
	result_list = noteStore.findNotesMetadata(dev_token, updated_filter, offset, max_notes, result_spec)

	# note is an instance of NoteMetadata
	# result_list is an instance of NotesMetadataList


	for note in result_list.notes:
	    print note.title
	    notesContents[note.title] = noteStore.getNoteContent(note.guid)
	    allNotes.append(note)


	 
	print(' ')
	print( 'Username')
	print user.username    

	# note = Note()
	# note.title = "I'm a test note!"
	# note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
	# note.content += '<en-note>Testing Note</en-note>'
	# note.notebookGuid = firstID
	# note = noteStore.createNote(note)

	# print('successfully created a note!!')

	# return firstID



# CREATING A NOTE IN THE CURRENT NOTEBOOK
def createNote (firstID, title='I am a test title', contents= 'Testing Contents'):
	userStore = client.get_user_store()
	noteStore = client.get_note_store()
	note = Note()
	note.title = title
	note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
	note.content += '<en-note>' + contents + '</en-note>'
	note.notebookGuid = firstID
	note = noteStore.createNote(note)

	print('successfully created a note!!')


getFirstNoteBook()
print(firstID)
createNote(firstID)


# notes = noteStore.findNotes(authToken, filter, 0, 1000)
# for note in notes.notes:
#     print note.title



# noteStore.createNote('Hackathon test', 'This is the content of the note')




# Testing evernote api




@app.route('/auth')
def auth_start():
    """Makes a request to Evernote for the request token then redirects the
    user to Evernote to authorize the application using the request token.

    After authorizing, the user will be redirected back to auth_finish()."""

    client = get_oauth_client()

    # Make the request for the temporary credentials (Request Token)
    callback_url = 'http://%s%s' % ('127.0.0.1:5000', url_for('auth_finish'))
    request_url = '%s?oauth_callback=%s' % (EN_REQUEST_TOKEN_URL,
        urllib.quote(callback_url))

    resp, content = client.request(request_url, 'GET')

    if resp['status'] != '200':
        raise Exception('Invalid response %s.' % resp['status'])

    request_token = dict(urlparse.parse_qsl(content))

    # Save the request token information for later
    session['oauth_token'] = request_token['oauth_token']
    session['oauth_token_secret'] = request_token['oauth_token_secret']

    # Redirect the user to the Evernote authorization URL
    return redirect('%s?oauth_token=%s' % (EN_AUTHORIZE_URL,
        urllib.quote(session['oauth_token'])))


@app.route('/authComplete')
def auth_finish():
    """After the user has authorized this application on Evernote's website,
    they will be redirected back to this URL to finish the process."""

    oauth_verifier = request.args.get('oauth_verifier', '')

    token = oauth.Token(session['oauth_token'], session['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    client = get_oauth_client()
    client = get_oauth_client(token)

    # Retrieve the token credentials (Access Token) from Evernote
    resp, content = client.request(EN_ACCESS_TOKEN_URL, 'POST')

    if resp['status'] != '200':
        raise Exception('Invalid response %s.' % resp['status'])

    access_token = dict(urlparse.parse_qsl(content))
    authToken = access_token['oauth_token']

    userStore = get_userstore()
    user = userStore.getUser(authToken)

    # Save the users information to so we can make requests later
    session['shardId'] = user.shardId
    session['identifier'] = authToken

    return "<ul><li>oauth_token = %s</li><li>shardId = %s</li></ul>" % (
        authToken, user.shardId)


@app.route('/notebook')
def default_notbook():
    authToken = session['identifier']
    noteStore = get_notestore()
    notebooks = noteStore.listNotebooks(authToken)
    for notebook in notebooks:
            defaultNotebook = notebook
            break

    return defaultNotebook.name

# THIS IS ALL EVERNOTE API

app.run(debug = True)




