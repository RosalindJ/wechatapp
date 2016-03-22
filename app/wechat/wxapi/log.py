class Log_:
    def log_result(self,file,word):
        fp = open(self.file,"a")
        fp.write(self.word)
        fp.close();