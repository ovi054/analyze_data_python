# This module processes the report requests given the command the user entered.
import temperature
def average(command):
    """
    Creates a report with a heading and a single line of output showing 
    the average, maximum, and minimum temperatures 
    for THE period specified in the command.
    """
    #format of print from instruction pdf
    print("{:>12} {:>5} {:>5} {:>5}".format('Period', 'Avg', 'Max', 'Min'))
    print("")
    #storing dataframe of temperature module to df
    df = temperature.dataframe
    query = command[8:] #ex: average Jan-2010 --> Jan-2010
    period = query
    if(command=='average'): #ex: average
        period = ''
        avg = df['Temperature'].mean() #finding avg of all temperature column
        maximum = df['Temperature'].max() #finding max of all temperature column
        minimum = df['Temperature'].min() #finding min of all temperature column

    elif(len(query)>=10): #ex: report? Jan-2010 or report? 21-Jan-2010
        if(query.startswith('0')): #if input: 01-Jan-2012
            query = query[1:] # formating 01-Jan-2012 to find exact value from df
        rslt_df = df.loc[df['Date']==query] #selecting and storing rows where Date is 'DD-MMM-YYYY' format
        #print(rslt_df.head())
        #print(rslt_df['Temperature'].describe())
        avg = rslt_df['Temperature'].mean() #finding avg of temperature column of selected rows
        maximum = rslt_df['Temperature'].max() #finding max of temperature column of selected rows
        minimum = rslt_df['Temperature'].min() ##finding min of temperature column of selected rows
        if(len(period)==10): #ex: if input: 1-Jan-2012
            period ='0'+period # adding '0' to make '01-Jan-2012' format
    else:
        rslt_df = df.loc[df['Date'].str.contains(query)] ##selecting rows where Date is 'MMM-YYYY' format
        #print(rslt_df.head())
        #print(rslt_df['Temperature'].describe())
        avg = rslt_df['Temperature'].mean() ##finding avg of temperature column of selected rows
        maximum = rslt_df['Temperature'].max() #finding min of temperature column of selected rows
        minimum = rslt_df['Temperature'].min() #finding max of temperature column of selected rows

    #printing period,avg,min,max values like instruction pdf format
    print("{:>12} {:>5.1f} {:>5.1f} {:>5.1f}".format(period, avg, maximum, minimum))
    print("")
    #return


def table(command):
    """
    Creates a report with a heading and a line of output showing 
    the average, maximum, and minimum temperatures 
    for EACH period within the period specfied in the command.
    """
    #format of print from instruction pdf
    print("{:>12} {:>5} {:>5} {:>5}".format('Period', 'Avg', 'Max', 'Min'))
    print("")
    df = temperature.dataframe
    query = command[6:]
    if(command=='table'): #ex: report? table
        year_list = [] #store unique year value of df (Ex: '2008','2009','2010' etc)
        start = df['Date'][0] 
        start = int(start[-4:]) ##1-Jan-2008 -->2008
        end = df['Date'][len(df)-1] 
        end = int(end[-4:]) ##31-Dec-2015 -->2015

        for i in range(start,end+1):
            year_list.append(str(i)) #ex:[2008,2009,----,2015]

        for i in range(len(year_list)):
            #rslt-df selects rows where Date contains that year: ex:if i=2010 then all DD-MM-2010 selceted
            rslt_df = df.loc[df['Date'].str.contains(year_list[i])]
            period = year_list[i]
            avg = rslt_df['Temperature'].mean() #finding avg of selected rows
            maximum = rslt_df['Temperature'].max() #finding max of selected rows
            minimum = rslt_df['Temperature'].min() ##finding min of selected rows
            #printing values
            print("{:>12} {:>5.1f} {:>5.1f} {:>5.1f}".format(period, avg, maximum, minimum))
    elif(len(query)>=8): # report : table MMM_YYYY
        #month_dict stores no. of date of a month
        month_dict = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,
        'Oct':31,'Nov':30,'Dec':31}
        month = query[0:3]
        #print(month)
        year = int(query[-4:])
        #print(year)
        #correcting no. of day for february for that input year: 28/29-leap-year
        if(month=='Feb'):
            if(year%400==0):
                month_dict['Feb']=29
            elif(year%4==0 and year%100!=0):
                month_dict['Feb']=29
        #print(month_dict)
        day_list = []
        val = month_dict[month]
        for i in range(1,val+1):
            period = str(i)+'-'+query #'DD-MM-YYYY'
            #rslt-df selects rows where Date is specific 'DD-MM-YYYY'
            rslt_df = df.loc[df['Date']==period]  
            avg = rslt_df['Temperature'].mean() #finding avg temp of selected rows
            maximum = rslt_df['Temperature'].max() #finding max temp of selected rows
            minimum = rslt_df['Temperature'].min() #finding min temp of selected rows
            if(len(period)==10):
                period = '0'+period #D-MM-YYYY -->DD-MM-YYYY
            print("{:>12} {:>5.1f} {:>5.1f} {:>5.1f}".format(period, avg, maximum, minimum))

    else: # report : table YYYY
        month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for i in range(len(month_list)):
            period = month_list[i]+'-'+query #MM-YYYY
            #rslt-df selects rows where Date contains specific 'MM-YYYY'
            rslt_df = df.loc[df['Date'].str.contains(period)]
            avg = rslt_df['Temperature'].mean() #finding avg temp of selected rows
            maximum = rslt_df['Temperature'].max() #finding max temp of selected rows
            minimum = rslt_df['Temperature'].min() ##finding min temp of selected rows
            print("{:>12} {:>5.1f} {:>5.1f} {:>5.1f}".format(period, avg, maximum, minimum))
    print("")






    #return

