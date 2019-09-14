#stephen Duncanon
#txt prep

YEAR = 'i1980'


#STEP 1, GET RID OF WHITE SPACE
read_file = open('doc.txt','r')
write_file = open('out.txt','w')
for line in read_file:
    if line !="\n":
        write_file.write(line)
read_file.close()
write_file.close()



#STEP 2, get only needed lines
read_file = open('out.txt','r')
write_file = open('out2.txt','w')
save_next_line = 0
for line in read_file:
    if save_next_line == 1:
        write_file.write(line)
        save_next_line = 0
    #THESE MIGHT NEED TO BE CHANGED
    if line == "<td>Download PDF</td>\n" or line == "          <altitudeMode>clampToGround</altitudeMode>\n":
        save_next_line = 1
read_file.close()
write_file.close()


#Step 3. seperate links out only odd rows n=1
read_file = open('out2.txt','r')
write_file1 = open('links.txt','w')
write_file2 = open('coords.txt','w')
line_counter = 1
for line in read_file:
    if line_counter % 2 != 0:
        write_file1.write(line)
        line_counter +=1
    else:
        write_file2.write(line)
        line_counter += 1
      
read_file.close()
write_file1.close()
write_file2.close()

#Step 4, clean up
read_file1 = open('links.txt','r')
read_file2 = open('coords.txt','r')
write_file1 =open(YEAR+'_links.txt','w')
write_file2 = open(YEAR+'_coords.txt','w')

for line in read_file2:
    #part1 = line.split('>')[1]
    #part2 = part1.split('<')[0]
    #part3 = part2.split(',')
    #coords = part3[0]+','+part3[1]
    raw = line.split(' ')[12]
    raw_1= raw.split(',')
    coords = raw_1[0]+','+raw_1[1]
    
    #raw = line.split(',')
    #coords = raw[0].lstrip('\t')+','+raw[1]
    write_file2.write(coords+'\n')

for line in read_file1:
    try:
        linktxt = (line.split('"')[3])
    except:
        IndexError
    write_file1.write(linktxt+'\n')


write_file1.close()
write_file2.close()
read_file1.close()
read_file2.close()
