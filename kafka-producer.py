from kafka import KafkaProducer

# Kafka broker and topic configurations
BROKER = 'localhost:9092'
TOPIC = 'votes'

def get_color_vote():
    # Replace this function with the logic to fetch data from your voting app
    # For demonstration purposes, we'll use a simple input prompt to get the color vote
    color = input('Enter your color vote (red, blue, green, yellow): ')
    return color.lower()

def main():
    # Create Kafka Producer instance
    producer = KafkaProducer(bootstrap_servers=BROKER)

    print('Kafka Producer started. Type "exit" to quit.')

    while True:
        color = get_color_vote()

        if color == 'exit':
            break

        # Send the color vote to Kafka topic
        producer.send(TOPIC, value=color.encode())

    # Close the producer
    producer.close()

if __name__ == '__main__':
    main()
