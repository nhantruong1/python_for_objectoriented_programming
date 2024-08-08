
class Date:
    def __init__(self, year, month, day):   # Constructor / Init method
        self.year = year
        self.month = month  # Instance attribute
        self.day = day
        
    def arrange_value_into_Data_pattern(self):  # Instance method
        date = str(self.day) + '-' + str(self.month) + '-' + str(self.year)
        return date
    
    @classmethod
    def from_string(cls, string): # Class method
        import re
        # 00-00-0000 or 00/00/0000
        date = re.findall(r'\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}', string)[0]
        list_date = date.replace('/', '-').split('-')
        date = list_date[0]
        month = list_date[1]
        year = list_date[2]
        return cls(year,month,date)
    
    @staticmethod   # 2022-05-12 --> 12-05-2022
    def setDatePattern(string):
        list1 = string.replace('/', '-').split('-')
        date_update = list1[0]
        month_update = list1[1]
        year_update = list1[2]
        date = date_update + '-' + month_update + '-' + year_update
        return date
        
date1 = Date(2021, 5, 12)
date2 = Date.from_string('12/05/2021')
print(date2.arrange_value_into_Data_pattern())
date3 = Date.setDatePattern('2022-05-12')