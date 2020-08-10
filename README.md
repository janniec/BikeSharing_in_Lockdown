# Divvy in the Pandemic Lockdown

For this project, I was interested better understand the experience of Divvy, Chicago's bicycle-sharing program, during the Pandemic Lockdown and Reopening of 2020. Specifically I wanted to answer:
1. Was demand for bicycles higher or lower during the Lockdown?
2. Has trips moved away from the Loop and the Lakefront?
3. Did revenue increased or decreased during the Lockdown?


## Data

Data for this project came from [Divvy](https://www.divvybikes.com/system-data). I used the following files related to bicycle rentals from January to June of 2020. 
  * 202004-divvy-tripdata.zip
  * 202005-divvy-tripdata.zip
  * 202006-divvy-tripdata.zip
  * Divvy_Stations_Trips_2013.zip

Each rental is anonymized and includes: 
  * ride id
  * time of rental
  * time of return
  * rental station name
  * return station name
  * latitude & longitude of rental
  * latitude & longitude of return
  * whether the account of rental was "member" or "casual"
  
  
## Installation

The libraries required for this code are listed in 'requirements.txt'. In order to install all the libraries: `pip3 install -r requirements.txt`.


## File Descriptions

2 md files 
  * README.md - information about this repository.
  * blogpost.md - blogpost about the findings from analysis in this repository.

4 ipynb files - notebooks that answer the questions mentioned above.
  * Data_Prep_and_Clean.ipynb - notebook that loads, prepares, and cleans the data, and saves the dataframe.
  * Did_Revenue_Increase_or_Decrease_during_the_Lockdown.ipynb
  * Has_Rides_Moved_Away_from_the_Loop_and_Lakefront_During_the_Lockdown.ipynb
  * Was_Demand_for_Bicycles_Higher_or_Lower_During_the_Lockdown.ipynb
  
2 py modules
  * haversine_forumla.py - module containing function to calculate distance in miles between 2 latitude and longitude points.
  * visualize_plots.py - module containing function to visualize pivot plots and save them as pngs.
  
5 png files in the 'images' directory - images of the visualizations created by the code. 
  * count_ride_id_by_week.png
  * mean_duration_minutes_by_week.png
  * median_end_dist_from_lakefront_by_week.png
  * median_end_dist_from_loop_by_week.png
  * sum_revenue_by_week.png


## Results

The findings from the code in this repository can be found in the [blog post](https://github.com/janniec/RideSharing_in_Lockdown/blob/master/blogpost.md).


## Next Steps

Given the cyclical nature of outdoor activity and weather in Chicago, this data would be appropriate for a time series analysis.
