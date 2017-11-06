# Hectic Hurricanes - HackK-State-2017

## Getting Started
Once, we had decided that we wanted to go for the Hurricane Track, our first big challenge was collecting the data that we would use. This was challenging because there are a lot of datasets that we could use, but many didn't quite fit our needs. We eventually found fairly detailed Hurricane data reaching back to 1851.

## What it does
Once we decided on a dataset, we needed to figure out exactly kind of interpretations we wanted to make from the data. Since we had all of this data over time, it would make sense to try to predict future years based on historical data.

## How we built it
After some research, we decided to use an Auto-Regression model. When we were testing this model, we made sure to only train on two-thirds of the data and save the rest for testing. Our tests were reasonably successful so we decided to use this as our final model.

## Challenges we ran into
1. Finding data
2. Working with AWS
3. Using the google maps web API

## Accomplishments that we're proud of
1. Geeting reasonable results from our data model
2. Using the google maps web API to get latitude and longitude locations from human-readable addresses.

