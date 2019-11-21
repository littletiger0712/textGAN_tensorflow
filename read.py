import io
import pickle
def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = []
    flag = False
    for line in fin:
        if float == False:
            flag = True
            continue
        else:
            tokens = line.rstrip().split(' ')
            data.append([tokens[0],map(float, tokens[1:])])
    
    print(len(data))
    print(data[0])
load_vectors('wiki-news-300d-1M.vec')
