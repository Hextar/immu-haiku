from immudb import ImmudbClient
import re

_IMMUDB_HOST_ = 'localhost'
_IMMUDB_PORT_ = 3322
_IMMUDB_USER_ = 'immudb'
_IMMUDB_PASS_ = 'immudb'
_TABLE_NAME_ = 'haikus_1'

# Instantiate the client class
# Note that "localhost:3322" is the default immudb port,
ic = ImmudbClient(_IMMUDB_HOST_ + ':' + str(_IMMUDB_PORT_))

# login using the default immudb credentials
ic.login(username=_IMMUDB_USER_, password=_IMMUDB_PASS_)

def escapeString(str):
	return re.sub('\W+','', str )

def createTable():
	ic.sqlExec('CREATE TABLE IF NOT EXISTS ' + _TABLE_NAME_ + ' (id INTEGER AUTO_INCREMENT, line VARCHAR, PRIMARY KEY id);')

def addAutoincrement():
	ic.sqlExec('ALTER TABLE ' + _TABLE_NAME_ + ' COLUMN id INT AUTO_INCREMENT;')

def fetchIdByTxId(txId):
	return ic.sqlQuery('SELECT * FROM (' + _TABLE_NAME_ + ' BEFORE TX ' + str(txId + 1) + ');')[-1:][0][0]

def insertLine(line):
	return ic.sqlExec('INSERT INTO ' + _TABLE_NAME_ + ' (line) VALUES (\'' + escapeString(line) + '\');')

def upsertLine(id, line):
	return ic.sqlExec('UPSERT INTO ' + _TABLE_NAME_ + ' (id, line) VALUES (' + str(id) + ', \'' + escapeString(line) + '\');')

def fetchLine(txId, n, id):
	return ic.sqlQuery('SELECT * FROM (' + _TABLE_NAME_ + ' BEFORE TX ' + str(txId + n) + ') WHERE id=' + str(id) + ';')[0][1]
