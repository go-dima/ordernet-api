from utils import format_currency


class Holding(object):
    def __init__(self, record):
        self.id = record['c']
        self.amount = record['bd']
        self.original_cost = record['be']
        self.current_value = record['bf']
        self.percentage = record['bk']
        self.en_description = record['i']
        self.he_description = record['j']
        self.unit_value = record['y']
        self.type = record['cg']
        self.profit = self.current_value - self.original_cost
        self.profit_percentage = (self.profit / self.original_cost) * 100

    def __str__(self):
        return self.en_description.ljust(20) + "\t" + \
               str(self.amount).ljust(15) + "\t" + \
               format_currency(self.current_value).ljust(15) + "\t" + \
               format_currency(self.profit).ljust(15) + "\t" + \
               f"{self.profit_percentage:.2f}%"
#
# c - Number (Symbol)		מספר נייר
# bd - Amount				כמות נוכחית
# be - Cost			    	        עלות
# bf - Current Value		שווי נוכחי
# bk - Percentage			אחוז אחזקה
# i - Eng description
# j - Heb Description		שם נייר
# y - Value 				שער
# cg - Type
# -----
# bf - be					שינוי מעלות
# (bf - be)/be		    	שינוי מעלות ב%
