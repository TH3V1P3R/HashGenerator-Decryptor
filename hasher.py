import hashlib
class h:
    def hashin(self,t,ht):
        t = t.encode("utf-8")
        ht = hashlib.new(ht)
        ht.update(t)
        return ht.hexdigest()
