import pandas as pd
from math import ceil
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def plot_pivot(df, value, aggfunc, y_label):
    '''
    df [dataframe] = Divvy dataframe, must have contain at least 'start_week' column
    value [string] = column name of the values we want to aggregate
    aggfunc [string] = how we want to aggregate the value, i.e. 'count', 'mean', 'mode', 'sum' etc. 
    y_label [string] = descriptive label for the y axis and the title of the plot
    Function to create a pivot table from a Divvy dataframe, plot an aggregation, and save a visualization.
    pivot_df [dataframe] = the pivot table grouping 'start_week' and aggregating the value
    '''
    # create a pivot table grouping by 'start_week'
    # applying the aggfunc, like "sum", to our designated value such as "duration"
    pivot_df = df.pivot_table(index='start_week', values=value, aggfunc=aggfunc)
    
    # plot the pivot table
    ax = pivot_df.plot(figsize=(15,9), grid=True, title=y_label+' by Week')
    
    # 'start_week' is a numerical index for each week in a year ranging from 1 to 52, and the ticks mark every 5th week
    # so I am adding fixed labels to replace the week index ticks with the Monday dates of each week. 
    ax.set_xticklabels(['0', ' 2019-12-29', ' 2020-01-27', \
                        ' 2020-03-02', ' 2020-04-06', ' 2020-05-11', \
                        ' 2020-06-15'], rotation=90)
    # labels the axis
    ax.set_ylabel(y_label)
    ax.set_xlabel("Weeks of ...")
    
    # we will be adding significant dates related to the lockdown and reopening in Chicago to our visualization
    chicago_dates=[{'date': '2020-03-09', 'label': 'Governor issues disaster proclamation'}, 
                   {'date': '2020-03-20', 'label': 'Governor announces stay-at-home order'}, 
                   {'date': '2020-03-26', 'label': 'Mayor closes parks & lakefront'}, 
                   {'date': '2020-03-31', 'label': 'Governor extends stay-at-home order'}, 
                   {'date': '2020-04-12', 'label': 'Easter Sunday'},
                   {'date': '2020-04-17', 'label': 'Governor closes schools for rest of school year'},
                   {'date': '2020-04-23', 'label': 'Governor extends stay-at-home order again'}, 
                   {'date': '2020-05-01', 'label': 'IL enters Phase 2 of Reopening'},
                   {'date': '2020-05-08', 'label': 'Mayor announces Chicagos reopening guidelines'}, 
                   {'date': '2020-05-25', 'label': 'Memorial Day and the George Floyd protests start'},
                   {'date': '2020-06-03', 'label': 'Chicago enters Phase 3 of Reopening'}, 
                   {'date': '2020-06-26', 'label': 'Chicago enters Phase 4 of Reopening'}]
    
    value_min = 0
    value_max = ceil(pivot_df[value].max())
    value_center = value_max/2
     
    # each date will be marked by a vertical red line    
    plt.vlines(x=[pd.to_datetime(event['date']).week for event in chicago_dates], \
               ymin=value_min, ymax=value_max, color = 'r')
    # Each vertical red line will be labeled with a description from the chicago_dates dictionary
    for event in chicago_dates:
        plt.text(pd.to_datetime(event['date']).week+.25, value_center, event['label'], \
                 rotation=90, verticalalignment='center', backgroundcolor='white')
    
    # save the visualization as a png file
    plt.savefig('images/'+aggfunc+'_'+value+'_'+"by_week.png")    
    plt.show()
    
    return pivot_df