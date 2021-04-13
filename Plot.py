'''
Data from https://www.who.int/data/data-collection-tools/who-mortality-database
'''
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def read (start, code, end, name):
    with open('Morticd7.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        prevyear = 0
        prevcause = " "
        deaths = 0
        large1 = 0
        large2 = 0
        large3 = 0
        large4 = 0
        cause1= ' '
        cause2= ' '
        cause3= ' '
        cause4 = ' '
        list1= ' '
        list2= ' '
        list3= ' '
        list4 = ' '
        first = [' ']*100
        fd = [' ']*100
        second = [' ']*100
        sd = [' ']*100
        third = [' ']*100
        td=[' ']*100
        pop = [0]*100
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if int(f'{row[0]}') == code :
                    year = int(f'{row[3]}')
                    cause = f'{row[5]}'
                    listx = f'{row[4]}'
                    if year != prevyear :
                        first[year - start] = cause2
                        second[year - start] = cause3
                        third[year - start] = cause4
                        fd[year - start] = large2
                        sd[year - start] = large3
                        td[year - start] = large4
                        large1 = 0
                        large2 = 0
                        large3 = 0
                        large4 = 0
                        
                    if cause != prevcause :
                        if deaths > large1:
                            large4 = large3
                            large3 = large2
                            large2 = large1
                            large1 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 = cause1
                            cause1 = prevcause
                            list4 = list3
                            list3 = list2
                            list2 = list1
                            list1 = prevlist
                        elif deaths > large2:
                            large4 = large3
                            large3 = large2
                            large2 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 =  prevcause
                            list4 = list3
                            list3 = list2
                            list2 =  prevlist
                        elif deaths > large3:
                            large4 = large3
                            large3 =  deaths
                            cause4 = cause3
                            cause3 =  prevcause
                            list4 = list3
                            list3 =  prevlist
                        elif deaths > large4:
                            large4 = deaths
                            cause4 =  prevcause
                            list4 =  prevlist
                            
                        deaths = int(f'{row[9]}')
                    else:
                        deaths = deaths + int(f'{row[9]}')

                    
                    prevcause = cause
                    prevyear = year
                    prevlist = listx
          
                    line_count += 1
    with open('Morticd8.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if int(f'{row[0]}') == code :
                    
                    year = int(f'{row[3]}')
                    cause = f'{row[5]}'
                    listx = f'{row[4]}'
                    if year != prevyear :
                        first[year - start] = cause2
                        second[year - start] = cause3
                        third[year - start] = cause4
                        fd[year - start] = large2
                        sd[year - start] = large3
                        td[year - start] = large4
                        large1 = 0
                        large2 = 0
                        large3 = 0
                        large4 = 0
                        
                    if cause != prevcause :
                        if deaths > large1:
                            large4 = large3
                            large3 = large2
                            large2 = large1
                            large1 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 = cause1
                            cause1 = prevcause
                            list4 = list3
                            list3 = list2
                            list2 = list1
                            list1 = prevlist
                        elif deaths > large2:
                            large4 = large3
                            large3 = large2
                            large2 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 =  prevcause
                            list4 = list3
                            list3 = list2
                            list2 =  prevlist
                        elif deaths > large3:
                            large4 = large3
                            large3 =  deaths
                            cause4 = cause3
                            cause3 =  prevcause
                            list4 = list3
                            list3 =  prevlist
                        elif deaths > large4:
                            large4 = deaths
                            cause4 =  prevcause
                            list4 =  prevlist
                            
                        deaths = int(f'{row[9]}')
                    else:
                        deaths = deaths + int(f'{row[9]}')

                    
                    prevcause = cause
                    prevyear = year
                    prevlist = listx
          
                    line_count += 1

    with open('Morticd9.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if int(f'{row[0]}') == code :
                    
                    year = int(f'{row[3]}')
                    cause = f'{row[5]}'
                    listx = f'{row[4]}'
                    if year != prevyear :
                        first[year - start] = cause2
                        second[year - start] = cause3
                        third[year - start] = cause4
                        fd[year - start] = large2
                        sd[year - start] = large3
                        td[year - start] = large4
                        large1 = 0
                        large2 = 0
                        large3 = 0
                        large4 = 0
                        
                    if cause != prevcause :
                        if deaths > large1:
                            large4 = large3
                            large3 = large2
                            large2 = large1
                            large1 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 = cause1
                            cause1 = prevcause
                            list4 = list3
                            list3 = list2
                            list2 = list1
                            list1 = prevlist
                        elif deaths > large2:
                            large4 = large3
                            large3 = large2
                            large2 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 =  prevcause
                            list4 = list3
                            list3 = list2
                            list2 =  prevlist
                        elif deaths > large3:
                            large4 = large3
                            large3 =  deaths
                            cause4 = cause3
                            cause3 =  prevcause
                            list4 = list3
                            list3 =  prevlist
                        elif deaths > large4:
                            large4 = deaths
                            cause4 =  prevcause
                            list4 =  prevlist
                            
                        deaths = int(f'{row[9]}')
                    else:
                        deaths = deaths + int(f'{row[9]}')

                    
                    prevcause = cause
                    prevyear = year
                    prevlist = listx
          
                    line_count += 1
    with open('Morticd10_part1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if int(f'{row[0]}') == code :
                    
                    year = int(f'{row[3]}')
                    cause = f'{row[5]}'
                    listx = f'{row[4]}'
                    if year != prevyear :
                        first[year - start] = cause2
                        second[year - start] = cause3
                        third[year - start] = cause4
                        fd[year - start] = large2
                        sd[year - start] = large3
                        td[year - start] = large4
                        large1 = 0
                        large2 = 0
                        large3 = 0
                        large4 = 0
                        
                    if cause != prevcause :
                        if deaths > large1:
                            large4 = large3
                            large3 = large2
                            large2 = large1
                            large1 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 = cause1
                            cause1 = prevcause
                            list4 = list3
                            list3 = list2
                            list2 = list1
                            list1 = prevlist
                        elif deaths > large2:
                            large4 = large3
                            large3 = large2
                            large2 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 =  prevcause
                            list4 = list3
                            list3 = list2
                            list2 =  prevlist
                        elif deaths > large3:
                            large4 = large3
                            large3 =  deaths
                            cause4 = cause3
                            cause3 =  prevcause
                            list4 = list3
                            list3 =  prevlist
                        elif deaths > large4:
                            large4 = deaths
                            cause4 =  prevcause
                            list4 =  prevlist
                            
                        deaths = int(f'{row[9]}')
                    else:
                        deaths = deaths + int(f'{row[9]}')

                    
                    prevcause = cause
                    prevyear = year
                    prevlist = listx
          
                    line_count += 1
    with open('Morticd10_part2.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if int(f'{row[0]}') == code :
                    
                    year = int(f'{row[3]}')
                    cause = f'{row[5]}'
                    listx = f'{row[4]}'
                    if year != prevyear :
                        first[year - start] = cause2
                        second[year - start] = cause3
                        third[year - start] = cause4
                        fd[year - start] = large2
                        sd[year - start] = large3
                        td[year - start] = large4
                        large1 = 0
                        large2 = 0
                        large3 = 0
                        large4 = 0
                        
                    if cause != prevcause :
                        if deaths > large1:
                            large4 = large3
                            large3 = large2
                            large2 = large1
                            large1 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 = cause1
                            cause1 = prevcause
                            list4 = list3
                            list3 = list2
                            list2 = list1
                            list1 = prevlist
                        elif deaths > large2:
                            large4 = large3
                            large3 = large2
                            large2 = deaths
                            cause4 = cause3
                            cause3 = cause2
                            cause2 =  prevcause
                            list4 = list3
                            list3 = list2
                            list2 =  prevlist
                        elif deaths > large3:
                            large4 = large3
                            large3 =  deaths
                            cause4 = cause3
                            cause3 =  prevcause
                            list4 = list3
                            list3 =  prevlist
                        elif deaths > large4:
                            large4 = deaths
                            cause4 =  prevcause
                            list4 =  prevlist
                            
                        deaths = int(f'{row[9]}')
                    else:
                        deaths = deaths + int(f'{row[9]}')

                    
                    prevcause = cause
                    prevyear = year
                    prevlist = listx
          
                    line_count += 1

    pop = {}
    with open('population_total.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        prevyear = 0
            
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if f'{row[0]}' == name :
                    #print('yeah')
                    for x in range(end - start+1):
                        pop[x] = int(f'{row[start-1800 + x+1]}'  )  
            line_count += 1
    print(pop)
    first[year - start+1] = cause2
    second[year - start+1] = cause3
    third[year - start+1] = cause4
    fd[year - start+1] = large2
    sd[year - start+1] = large3
    td[year - start+1] = large4
    

                    
    firstlabels = [" "]*(2016-start+1)
    fd1 =[0]*(2016-start+1)
    secondlabels = [" "]*(2016-start+1)
    sd1 =[0]*(2016-start+1)
    thirdlabels = [" "]*(2016-start+1)
    td1 =[0]*(2016-start+1)
    print(first)
    for x in range (end-start+1):
        if fd[x+1] == ' ' :
            firstlabels[x] = 'NA ' + str(x+start)
            fd1[x] = 0
            secondlabels[x] = 'NA ' + str(x+start)
            sd1[x] = 0
            thirdlabels[x] = 'NA ' + str(x+start)
            td1[x] = 0
        else:
            firstlabels[x] = first[x+1]+ ' ' + str(x+start)
            fd1[x] = float(fd[x+1])/pop[x] * 1000000
            secondlabels[x] = second[x+1] + ' ' + str(x+start)
            sd1[x] = float(sd[x+1])/pop[x] * 1000000
            thirdlabels[x] = third[x+1] + ' ' + str(x+start)
            td1[x] = float(td[x+1])/pop[x] * 1000000
        #print (firstlabels[x], fd1[x])
        
    y_pos = np.arange(len(firstlabels))    
    plt.bar(y_pos, fd1, align='center', alpha=0.5)
    plt.xticks(y_pos, firstlabels)
    plt.xticks(rotation=90)
    plt.xticks(fontsize=5)
    plt.ylabel('Deaths Per Million')
    plt.title('Showing leading cause of death '+'for ' + name)
    plt.show()

    y_pos = np.arange(len(secondlabels))    
    plt.bar(y_pos, sd1, align='center', alpha=0.5)
    plt.xticks(y_pos, secondlabels)
    plt.xticks(rotation=90)
    plt.xticks(fontsize=5)
    plt.ylabel('Deaths Per Million')
    plt.title('Showing the second leading cause of death '+'for ' + name)
    plt.show()

    y_pos = np.arange(len(thirdlabels))    
    plt.bar(y_pos, td1, align='center', alpha=0.5)
    plt.xticks(y_pos, thirdlabels)
    plt.xticks(rotation=90)
    plt.xticks(fontsize=5)
    plt.ylabel('Deaths Per Million')
    plt.title('Showing the third leading cause of death '+'for ' + name)
    plt.show()




read(1954, 4020, 2016, 'Belgium') #1 Belgium
read(1985, 4038, 2016, 'United Kingdom') #2 UK
read(1971, 4280, 2016, 'Spain') #3 Spain - skips years
read (1951, 4180, 2016, 'Italy') #4 Italy
read (1951, 4290, 2016, 'Sweden') #5 Sweden#
read(1950, 4080, 2016, 'France') #6 France only to 2014
read(1950, 2450, 2016, 'United States') #7 USA - only to 2007 for pop
read(1950, 4210, 2016, 'Netherlands') #8
read(1950, 4170, 2015, 'Ireland') #9 Ireland - only to 2015 skips years
read(1962, 2180, 2016, 'Ecuador') #10 Ecuador
read(1951, 4300, 2016, 'Switzerland') #11 Switzerland
read(1950, 2090, 2016, 'Canada') #12 Canada
read(1966, 2370, 2016, 'Peru') #13 Peru
read(1977, 2070, 2016, 'Brazil') #14 Brazil
read(1955, 2120, 2016, 'Chile') #15 Chile
read(1955, 4240, 2016, 'Portugal')#16 Portugal
read(1955, 2310, 2016, 'Mexico') #17 Mexico
read(1991, 4260, 2016, 'Moldova') #18 Moldova
read(1974, 3130, 2016, 'Iran')#19 Iran
read(1955, 2350, 2016, 'Panama') #20 Panama











