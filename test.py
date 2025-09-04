
# print("hello world")


def kusok_koda(): 
    # for i in range(0, 3):
    #     print("kusok_koda")

    i = 0
    while i != 3:
        print("kusok_koda")
        i += 1


def kusok_koda_1(i, text):
    while i != 3:
        print(text)
        i += 1


int = 4
print(int)
int2 = -1
int = int + int2
b = int == 3
if b: 
    int = int2
else: 
    if int2 == -1:
        int = 10
    else:
        int = 2



# циклы

while b: 
    int += 1
    if int == 3: 
        b = False
    print(b)

# l = [3, 4, 5, 6]
# l = range(3, 7)

for i in range(3, 7):
    print(i)



# методы

kusok_koda()
kusok_koda_1(1, "kusok_koda_1")




# словари

# dictionary = {"key": "value", "key1": "value1"}
dictionary = {1: True, 1: False}

print(dictionary)


data = [
    {
        "name": "Petar",
        "country": "Russia"
    },
    {
        "name": "Kolya",
        "country": "Russia"
    },
    {
        "name": "Gans",
        "country": "Germany"
    },
    {
        "name": "Ilya",
        "country": "Russia"
    },
    {
        "name": "SunHuy",
        "country": "Japan"
    },
    {
        "name": "Braynt",
        "country": "USA"
    },
]

grouped_data = {}

for d in data:
    d_country_value = d["country"]
    if grouped_data.get(d_country_value) is None:
        grouped_data[d_country_value] = 1
    else:
        grouped_data[d_country_value] += 1
    
print(grouped_data)
