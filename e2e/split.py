import csv
import sys

csv_file = sys.argv[1]


table_dict = {}

with open( csv_file ) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in list(csv_reader):
        table = row[0]
        text = row[1]
        if table in table_dict.keys():
            table_dict[table].append(text)
        else:
            table_dict[table] = [text]

print('Unique table rows: {0}'.format(len(table_dict.keys())))


total_rows = 0

eight_attr = 0
seven_attr = 0
six_attr = 0
five_attr = 0
four_attr = 0
three_attr = 0

train_set = []
test_dev_set = []

def save(dataset,k,v):
    for text in v:
        dataset.append( (k,text) )

for k,v in table_dict.items():
    total_rows += len(v)
    if len(k.split(','))==8:
        eight_attr += len(v)
        save(test_dev_set,k,v)
    if len(k.split(','))==7:
        seven_attr += len(v)
        save(train_set,k,v)
    if len(k.split(','))==6:
        six_attr += len(v)
        save(train_set,k,v)
    if len(k.split(','))==5:
        five_attr += len(v)
        save(train_set,k,v)
    if len(k.split(','))==4:
        four_attr += len(v)
        save(train_set,k,v)
    if len(k.split(','))==3:
        three_attr += len(v)
        save(test_dev_set,k,v)

print('Table with 8 attributes: {0}'.format(eight_attr))
print('Table with 7 attributes: {0}'.format(seven_attr))
print('Table with 6 attributes: {0}'.format(six_attr))
print('Table with 5 attributes: {0}'.format(five_attr))
print('Table with 4 attributes: {0}'.format(four_attr))
print('Table with 3 attributes: {0}'.format(three_attr))

print('Table with all attributes: {0}'.format(total_rows))


print('Train set size {0}'.format(len(train_set)))
print('Test set size {0}'.format(len(test_dev_set)))

import random

indices = random.sample(list(range(len(train_set))),3367)

print('Adding {}'.format(len(indices)))


def write_data(filename=None,dataset=None):
    # write to train file
    train_data = open('{}.data'.format(filename),'w')
    train_text = open('{}.text'.format(filename),'w')
    for t in dataset:
        train_data.write('{}\n'.format(t[0]))
        train_text.write('{}\n'.format(t[1]))
    train_data.close()
    train_text.close()


new_train_set = []
for i,t in enumerate(train_set):
    if i in indices:
        test_dev_set.append(t)
    else:
        new_train_set.append(t)

print('Train set size {0}'.format(len(new_train_set)))
print('Test/dev set size {0}'.format(len(test_dev_set)))


# write to train file
write_data(
    filename='train',
    dataset=new_train_set
)

testset = []
devset = []
test_indices = random.sample(list(range(len(test_dev_set))),630)
for i,t in enumerate(test_dev_set):
    if i in test_indices:
        testset.append(t)
    else:
        devset.append(t)

# write to test/dev file
write_data(
    filename='test',
    dataset=testset
)
write_data(
    filename='dev',
    dataset=devset
)





