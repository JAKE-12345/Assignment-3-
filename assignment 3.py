# Car dealership, Toyota car, Benz, Rolls Royce etc, each car has its own sale price, write a code that asks the person buying a car the brand of car that he/she wants. 
#Over 30 cars minimum
#GitHub - JAKE-12345
#Github link - https://github.com/JAKE-12345?tab=repositories
#6930821 - Atsuste Johnson Kingsley
print("Welcome to JAE's Wheels, affordable quality cars for everybody. /" 
      "Walk into a JAE's autoshop and leave with a brand new set of wheels today!")
sports_cars = {'Tesla model S': 94990, 'Tesla model E': 129990 , 'Tesla model X' : 138990 ,
               'BMW M5' : 107900, 'BMW M4' : 87495, 'BMW M3' : 75295 , 
               'Nissan 370z' : 43499, 'Nissan GTR Egoist' : 299950, 'Nissan GTR' : 113540 ,
               'Dodge Challenger' : 44000, 'Dodge Hellcat' : 81040, 'Dodge Demon' : 169995 , 
               'Koeinisegg Agera R' : 1500000, 'Koeinisegg Reggera' : 1900000,'Koeinisegg Gemera' : 1700000 , 
               'Porsche 911 carrera s' : 107550, 'Porsche 918 spyder' : 1584931, 'Porsche Taycan' : 190000 , 
               'Ford f150' : 84910, 'Ford Raptor' : 78480, 'Ford Ranger' : 39945 , 
               'Bugatti Chiron' : 3250000, 'Bugatti Veyron' : 1200000, 'Bugatti Divo' : 5400000 , 
               'Lamborghini Aventador SVJ': 864749, 'Lamborghini Huracan spyder' : 215204, 'Lamborghini Gallardo' : 173690 ,
               'Rolls Royce Phantom' : 467750, 'Rolls Royce Cullinan' : 351250, 'Rolls Royce Ghost' : 343000,}
print('Hi, i am Johnson. I will be attending to you today Sir/Madame ')
name_of_client = input('What may i refer to you as Sir/Madame? : ')
print("Welcomme to JAE's Wheels " + name_of_client)
car_type = input("What are we looking to cruise in today " + name_of_client + "? :")
if car_type in sports_cars :
    print("We've got it, just how you want it. " + name_of_client)
    print("She is a beauty worth...  $" + str(sports_cars[car_type] ))
else:
    print("Oops!, we currently don't have that spec of car you want." + name_of_client + " But we'll be sure to get it around next time")
    
    