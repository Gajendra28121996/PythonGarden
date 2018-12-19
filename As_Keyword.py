# The from keyword is used to import only a specified section from a module.
# The import keyword is used to import modules.
# The as keyword is used to create an alias. --  we create an alias, c, when importing the calendar module, and now we can refer to the calendar module by using c instead of calendar.
##### AS
import calendar as c
print(c.month_name[1])