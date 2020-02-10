import os
import urllib.request
# from pprint import pprint as pp

# remember to uncomment this before submittion
TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

# =============================================================================
# PY_BOOK, OTHER_BOOK = '🐍', '.' # remove this line before submitting
# DATA = 'safari.logs'
# =============================================================================

def create_chart():
    
    with open(DATA, 'r') as f:
        data = f.read().strip().split('\n')
        entries = list(_pairup(data))
        
        entries_dict = dict()
        
        for entry in entries:
            
            if 'slack' in entry[1]:
                date = entry[0][:5]
                entries_dict.setdefault(date, '')
                
                if 'python' in entry[0].lower():
                    entries_dict[date] += PY_BOOK   
                else:
                    entries_dict[date] += OTHER_BOOK
                
        for k, v in entries_dict.items():
            print(k, v)
        
def _pairup(iterable):
    "Helper function to pair up lines in the log entries"
    x = iter(iterable)
    return zip(x, x)
    
# create_chart()