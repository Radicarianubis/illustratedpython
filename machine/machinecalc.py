
def rpm():
    vc = input("What is the cutting speed? (feet per minute) ")
    d = input("What is the diameter of the cutter? (inches) ")
    n = ((float(vc) * 12) / (3.14159 * float(d)))
    print(f"{int(round(n))} RPM")

def cutting_speed():
    n = input("What is the RPM? ")
    d = input("What is the diameter of the tool? (inches) ")
    vc = ((float(n) * 3.14159 * float(d)) / (12))
    print(f"{(round(vc, 1))} feet per minute")

def feed():
    n = input("What is the RPM? ")
    z = input("What is the numer of teeth? ")
    fz = input("What is the feed per tooth? (thousandths of an inch) ")
    vf = (float(n) * float(z) * float(fz))
    print(f"{(round(vf, 1))} inches per minute")

def mmr():
    ae = input("What is the radial depth of cut? (inches) ")
    ap = input("What is the axial depth of cut? (inches) ")
    vf = input("What is the feed? (inches per min.) ")
    q = (float(ae) * float(ap) * float(vf))
    print(f"{(round(q, 1))} cubic inches per minute of material removed")

rpm()
cutting_speed()
feed()
mmr()

