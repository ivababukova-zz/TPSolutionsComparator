import sys

# read file and extract the pieces for comparison
def readSol(solfile):
    sols = []
    with open(solfile, "r") as f:
        for line in f.readlines():
            line = line.split()
            if len(line) > 2 and line[0] == "Schedule:":
                trip = []
                for flight in line[1:]:
                    trip.append(int(flight))
                sols.append(trip)
            elif len(line) == 2:
                sols.append(float(line[1]))
    return sols

def compare(sol1, sol2):
    for i1, i2 in zip(sol1, sol2):
        if not i1 == i2:
            return(False, i1, i2)
    return([True])

# python compareSols.py <ipsol filename> <cpsol filename>
ipfile = sys.argv[1]
cpfile = sys.argv[2]

ipsol = readSol(ipfile)
cpsol = readSol(cpfile)
areSame = compare(ipsol, cpsol)
if not areSame[0]:
    print(ipfile, cpfile, " are not the same, at least ", areSame[1:], " differ.")
