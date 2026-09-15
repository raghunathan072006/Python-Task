try:
    a=10
    b=int("tt")
    print(a+b)
    c=[1,3]
    print(c[0])
except NameError:
    print(d)
except TypeError:
    print("invalid type error")
except ValueError:
    print("invalid value error")
except IndexError:
    print("index error")
else:
    print("working else")
finally:
    print("working finally")