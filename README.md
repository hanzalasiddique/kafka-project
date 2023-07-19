# kafka-project
# Voting App with Kafka Microservices

## Description
This project is a simple Voting App built using Python and Apache Kafka.
It consists of two microservices: a producer microservice that sends color votes to a Kafka topic, and a consumer microservice that consumes color votes from the Kafka topic.
The app allows users to vote for their favorite color among four options: red, blue, green, and yellow.

## Features
- A web-based Voting App with a simple user interface.
- Kafka-based microservices architecture for data ingestion and processing.
- Real-time color voting and data streaming using Kafka topics.
- Option to run both producer and consumer microservices locally or on separate machines.

## Setup and Configuration
1. Clone this repository to your local machine.

2. Install the required dependencies using `pip`:
   ```bash
   pip install kafka-python
