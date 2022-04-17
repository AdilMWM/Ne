file = open('data/s.dat','r')
read = file.readlines()
y = {}

for stri in read:
    splitstr = stri.split()
    y = splitstr[4:]
    y = [int(i) for i in y]

    summ = sum(y)
    y1 = []
    y0 = []
    if summ > 0:
        y1 = y
        y1 = [str(e) for e in y1]
        y_str = ''.join([str(ii) + ' ' for ii in y1])
        y_str1 = splitstr[0] + ' ' + splitstr[1] + ' ' + splitstr[2] + ' ' + splitstr[3] + ' ' + y_str + '\n' 

        file1 = open('data/s111.dat','a')
        file1.write(y_str1)
        file1.close

    else:                   #дополнительный файл, который записывает в txt даты нулевых событий
        y0 = y
        y0 = [str(ee) for ee in y0]
        #y_str = ''.join([str(iii) + ' ' for iii in y0])
        y_str0 = splitstr[0] + ' ' + splitstr[1] + ' ' + splitstr[2] + ' ' + splitstr[3] + '\n' 

        file1 = open('data/s000.dat','a')
        file1.write(y_str0)
        file1.close
        