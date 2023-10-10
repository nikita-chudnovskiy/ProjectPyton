class DataBase:
    __instance = None


    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __del__(self):
        DataBase.__instance =None
    def __init__(self,user,psw,port):
        self.user = user
        self.psw = psw
        self.port = port


    def connect(self):
        print(f"Соединение с БД {self.user}, {self.psw}, {self.port}"  )

db =DataBase('root','1234',80)
db2 =DataBase('root2','5678',80)

print(id(db))
print(id(db2))
db2.connect()   # Тут нужен будет еще метод __cal__(cls, *args, **kwargs):
