
def rpm():
    vc = input("What is the cutting speed in feet per minute?")
    d = input("What is the diameter of the cutter?")
    n = ((float(vc) * 12) / (3.14159 * float(d)))
    print(int(round(n)))

def cutting_speed():
    n = input("What is the RPM?")
    d = input("What is the diameter of the tool?")
    vc = ((float(n) * 3.14159 * float(d)) / (12))
    print(int(round(vc)))

def feed():
    n = input("What is the RPM? ")
    z = input("What is the numer of teeth? ")
    fz = input("What is the feed per tooth? ")
    vf = (float(n) * float(z) * float(fz))
    print(int(round(vf)))

def mmr():
    ae = input("What is the radial depth of cut? ")
    ap = input("What is the axial depth of cut? ")
    vf = input("What is the feed? (inches per min.) ")
    q = (float(ae) * float(ap) * float(vf))
    print(q)

mmr()
