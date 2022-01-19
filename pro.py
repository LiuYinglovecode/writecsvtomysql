import sys
def search(args):
    with open('sql.txt', 'r') as f:
        c=0
        a = []
        for l in f.readlines():
            l = l.strip()
            c+=1
            if l == "":
                a.append(c)
        step = 2
        list__ = [a[i:i+step] for i in range(0, len(a)-1, 1)]
        for ii in list__:
            ii[0] = ii[0] + 1
            ii[1] = ii[1] - 1
            f.seek(0)
            temp = f.read().splitlines()
            for x in temp[ii[0]:ii[1]]:
                if args in x:
                    neww = temp[ii[0]+1:ii[1]]
                    s = ii[1] - ii[0] - 2
                    string = ''.join([str(i) for i in neww])
                    new = (string, s)
                    return(new) 
# uncomment this if need to be executed as a script from the command-line
#if __name__== "__main__":
#    args = str(sys.argv[1])
#    search(args)
