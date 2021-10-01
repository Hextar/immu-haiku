# This allow the user to store immutable a haiku
# in immudb using SQL inserts
# What's a Haiku? https://en.wikipedia.org/wiki/Haiku

from sql import createTable, fetchIdByTxId, insertLine, upsertLine, fetchLine 
from haiku import validate_haiku 
import sys

# --- CREATE TABLE ------------------------
try:
    # create the haiku table
    createTable()

except Exception as e:
    print('Err: Error creating table', e)
    sys.exit(1)

# --- WRITE HAIKU ------------------------
try:
    print('Let\'s write a Haiku\n------')
    
    # 1. ask for haiku first line, insert it and retrieve the txId
    txId = insertLine(input('Enter first line: ')).dtxs[0].id

    # retrieve last autoincremental id by using txId
    id = fetchIdByTxId(txId)

    # 2. ask for haiku second line and upsert it by id
    upsertLine(id, input('Enter second line: '))

    # 3. ask for haiku second line and upsert it by id
    upsertLine(id, input('Enter third line: '))

except Exception as e:
    print('Err: while writing haiku', e)
    sys.exit(1)

# --- READ HAIKU ------------------------
try:
    haiku = fetchLine(txId, 1, id) + '\n' + \
        fetchLine(txId, 2, id) + '\n' + \
        fetchLine(txId, 3, id)
except Exception as e:
    print('Err: while reading haiku', e)
    sys.exit(1)

# --- CHECK HAIKU ------------------------
try:
    # Haiku validation, examples:
    # VALID: I've used immudb...\nTo write a haiku,\nsplash! Silence again.
    # VALID: I've used immubd...\nHaiku is in its history,\nwith sql, Validated!.
    # NOT VALID: Autumn moonlight -\nA worm digs silently\ninto the chestnut.
    if validate_haiku(haiku):
        print('------\nCongrats, That\'s a valid Haiku!')
    else:
        print('------\nDang, not a valid Haiku, probably just a Senryū')
            
except Exception as e:
    print('Err: while checking haiku', e)
    sys.exit(1)