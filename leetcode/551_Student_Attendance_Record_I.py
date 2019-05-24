def should_get_A(records):

    return False if "LLL" in records or records.count('A') > 1  

records = "PPLLLP";


print(should_get_A(records));
