# IMMU-HAIKU
The goal of this application it's to ask the user to compose a haiku (a short poem of 3 lines).
Every line of the haiku it's insert and then upsert using the same 'id', then the complete haiku it's stored in the history of an entry.
To assure each haiku has only 3 lines, the 'haiku' table it's created with AUTO_INCREMENT on the PRIMARY KEY.
After inserting 3 lines the history it's retrieved and the whole haiku it's then tested to see if its valid

### 0. immudb-py doc 
Can't find any reference on how to use SQL with immudb-py, UPDATE: by trial-and error I discovered the sqlExec and sqlQuery

### 1. Can't Update AUTO_INCREMENT 
Using ALTER TABLE to make a column AUTO_INCREMENT doesn't seems to be working

### 2. Can't retrieve last identity
Cannot do something like SELECT SCOPE_IDENTITY(); to retrieve the last identity value inserted into an identity column in the same scope

### 3. PROPOSAL
Just as BEFORE TX works it could be interesting to have something like AFTER TX

### 4. No easy method to retrieve the whole history
```
eg: SELECT history FROM <table_name> WHERE id=<id>
```

### 5. 'USE SNAPSHOT BEFORE TX <N>'
Using 'USE SNAPSHOT BEFORE TX <N>' returns 'not yet supported'

### 6. Not able to concat a BEFORE TX with a SQL condition
```
SELECT * FROM (haiku10 BEFORE TX 203) WHERE id LIKE '28';
```