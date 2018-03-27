'''
Index file of the back end.
'''

import sys
from project.routes import app
from project.db import DatabaseInit


options = ['help', 'runserver', 'initdb']

if __name__ == '__main__':
    port = 4001
    if len(sys.argv) < 2 or not sys.argv[1] in options:
        print('''
              Error: Unrecognized option.
              Run 'python3 runserver.py help' for available options.
              ''', end = '')
    elif sys.argv[1] == 'help':
        print('''
              Available options are:
                  help      - Show available options.
                  initdb    - Initialize the database. Please modify the parameters in db.py first.
                  runserver - Start the back-end application. Default port is 4001.
              ''')
    elif sys.argv[1] == 'initdb':
        DatabaseInit()
        print('Database initialize success.')
    elif sys.argv[1] == 'runserver':
        app.run(host = '127.0.0.1', port = port)