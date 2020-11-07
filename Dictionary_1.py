day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
abc = ['yes', 'sure', 'yup', 'yeah', 'y']

# schedule for sunday, monday, tuesday, wednesday, thursday
time_schedule = {
   "8am" : "Wake up",
   "8am-9am" : "Freshen up and have breakfast" ,
   "9am-9:20am" : "Free time!!!" ,
   "9:20am-10am" : "Onlie class 'IK IT SUCKS BUT ITS REALITY'" ,
   "10am-1:30pm" : "Bunk classes -_-" ,
   "1:30pm-2pm" : "WORK OUT!!!!" ,
   "2pm-2:30pm" : "Shower" ,
   "2:30pm-3pm" : "Lunch" ,
   "3pm-8am" : "Sleep"
}   

# different schedule for Friday and Saturday
time_schedule_2 = {
    '10am' : 'Wake up' ,
    '10am-11am' : 'Freshen up and have lunch' ,
    '11am-12pm' : 'Stare at books' ,
    '12pm-1pm' : 'Play games' ,
    '1pm-2pm' : 'Play games' ,
    '2pm-3pm' : 'Play games' ,
    '3pm-10am' : 'Play games'
}


# the operation section
def main_frame():
    for i in day:
        user = input('Enter a day : ')
        # if user.lower() == i[-1]:
        if user.lower() == 'saturday' or user.lower() == 'friday':
            for x, y in time_schedule_2.items():
                user_3 = input('Enter a time : ')
                if user_3 in x:
                    print(print(user.title() + ' : ' +  x + ' : ' + y))
                    break
                else:
                    print("That is not in your schedule!!!")
                    break
        else:
            for key, value in time_schedule.items():
                user_2 = input('Enter the time : ')
                print(key, user_2)
                if user_2 == key:
                    print(user.title() + ' : ' + key + ' : ' + value)
                    break
                else:
                    print("That is not in your schedule!!!")
                    break


main_frame()