from libs import *

class Conectivos():

    def inserirData(self):
        self.data = self.calen.get_date()
        if len(self.data) == 0 or len(self.data) != 0:
            self.calen.destroy()
        self.et_data.delete(0, END)
        self.et_data.insert(0, self.data)
        self.confirmaData.destroy()