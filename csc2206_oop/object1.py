class School:
    def __init__(self,name,sch_type):
        self.name=name
        self.sch_type=sch_type

##    def new_school(self, name, sch_type):
##        name = name
##        sch_type = sch_type

    def school_details(self):
         print('School name - ',self.name)
         print('School type - ',self.sch_type)


# Objects
school1=School('catuc','university')
school2=School('Uba','university')
school3=School('Gsb','secondary')

school1.school_details()
