def is_year_leap(year):
    """
    Function that determines if the year is a leap year

    """

    is_year_leap = True
    if year < 1582 : is_year_leap = False
    elif year % 4 != 0 : is_year_leap = False
    elif year % 100 != 0 : is_year_leap = True
    elif year % 400 != 0 : is_year_leap = False
    
    return is_year_leap


#
# Test for code.
#

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

