#! /usr/bin/python


import os



def print_test(alpha):
        f = open('colors')
        command = "set term pdfcairo enhanced round color size 5,50 font 'Source Sans Pro Bold';set samples 1000;set key lmargin;set xrange [0:10];unset xtics;set ytics scale 0 font ',16' textcolor rgb 'gray50';set border 0 lc rgb 'gray50' lw 2; set title ' Alpha = "+str(alpha)+"' font ',20'; unset key;"


        command += "set output 'colors-"+alpha+".pdf';"

        command_1tics = "set ytics ("
        command_2tics = "set y2tics ("

        for i,line in enumerate(f):
            c = line.split(' ')
            if len(c)<2: continue
            label,color_tmp = c[0],c[1]
            color = "#"+alpha+color_tmp[1:]
            #print label,color
            
            y = 3*i
            command_1tics += '"'+label+'" '+ str(y) + ','
            command_2tics += '"'+color+'" '+ str(y) + ','
            
            if i == 0:
                command += 'plot exp(-x/3)*sin(5*x)+'+str(y)+' lw 8 lc rgb "'+color+'" title "'+label+'"'
            else:
                command += ',exp(-x/3)*sin(5*x)+'+str(y)+' lw 8 lc rgb "'+color+'" title "'+label+'"'
        command_1tics = command_1tics[:-1]+');'
        command_2tics = command_2tics[:-1]+');'

        f.close()

        f = open('makeplot.gp','w')
        f.write(command_1tics)
        f.write(command_2tics)
        f.write(command)
        f.close()

        os.system('gnuplot makeplot.gp')


        #print command        

            



list_alpha = ['11','22','33','44','55','66','77','88','99','aa','bb','cc','dd','ee']
for alpha in list_alpha:
    print "Generating guide for alpha = " + alpha
    print_test(alpha)
