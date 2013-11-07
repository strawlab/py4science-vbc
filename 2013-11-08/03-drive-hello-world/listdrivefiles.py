
# ....
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apgooglelayer.oauth import get_drive_service
from apgooglelayer.drive import GoogleDrive


secrets = "./client-secrets.json"
service = get_drive_service(secrets, "py4science-example03")

Drive = GoogleDrive(service)

FileTree = Drive.folder_structure()
for name, treenode in FileTree.flatten_names():
    print name

