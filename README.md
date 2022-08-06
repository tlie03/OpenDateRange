# OpenDateRange
This is a Python package that provides date ranges which allow open borders.
Thereby it is possible to create date ranges that contain all dates 
up to a certain date or all dates from a certain date on. Of course date ranges 
with concrete dates as borders are supported as well. But there is no support
for any kind of daytime measurement. 

## Technical information
The package was developed with python 2.7.18 and only uses the build in 
python packages abc and datetime.

## Description of the provided Interface
This package provides only one class which is the DateRange class.
The following sections describe how to use this class and how to 
interact with its instances.
* [Date formats](#date-formats)
* [Creating date ranges](#creating-date-ranges)
* [Representation of date ranges](#Representation-of-date-ranges)
* [Contains operator](#contains-operator)
* [Intersection between date ranges](#intersection-between-date-ranges)
* [Infinite date ranges](#infinite-date-ranges)
* [Date range iterator](#date-range-iterator)
* [Date range length](#date-range-length)

### Date formats
The package supports all datetime formats that are supported by the 
build in datetime package. The date format can be changed via 
the static attribute DATE_FORMAT that belongs to the DateRange class and
is predefined as "%Y-%m-%d". When the date format is changed 
all dates that are involved in interactions with instances of the DateRange
class must match the new date format. Furthermore, all dates that are returned
by any methods of the DateRange class match the new format as well.
#### Example
```
print(DateRange.DATE_FORMAT)
>>> %Y-%m-%d
```
Accepts and outputs only dates of the "%Y-%m-%d" format.
```
DateRange.DATE_FORMAT = "%Y.%m.%d"
print(DateRange.DATE_FORMAT)
>>> %Y.%m.%d
```
Now accepts and outputs only dates of the "%Y.%m.%d" format.

### Creating date ranges
### Representation of date ranges
### Contains operator
### Intersection between date ranges
### Infinite date ranges
### Date range iterator
### Date range length


