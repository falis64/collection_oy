# Movie ratings program

## The task was to make a new version of the movie ratings program


```
## Ask the user for their age
years = input("how old are you?")
age = int(years)
### Do not let the user enter an incorrect value (ages over 117 and ages under 1)
if age > 117:
    print("This is not a valid age")
elif age <= 1:
    print("This is not a valid age")
#### Program should tell them what rated movies they can watch (so if 13 they can watch U, PG and 12 rated movies)
elif age >= 18:
    print("The movie rating that are available to you are pg, 12, 15, 18")
elif age >= 15:
    print("The movie ratings that are available to you are pg, 12 and 15")
elif age >= 12:
    print("The movie ratings that are available to you are pg and 12")
```