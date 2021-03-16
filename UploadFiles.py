import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)    
        
        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AstVkzr296gyhcZOucSToJ_Ads4Bx9QAmUJGB7UHmVf2ccP3Mlsabs5cHOA5dSORF9dB5MBo5w29814MacU0ZNLWXH-0JxCmnI8hnlNDGIGauUTEZZ42DPzZ0F-eryFzkpfDLA8'
    transferData = TransferData(access_token)         
       
    file_from = input("Enter the  file path to transfer. ")
    file_to = input("Enter full path to upload to dropbox. ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved.")

main()