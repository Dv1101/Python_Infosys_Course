print ( ' enter the number of days ' )
days = int ( input ( ) )
years = days // 365
weeks = ( days & 365 ) // 7
days_remaining = days - years * 365 - weeks * 7
print ( ' Years : ', years ) 
print ( ' Weeks : ' ,weeks )
print ( ' Days : ' ,days_remaining )