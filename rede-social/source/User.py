class User:
    def __init__(self,id_user,name,received,count_received,sent,count_sent,email):
        self.id_user = id_user
        self.name = name
        self.received = []
        self.count_received = 0
        self.sent = []
        self.count_sent = 0
        self.email = email


