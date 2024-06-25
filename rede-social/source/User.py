class User:
    def __init__(self,id,name,received,count_received,sent,count_sent):
        self.id = id
        self.name = name
        self.received = []
        self.count_received = 0
        self.sent = []
        self.count_sent = 0