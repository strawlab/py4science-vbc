
# ....
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apgooglelayer.oauth import get_service
from apgooglelayer.drive import GoogleDrive
from apgooglelayer.spreadsheets import GoogleSpreadsheets

secrets = "./client-secrets.json"

service = get_service(secrets, ['https://www.googleapis.com/auth/drive',
               'https://spreadsheets.google.com/feeds']  , 'drive', 'v2', "py4science-example05a")


Drive = GoogleDrive(service)
Spreadsheets = GoogleSpreadsheets()




FileTree = Drive.folder_structure()

i = 0
for name, treenode in FileTree.flatten_names():
    if treenode.get('mimeType','') == 'application/vnd.google-apps.spreadsheet':
        i += 1
        if i > 5: break
        print "Id:", treenode['id']
        for j, cell in enumerate(Spreadsheets.get_cells_from_first_worksheet( treenode['id'], http=service._http )):
            if j >= 20: break
            print "%02d,%02d : %s" % (int(cell.cell.row), int(cell.cell.col), cell.content.text)
            




