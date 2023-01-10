# Bill Automation

## Overview

This is a project which will be used to help people who are not capable of paying their bills online easily due to their limited understanding of the web.

In order to achieve this, the project will aggregate the prices of each bill from various sites using selenium. If all bills have values in them, it will then proceed to send a sms message via twilio to the user stating the price of the bill for each various sites, and to reply "Yes" or "No" to pay them.

Once a user message is received, if they sent a yes, then the bills will be paid. If no it will not get paid and remind the user the next day.

Build the docker image and run using:
```
docker build -t receivemsgserver .
docker run -d -p 8000:5000 <IMAGEID>
```
