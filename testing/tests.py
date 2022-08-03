from OpenDateRange import DateRange
from testing.helper.timer import timer


@timer
def cal_length(date_range):
    return len(date_range)


dr = DateRange("2002-12-12", "2003-12-11")

print(cal_length(dr))
print(cal_length(dr))