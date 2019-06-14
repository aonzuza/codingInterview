




racks = 128;
results = [30046];

for i in range(racks - 1):

    results.append(results[-1] + 60);


print(results);
