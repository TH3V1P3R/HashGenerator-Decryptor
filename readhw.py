class rdw:
    def read(self, wordlist):
        f = open(wordlist, "r")
        return f.readlines()

