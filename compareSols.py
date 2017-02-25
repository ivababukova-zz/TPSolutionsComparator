import sys

# read file and extract the pieces for comparison
def readSol(solfile):
    sols = []
    with open(solfile, "r") as f:
        sol = []
        for line in f.readlines():
            line = line.split()
            if len(line) == 0:
                sols.append(sol)
                sol = []
            if len(line) > 2 and line[0] == "Schedule:":
                trip = []
                for flight in line[1:]:
                    trip.append(int(flight))
                sol.append(trip)
            elif len(line) == 2:
                sol.append(float(line[1]))
    return sols

def compare(sols1, sols2):
    areEqual = True
    for sol1 in sols1:
        if not sol1 in sols2:
            areEqual = False
            print(sol1)
    if not areEqual:
        print("not in ip")
    areEqual = True
    for sol2 in sols2:
        if not sol2 in sols1:
            areEqual = False
            print(sol2)
    if not areEqual:
        print("not in cp")

# python compareSols.py <cpsol filename> <ipsol filename>
ipfile = sys.argv[1]
cpfile = sys.argv[2]

ipsol = readSol(ipfile)
cpsol = readSol(cpfile)
compare(ipsol, cpsol)
