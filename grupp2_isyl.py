#Mario
#16.01.21


# 4. List Less Than Ten
# 	Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
# 		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
# 	Write this in one line of Python.
# 	Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
kasutaja = 5
for i in a: new_list.append(i) if i<kasutaja else 0
print(new_list)

exit()

# 2. Vanused
# 	loo vanuste loend 1p
# 	leia numbrite suurim ja väikseim arv  1p
# 	kogusumma  1p
# 	keskmine 1p

vanused=[7,6,5,19,18,18,17,20,15,11,7,10,13,12,20,11,10,14,18,14,24,6,17,16,6,17,5,13,11]
def vanuste_stat(loend):
    maks = max(vanused)
    miin = min(vanused)
    summa = 0
    for i in vanused:
        summa+=i
    print(f"Maksimum: {maks} Miinimum: {miin} Summa: {summa}")
vanuste_stat(vanused)