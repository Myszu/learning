# Create a "Calendar" object with two int type arguments: 'year', 'month'
# and one optional int type argument 'first_day' with default value of 0.
# When used as below:
# 
# calendar = Calendar(2026, 3)
# calendar.draw_calendar()
# 
# will the code should output:
# 
# ['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
# ['23.02', '24.02', '25.02', '26.02', '27.02', '28.02', '01.03']
# ['02.03', '03.03', '04.03', '05.03', '06.03', '07.03', '08.03']
# ['09.03', '10.03', '11.03', '12.03', '13.03', '14.03', '15.03']
# ['16.03', '17.03', '18.03', '19.03', '20.03', '21.03', '22.03']
# ['23.03', '24.03', '25.03', '26.03', '27.03', '28.03', '29.03']
# ['30.03', '31.03', '01.04', '02.04', '03.04', '04.04', '05.04']
# 
# use only below imports and base python functions:
# 
# from datetime import date, timedelta