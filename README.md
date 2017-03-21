# Use NUPIC to detect anomaly in employee movement in a Restricted Zone

data1.csv contains the emoplyee movement data and contains the employeed id, time of card swipe and whether the employee moved in or out.

Normal ML algorithms cannot be used to analyze spatial data. They fail to build corelations because of the ever increasing parameter of timestamp and also if looked at mathematically are incapable of identifying weekly, monthly, daily or any other spatial pattern.

To tackle this problem NUPIC uses its HTM algorithm. For each swipe an anomaly score of range 0-1 is generated and a threshold can be set depending upon the level of Restriction and an alarm can be raise in case an anomaly is detected.

Note - This example is inspired from hot gym example provided by NUPIC.
