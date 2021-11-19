import dropbox 
class transferdata:
    def_init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_too):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb')as f:
            dbx.file_upload(f.read(),file_too)
def main():
        access_token='sl.A8lJE7N3RAVtfLJvDYv5x1sOaP4gYkCPcr1c_oLqXv-nFu-nEs94JlvC7ejEYRl55ttWcJ2fkUcQVBslzt2g5_1TlA0UEsniij7OP_qWXoJuPn3FII5DfTgDJltgr24rzpz-lpw'
        transferdata=transferdata(access_token)
        file_from='test.txt'
        file_too='/test_dropbox/test.txt'
        transferdata.upload_file(file_from,file_too)
        print("file has been moved")
main()