class Employee:

    def __init__(self,name,empid,department,title):

        self.name=name
        self.id=empid
        self.department=department
        self.title=title


    def getname(self):
        return self.name

    def getid(self):
        return self.id

    def getdepartment(self):
        return self.department

    def gettitle(self):
        return self.title

    def setname(self,name):
        self.name=name

    def setid(self,empid):
        self.id=emp_id

    def setdepartment(self,dept):
        self.department=dept

    def settitle(self,title):
        self.title=title