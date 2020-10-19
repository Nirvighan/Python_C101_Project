# IMPORT NEEDED LIBRARIES
import dropbox
import os

# CREATE THE TRANSFER DATA CLASS
class TransferData:

    # CREATE THE INIT FUNCTION
    def __init__(self,accessToken):
        self.accessToken = accessToken

    # CREATE A FUNCTION FOR UPLOADING FILE ON DROPBOX
    def UploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

    
# CREATE THE MAIN FUNCTION    
def main():
    accessToken = '3r652F1gy6QAAAAAAAAAAXPSMVagVaDPkYVvDWbjOEJZtuf3P1gZDEfdAPilPTCz'
    transferdata = TransferData(accessToken)

    file_from = input("ENTER THE FILE NAME")
    file_to = input("ENTER THE FULL PATH")

    transferdata.UploadFile(file_from,file_to)



# CALL THE MAIN FUNCTION
main()