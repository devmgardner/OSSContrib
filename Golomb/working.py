from time import process_time as timer
start = timer()
from datetime import timedelta
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
fname = f'{currentdir}/Golomb-workinglog.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
#
def golomb(n):
    n = int(n)
    fhand.write(f'n is {n}\n')
    if n == 1:return 1
    temp = [1, 2, 2, 3, 3]
    fhand.write(f'temp is {temp}\n')
    while len(temp) < n:
        fhand.write(f'position {n} does not exist in temp, processing\n')
        #fhand.write(f'temp[{n}] does not exist, processing\n')
        #fhand.write(f'range(n) is {range(n)}\n')
        #fhand.write(f'range to process is {list(map(lambda x: x+1, range(n)))}\n')
        fhand.write(f'range to process is range(1,{n})\n')
        for i in range(n):
            fhand.write(f'----current number in range is {i+1}\n')
            #fhand.write(f'----i in range(n) is currently {i}\n')
            if len(temp) > i:
                fhand.write(f'\t----position {i+1} in temp exists: {temp[i]}\n')
                #fhand.write(f'\t----temp[{i}] exists: {temp[i]}\n')
                continue
            else:
                lastval = temp[-1]
                fhand.write(f'\t----position {i+1} in temp does not exist, appending\n')
                #fhand.write(f'\t----temp[{i}] does not exist, appending\n')
                fhand.write(f'\t\tlast value in current list is {lastval}\n')
                fhand.write(f'\t\tnext value to append is {lastval+1}\n')
                #fhand.write(f'item in temp at position {lastval} is {temp[lastval-1]}\n')
                fhand.write(f'\t\t\tnumber in position {lastval+1} in temp is {temp[lastval]}\n')
                fhand.write(f'\t\t\t\tappending {temp[lastval]} {lastval+1}s\n')
                for x in range(temp[lastval]):temp.append(lastval + 1)
                #fhand.write(f'\t\t\t\tafter processing {i}, temp is {temp}\n')
                fhand.write(f'\t\t\t\tprocessed {i+1}, temp is now {temp}\n')
                fhand.write(f'\t\t\t\tlength of temp is now {len(temp)}\n')
    fhand.write(f'final temp is {temp}\n')
    fhand.write(f'Number in position {n} in the Golomb sequence is {temp[n-1]}')
    end = timer()
    return (temp[n-1], end)
    #while not (n+1) in temp:
    #    fhand.write(f'n + 1 is not in {temp}\n')
    #    for i in range(n):
    #        fhand.write(f'\ti in range(n) is currently {i}\n')
    #        fhand.write(f'\t\ttemp[i] is currently {temp[i]}\n')
    #        for x in range(temp[i]):
    #            fhand.write(f'\t\t\tx in range(temp[i]) is currently {x}, appending i+1\n')
    #            temp.append(i+1)
    #
    #
    #
    #for elem in range(n + 1):
    #    for count in range(temp[elem]):
    #        temp.append(int(i))
    #return temp
result = golomb(input('Enter n> '))
print(f'Calculated answer {result[0]} in {timedelta(seconds=result[1]-start)} seconds.')
#1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11