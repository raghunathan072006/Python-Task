class distance:
    def __init__(self):
        self.feet = 0
        self.inch = 0

    def get_distance(self):
        self.feet = int(input("Enter the distance in feet"))
        self.inch = int(input("Enter the distance in inch"))

    def display(self):
        print("feet :", self.feet)
        print("inch :", self.inch)


d1 = distance()
d2 = distance()
d3 = distance()
d4 = distance()

choice = int(input("Enter your choice (1/2/3/4)"))

if choice == 1:
    d1.get_distance()
    d2.get_distance()

    d3.feet = d1.feet + d2.feet + (d1.inch + d2.inch) // 12
    d3.inch = (d1.inch + d2.inch) % 12

    print("Distance 1")
    d1.display()

    print("Distance 2")
    d2.display()

    print("The sum of distance")
    d3.display()

elif choice == 2:
    d1.get_distance()
    d2.get_distance()
    d3.get_distance()
    d4.get_distance()

    d3.feet = (d1.feet + d2.feet + d3.feet + d4.feet) // 4
    d3.inch = (d1.inch + d2.inch + d3.inch + d4.inch) // 4

    print("The average of distance")
    d3.display()

elif choice == 3:
    d1.get_distance()
    d2.get_distance()
    d3.get_distance()
    d4.get_distance()

    # Find minimum distance
    distances = [d1, d2, d3, d4]

    minimum = distances[0]

    for d in distances:
        if (d.feet * 12 + d.inch) < (minimum.feet * 12 + minimum.inch):
            minimum = d

    print("Minimum distance")
    minimum.display()

elif choice == 4:
    d1.get_distance()
    d2.get_distance()
    d3.get_distance()
    d4.get_distance()

    # Find maximum distance
    distances = [d1, d2, d3, d4]

    maximum = distances[0]

    for d in distances:
        if (d.feet * 12 + d.inch) > (maximum.feet * 12 + maximum.inch):
            maximum = d

    print("Maximum distance")
    maximum.display()