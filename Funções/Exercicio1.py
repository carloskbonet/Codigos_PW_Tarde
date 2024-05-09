
def celsiusToFahrenheit(celsius:float):
    fahrenheit = float(0);

    fahrenheit = (celsius * 1.8) + 32;

    return fahrenheit;

def metersToFeets(meters:float):
    feets = float(0);

    feets = meters * 3.2808;

    return feets;    

def kmToMiles(kilometers:float):
    miles = float(0);

    miles = kilometers * 0.62137119;

    return miles;

result = float(0);

result = celsiusToFahrenheit(27);

print(f'27°C = {round(result , 2)}°F');

result = metersToFeets(1.8);

print(f'1.8 Metros = {round(result , 2)} Pés');

result = kmToMiles(321);

print(f'321 Km = {round(result , 2)} Miles');