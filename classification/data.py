import glob

all_filenames = glob.glob('../data/angles/*.txt')
def findFiles(path): return glob.glob(path)

# Build the category_lines dictionary, a list of names per language
category_lines = {}
all_categories = []

# Read a file and split into lines
def readLines(filename):
    lines = open(filename).read().replace('\t',' ').split('\n')
    sp_lines=[]
    for j in range(len(lines)):
        for i in lines:
            i = i.split()
            sp_lines.append(list(map(int, i)))
    return sp_lines

for filename in all_filenames:
    category = filename.split('\\')[-1].split('.')[0]
    print(category)
    all_categories.append(category)
    lines = readLines(filename)
    category_lines[category] = lines

n_categories = len(all_categories)

