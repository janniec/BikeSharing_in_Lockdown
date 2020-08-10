# Bicycle-Sharing in the Pandemic Lockdown.
How data from the first lockdown can prepare Divvy for the second one. 

<img src="https://github.com/janniec/RideSharing_in_Lockdown/blob/master/images/JE2LC456Q5AQ3AQNV6MLOVJHPI.jpg" alt="Dimensions" align="middle" height=400px>  
(image source: [Chicago Tribune](https://www.chicagotribune.com/business/transportation/ct-biz-divvy-cta-petition-looting-lightfoot-20200602-m74qyesnoned5ln2e6mf4k3csm-story.html))

### Introduction

Like fellow city-dwellers during the Coronavirus Pandemic, I have been avoiding public transportation. (Remember to wear masks, avoid crowds, and wash your hands!). In the City of Chicago, this means I rely more and more on Divvy, Chicago's bicycle-sharing program, to supply me with bicycles as my main means of transporation throughout the city. My limited but comfortable lifestyle depends on the continued viability of Divvy, the abundance of their bicycles, and Divvy's support in making bicycles available where demand is highest. 

On July 15, Mayor Lori Lightfoot of Chicago warned that the City would go back into lockdown if COVID-19 cases continued to rise. As cases surge across the United States, a second lockdown in Chicago is looking more imminent. Fortunately, Divvy has data from the first lockdown to help answer some questions in preparation for the second one. 

<img src="https://github.com/janniec/RideSharing_in_Lockdown/blob/master/images/LIGHTFOOT_071620_8.0.jpg" alt="Dimensions" align="middle" height=400px>  
(image source: [Chicago Sun Times](https://chicago.suntimes.com/city-hall/2020/7/15/21325689/coronavirus-young-people-positive-tests-chicago-reopening-rollback-lightfoot))

Focusing on the following significant events related to Chicago's (first) Lockdown and Reopening:
  * March 9, 2020 - Governor J. B. Pritzker announced a disaster proclamation (a state of emergency) for the state of Illinois.
  * March 20, 2020 - Governor Pritzker announced a statewide stay-at-home order starting on March 21.
  * March 26, 2020 - the City of Chicago closed parks and the lakefront due to too many people gathering.
  * March 31, 2020 - Governor Pritzker extended the statewide stay-at-home order.
  * April 12, 2020 - Easter Sunday
  * April 17, 2020 - Governor Prizker announced that all schools in the state will stay closed for the remainder of the school year.
  * April 23, 2020 - Governor Pritzker extended the statewide stay-at-home order again with stricter modifications.
  * May 1, 2020 - Governor Pritzker unveiled a five-phase plan for reopening the state and Illinois entered Phase 2 reopening.
  * May 8, 2020 - Mayor Lightfoot announced Chicago's separate reopening guidelines and schedule.
  * May 25, 2020 -  Memorial Day
  * May 29, 2020 - Protesters, demonstrators, and rioters started to gather around the Loop, Chicago's downtown.
  * June 3, 2020 -  Chicago entered Phase 3 of Reopening
  * June 26, 2020 - Illinois entered into Phase 4, allowing for larger gatherings and the re-opening of restaurants and bars under social distancing and mask-wearing guidelines.

(More information about [Divvy](https://en.wikipedia.org/wiki/Divvy), the [lockdown and reopening](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Illinois#City_of_Chicago), and the [protests](https://en.wikipedia.org/wiki/George_Floyd_protests_in_Chicago) can be found here.)

I used Divvy's [publically available ](https://www.divvybikes.com/system-data) 2020 data, which tracked over 1 million bicycle rentals during the first 6 months of 2020.  Each bicycle rental has the following:
  * a unique "ride_id", 
  * rental date and time
  * return date and time
  * rental station id and name
  * return station id and name 
  * their latitudes and logitudes
  * rider type - whether the rider's account was a "member" or "casual". 
I analyzed trends across the weeks of 2020 from January to June, focusing on the weeks of the dates above. Through this exercise, we were able to gain some valuable insights to prepare Divvy for the second lockdown.


## Part 1: Has Rides Moved Away from the Loop and the Lakefront?

Chicago was always a premier recreational cycling destintation for generations, with public parks, lakefront paths, and trails throughout the city. Since June of 2013, with the launch of Divvy, cycling has been a growing means of transportation througout the entire city. (In fact, in terms of area covered, Divvy is the largest bike share system in North America.) 

Before the pandemic, Divvy bicycles were regulary found around the Loop, Chicago's downtown and central business district, and along Chicago's Lakefront Trail, a 18.5 mile path stretching all along Chicago's eastern border to Lake Michigan. The Lakefront Trail connects Chicago's four major lakefront parks and various beaches. As a result, Divvy's network of bicycle rental stations are more densely situated around the Loop and key attractions along the Lakefront, as you can see on their [system map](https://member.divvybikes.com/map/). 

During the Lockdown, all but essential workers were ordered to work from home by the Governor's stay-at-home order and all parks and the Lakefront trail were closed. However, for the same reasons these locations attracted Divvy, they also attract residences. These popular neighborhoods still had locals who most likely needed modes of transporation apart from the public transporation, discouraged during the Lockdown. So I wanted to know if despite the the population still living around the Loop and the Lakefront, did Divvy rides move away from these former central hubs? 

<img src="https://github.com/janniec/RideSharing_in_Lockdown/blob/master/images/median_end_dist_from_loop_by_week.png" alt="Dimensions" align="middle" height=400px>  
To answer this question, I found the distance between the bicycle return/ destination and our points of interest.  I then aggregated the distances by weeks, and then plotted the medians by week, as marked by the Monday date of each week. As you can see, before the Governor issued the disaster proclamation, Illinois' version of state of emergency, the median distance hovered around 1.25 miles, meaning that half of Divvy's many bicycle rides ended close to a mile or less from the Loop. After the Lockdown began, when the Gonvernor announced the stay-at-home order, the median distance moved to more than 2.5 miles from the Loop. When the Governor extneded that order, the median moved closer to 3 miles. When the protests and riots began after Memorial Day, the median moved even farther way from the Loop. Interestingly, even with Illionis entering Phases 2, 3, and 4, Divvy rides appear to largely stay away from the Loop. 

<img src="https://github.com/janniec/RideSharing_in_Lockdown/blob/master/images/median_end_dist_from_lakefront_by_week.png" alt="Dimensions" align="middle" height=400px> 
For distance from the Lakefront, I only measured the difference in longitude, the east-west positions of the ride destinations from the Lakefront, regardless of how far north or south the ride took place. Before the Lockdown, the median distance from the Lakefront was almost consistenly around 1.55 miles. This median made sense because of the week day traffic in the Loop.  I had aggregated the data by week, including weekdays.  Whereas, the Lakefront largely drew crowds on the weekends. In addition, the 2 major train stations that fed commuters into the Loop, are both about 1.5 miles from the Lakefront. When the Governor announced the disaster proclamation, there was little very little change in the median. However, the median began to move away from the Lakefront with the stay-at-home order and the closure of the lakefronts.  Unlike the median distance from the Loop, the median distance from the Lakefront shrank with the Reopening. Apart from the spike in the median due to the protests and the riots, Divvy rides has been moving back to the Lakefront. 

Divvy rides and returns have been moving away from these central hubs. Given that traffic has not returned to the Loop yet and a second lockdown would keep traffic out for longer, Divvy should consider moving some fo the densly situated rental stations out of the Loop and into more residential neighborhoods. As for the Lakefront, Divvy rides appear to avoid the parks and trails only during Lockdown, only to return during reopening. Divvy should leave the Lakefront rental stations as they are. However, Divvy should consider ferrying the bicycles themselves away from the Lakefront druing the second Lockdown to meet the temporary demands of the bicycles elsewhere.


## Part 2: Was Demand for Bicycles Higher or Lower During the Lockdown?

With bicycle rentals moving away from the most active parts of the city, I wondered if demand for Divvy bicycles had decreased during the Lockdown. To answer this question, I looked at 2 metrics - the count of rides by week the average duration of those rides by week. 

<img src="https://github.com/janniec/RideSharing_in_Lockdown/blob/master/images/count_ride_id_by_week.png" alt="Dimensions" align="middle" height=400px>  
Before the Lockdown, the count of rodes swung wildy between 20,000 to 55,000, probably due to fluctuations in weather. However The Governor's disaster proclamation & stay-at-home lead to a clear dip in the total number of rides. For the msot part, the count stayed down until Illinois entered Phase 2 of Reopening. With the reopening, the count of rides has again swung wildy, probably due to fluctuations weather. But there is a clear rise in the count of rides per week. At June, the rides are nearly 4 times higher than the count at the beginning of the Lockdown. This degree of increase is suprising given the severe summer humidity and lack of any events to draw any traffic. I can only assume this level of popularity is due to the Reopening.

<img src="https://github.com/janniec/RideSharing_in_Lockdown/blob/master/images/mean_duration_minutes_by_week.png" alt="Dimensions" align="middle" height=400px>  
While the count of rides took an initial hit with the Lockdown, the same cannot be said with the duration of these rides. The Lockdown seems to have had an inverse impact on duration. Those rides increased quite a bit and continued to increase throughout the Lockdown. This increase makes sense because while most of Chicago stayed at home, those who had to go out probably chose to go the extra distance with a Divvy bicycle to avoid public transit. With the reopening, the average duration is about double the duration of the rides before the Lockdown.

Looking at these visualizations together, it would appear that demand for Divvy bicycles did go down but not as much as I would have thought becuase of how much duration of those rides increased. However, the Reopening gave the demand for Divvy bicycles a huge boost. The count of rides quadrupled while the duration has continued to increase. 

The flipside of demand is unavailability. Unfortunately, Divvy does not share that total number of bicycles in the program nor the ids of the bicycles for each trip to track bicycle conditions. So it would be hard to say how many bicycles are out of commisions or if there was a bicycle shortage during the Reopening. But Divvy may want to consider adding more bicycles to the program to meet the boost in demand for when the City reopens after the second Lockdown. 


## Part 3: Did Revenue Increased or Decreased during the Lockdown?

Finally and more importantly, how is Divvy doing? With [the news](https://www.chicagotribune.com/coronavirus/ct-coronavirus-chicago-business-closures-yelp-20200722-nmhvpmv72fdyzdjgvzoun7rima-story.html) reporting that as of July 2020, over 4,000 Chicago businesses have closed during the pandemic and more than half of them will never reopen, there's genuine concern for any buisness struggling during the Lockdown.

Obviously, we don't have any information into Divvy's costs or profits to gauge if Divvy is struggling. But we can look at our data for a general upward or downward trend in revenue from 'casual' and 'member' rides. 

Divvy technically has 3 tiers of riders. 
- The "Casual" rider pays \$3.00 for every 30 minutes of rental.   
- The "Day Pass" rider pays \\$15 for 3 hours worth of riding within 24 hours. After 3 hours, the "Day Pass" rider pays \\$3.00 for every 30 minutes.   
- The "Member" rider pays \\$99 for an annual membership. Included in the membership are unlimited rental under 45 mins. The "Member" rider pays \\$3.00 for ever 30 mins of rental beyond the first 45 mins.   

Unfortunately, we cannot calculate a full picture of Divvy's revenue from the data. In the 2020 data, the "Day Pass" rider is not a class under the "member_casual" category. Without rider IDs, we have no way of tracking subsequent rentals by the same rider. As such we must assume that all rides marked as "casual" were taken by "Casual" riders. In addition, the data does not include member_ids or any other identifying information. So we cannot track new members or incorporate membership fees into our revenue analysis. Instead, we are merely looking at the growth and shrinking of just revenue from "casual" and "member" rides only.

Please note that in August 2020 Divvy changed their pricing.

<img src="https://github.com/janniec/RideSharing_in_Lockdown/blob/master/images/sum_revenue_by_week.png" alt="Dimensions" align="middle" height=400px>  
Looking at the sum of revenue by week, there is a clear dip in the month of March, when the lockdown first started. But even after the Governor announces the stay-at-home order, revenue still increased slighlty, probably due to the longer durations of the rides. Once the State began talking about reopening, the revenue appears to have gotten back on track. There ar 2 noticeable dips in May and June.  The first dip appears be due to the beginning of the summer heat and humidity. The second dip appears to be due to the protests and riots. But overall, the effects on the Lockdown on revenue appears to be temporary. As long as Divvy prepares for another dip at the onset of a second lockdown, it should stay viable to see a comeback with the reopening. 


### Conclusion

In this article, we looked at Divvy's bicycle rental data to through the first half of 2020 to see how Chicago residents were riding and how Divvy was fairing during the Pandemic Lockdown and Reopening. 

1. We learned that Divvy rides had moved away from Chicago hotspots, the Loop and the Lakefront. While traffic appears to have returned to the Lakefront with the reopening, that has not been the case with the Loop. This observation indicated that Divvy could benefit from moving bicycles away from these former hotspots during a second Lockdown. 

2. We then looked at demand for Divvy's bicycles as quantified by the number of rides and the average duration of those rides. The number of rides dipped during the Lockdown but quickly rose during the Reopening. In contrast, the duration showed an overall upward trend throughout the year. Combined, this trend indicated an almost overcompensation in demand occurred during the reopening in response to the Lockdown. Divvy might want to consider adding more bicycles to its program to meet the demands of the reopening after a second lockdown.

3. Finally, we observed that the revenue Divvy generated from 'casual' and 'member' rides had taken a hit at the onset of the Lockdown but did not stay down. The effect of lockdowns like the first one should at most to be temporary and Divvy should be largely remain viable throughout these turbulent times. 

I should note that the findings here were observational. So the real question remains: 

#           How will Divvy do in the Second Lockdown?

To see more about this analysis, please check out my [Github](https://github.com/janniec/RideSharing_in_Lockdown/blob/master/README.md).