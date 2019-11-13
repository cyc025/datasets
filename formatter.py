
import sys 


new_data = open('{}.sorted'.format(sys.argv[1]),'w')
new_text = open('{}.sorted'.format(sys.argv[2]),'w')

trg_text = [line.replace('\n','') for line in list(open(sys.argv[2],'r').readlines())]

lines = [(index,line.replace('\n','')) for index,line in enumerate(list(open(sys.argv[1],'r').readlines()))]

sorted(lines,key=lambda tup: tup[1])

indices = []
curr_line = ''
counter = 0
for line_tup in lines:
    if curr_line==line_tup[1]:
        #do something
        indices.append(line_tup[0])
    else:
        if counter>0:
            indices.append(-1)
        indices.append(line_tup[0])
        curr_line = line_tup[1]
        new_data.write('{}\n'.format(line_tup[1]))
    counter += 1

# write text
write_count = 0
for index in indices:
    if index<0:
        new_text.write('\n')
    else:
        write_count += 1
        new_text.write('{}\n'.format(trg_text[index]))

print(write_count,len(trg_text))
assert write_count == len(trg_text)

new_text.close()
new_data.close()





