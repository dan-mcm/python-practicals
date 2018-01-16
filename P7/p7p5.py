#counter for loop
count = 1
#variable to hold total to print at end
total = 0

while count <= 10000:
    if count % 3 == 0:
        total += count;
    if count % 5 == 0:
        total += count;
    count += 1
    
print ( 'Sums of integers in range 1 - 10,000 that are divisble by 3 or 5 = ', total)
