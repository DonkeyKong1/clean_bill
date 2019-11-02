# CleanSpark Python Developer Exercise

## Problem Description

### Energy and Power

At CleanSpark we analyze electricity bills every day. In general, an electricity
bill comprises two primary parts: energy charges and maximum-power (demand)
charges. In order to understand these two portions of the bill, we must first
understand the difference between energy and power.

One helpful analogy is between electricity comsumption and driving your car.
In order to understand this better, let's use a concrete example. Imagine
you want to drive from San Diego to San Franciso this weekend. After checking
Google Maps, you know that you need to travel roughly 500 miles.

Now, let's assume someone asked you how long it will take you to get to San
Francisco. What would you say? ... Hopefuly, you thought to yourself, "I don't
have enough information. I need to know how fast I am driving in order to
know how long it will take."

This is because time and distance require a speed (or rate) to convert between
the two. You may recall the familiar definition of a rate:

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_cm&space;{\rm&space;speed}&space;=&space;\frac{\rm&space;distance}{\rm&space;time}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\fn_cm&space;{\rm&space;speed}&space;=&space;\frac{\rm&space;distance}{\rm&space;time}" title="{\rm speed} = \frac{\rm distance}{\rm time}" /></a>

Now, assume I also told you that you will be traveling at an average speed of
60 mph over your 500 mile journey to San Francisco and then asked you how long
it would take. Using our definition of speed (rate) we can easily calculate the
time required to get to San Francisco:

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_cm&space;{\rm&space;time}&space;=&space;\frac{\rm&space;distance}{\rm&space;speed}&space;=&space;\frac{\rm&space;500&space;\,&space;miles}{\rm&space;60&space;\,&space;mph}&space;=&space;\rm{8.\bar{3}&space;\,&space;h}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\fn_cm&space;{\rm&space;time}&space;=&space;\frac{\rm&space;distance}{\rm&space;speed}&space;=&space;\frac{\rm&space;500&space;\,&space;miles}{\rm&space;60&space;\,&space;mph}&space;=&space;\rm{8.\bar{3}&space;\,&space;h}" title="{\rm time} = \frac{\rm distance}{\rm speed} = \frac{\rm 500 \, miles}{\rm 60 \, mph} = \rm{8.\bar{3} \, h}" /></a>

Extending the example above to electricity we can say that energy is to distance
what power is to speed.  However the units can be a bit tricky. Energy is
measured in kWh and power is measured in kW. In order to provide some more
context, let's assume a building consumed 50 kWh over a 30 minute period and I
asked you what the averave power was. Well extending our formula from above:

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_cm&space;{\rm&space;power}&space;=&space;\frac{\rm&space;energy}{\rm&space;time}&space;=&space;\frac{\rm&space;50&space;\,&space;kWh}{\rm&space;0.5&space;\,&space;h}&space;=&space;{\rm&space;100&space;\,&space;kW}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\fn_cm&space;{\rm&space;power}&space;=&space;\frac{\rm&space;energy}{\rm&space;time}&space;=&space;\frac{\rm&space;50&space;\,&space;kWh}{\rm&space;0.5&space;\,&space;h}&space;=&space;{\rm&space;100&space;\,&space;kW}" title="{\rm power} = \frac{\rm energy}{\rm time} = \frac{\rm 50 \, kWh}{\rm 0.5 \, h} = {\rm 100 \, kW}" /></a>

Now that you understand energy and power we can discuss how energy bills are
typically calculated.

### Electricity Bills

As mentioned before, energy bills have two primary components: energy and
max-power (demand). These two portions are calculated in completely different
ways. We will first discuss energy and then max-power (demand).

Energy rates have units of $/kWh and are calculated at every 15 minute interval.
For example, if the energy rate is $0.01/kWh and the building consumed 100 kWh
of energy over that 15 minute interval, they are charged $1.00. This occurs at
every 15 minute interval in the month and all of the charges get summed up.
This sum of energy charges is the energy portion of your bill.

> Note: This operation is very similar to a dot product.

Max-power (demand) rates have units of $/kW and are calculated only once
per month. For example, for an entire month of data let's assume the maximum
average power (demand) in a single interval was 100 kW and the demand rate
is $20/kW. The customer would be they are charged $2000 once for that month.

### Problem

You are given a month electricity consumption data (kWh) in 15 minute intervals for a commercial facility located in San Diego, CA. This data is provided in the data.xlsx file in this repository. Each interval is labeled with the time it began and all intervals are 15 minutes long. Your task is to write two methods: one that calculates the total energy (consumption) portion of the monthly bill and the other that calculates the demand portion of the monthly bill.

The pricing scheme (electricity tariff) you should use to calculate the bills is outlined below. Your functions will need to use the electricity consumption data and the pricing scheme to calculate the energy and demand charges.

### Energy Rates

Weekends: $0.05/kWh

Weekdays (12:00 am - 4:00 pm): $0.20/kWh

Weekdays (4:00 pm - 9:00 pm): $0.30/kWh

Weekdays (9:00 pm - 12:00 am): $0.10/kWh

### Demand Rates

Monthly max: $20/kW

## Assumptions/Constraints

- This solution must be written against Python 3.7.x
- Package management should be done through pipenv
- The pricing scheme should be stored in an in-memory (sqlite) SQLAlchemy database
- pyTest unit tests should be included

## Required Functionality

- Stage the pricing scheme in an in-memory (sqlite) SQLAlchemy database
- Retrieve pricing scheme from the in-memory (sqlite) database
- Load interval data from the supplied data.xlsx file
- Calculate the energy portion of the monthly bill
- Calculate the demand portion of the monthly bill
- Verify that the values are correct by writing appropriate unit tests
- Verify any additional or intermediate functionality with unit tests

## Evaluation Criteria

We are looking for concise and readable code that meets the component specifications and recommend PEP-8 and PEP-257 as guides.
Where the component specifications are ambiguous or lacking, we are looking for you to make a decision that allows you to move forward without compromising the basic functionality of the application. We are expecting this task to take you 1-3 hours; please do not spend more than 5 hours on this task.

## Submission

Once you have finished working on your exercise, either post your solution in a hosted repo and provide a link or compress the repository into a .zip file and send through Stack Overflow.
