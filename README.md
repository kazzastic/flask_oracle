# Flask oracle

```python 
pip install Flask
pip install cx_Oracle
```
- Made on sqlite3 pre-installed with python3.X .

- Made on oracle DB 11g can be installed just google it.


- Entire tutorial can be seen 
[here](http://flask.pocoo.org/docs/1.0/tutorial/factory/)


- The rest of oracle cx_oracle has been seen from various documentations mainly [here](https://cx-oracle.readthedocs.io/en/latest/cursor.html)

- To run the server
#Linux
___
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
___
- In order for the DB to initialize run this 
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask init-db
```


