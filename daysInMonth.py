def is_year_leap(year):

    is_year_leap = True
    if year < 1582 : is_year_leap = False
    elif year % 4 != 0 : is_year_leap = False
    elif year % 100 != 0 : is_year_leap = True
    elif year % 400 != 0 : is_year_leap = False
    
    return is_year_leap

def days_in_month(year, month):

    if (month > 12 or month < 1):
        return
    sep_apr_jun_nov = [4, 6, 9, 11]
    if (is_year_leap(year)):
        if month == 2 : return 29
        elif month in sep_apr_jun_nov: return 30
        else : return 31
    else : 
        if month == 2 : return 28
        elif month in sep_apr_jun_nov: return 30
        else : return 31




#TEST

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "-> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

