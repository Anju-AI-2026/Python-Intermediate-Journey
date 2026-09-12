# Program 9: Create a list containing names of routes with noise below 50
routes = [
    {"name": "Route A", "noise": 30},
    {"name": "Route B", "noise": 65},
    {"name": "Route C", "noise": 40},
    {"name": "Route D", "noise": 80}
]
new_routes = [route["name"] for route in routes if route["noise"] < 50]
print(new_routes)


# Program 10: Create a list containing IDs of decisions with confidence below 50
decisions = [
    {"id": 1, "confidence": 80},
    {"id": 2, "confidence": 45},
    {"id": 3, "confidence": 65},
    {"id": 4, "confidence": 30}
]
new_decisions = [decision["id"] for decision in decisions if decision["confidence"] < 50]
print(new_decisions)


# Program 11: Create a list containing only integer values from mixed data
data = [10, "hello", 25, "45", 30, "python", 50, 2.25]
new_data = [num for num in data if isinstance(num, int)]
print(new_data)


# Program 12: Flatten a nested list into a single list
numbers = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]
new_numbers = [num for row in numbers for num in row]
print(new_numbers)