def timestamp():
    a,b,c = (int(i) for i in input("Write current time: ").split())
    x,y,z = (int(i) for i in input("Write current time: ").split())
    difference = (x*60*60+y*60+z) - (a*60*60+b*60+c)
    print(a,b,c,x,y,z,'Difference between them', difference)
timestamp()