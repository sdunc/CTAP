#Point fixer for poly maps


read_file = open('2008_coords.txt','r')
write_file = open('2.txt','w')

DELTA_LL = 0.03125

for line in read_file:
    ll = line.split(',')
    lon_fixed = float(ll[0])+DELTA_LL
    lat_fixed = float(ll[1])-DELTA_LL
    fixed_point = str(lon_fixed)+','+str(lat_fixed)
    write_file.write(fixed_point)
    write_file.write('\n')

read_file.close()
write_file.close()
    
    
