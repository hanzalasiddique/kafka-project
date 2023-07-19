from kafka import KafkaConsumer

# Kafka broker and topic configurations
BROKER = 'localhost:9092'
TOPIC = 'votes'

def main():
    # Connect to Kafka broker
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=[BROKER],
        group_id='votes_consumer_group',
        auto_offset_reset='earliest',
    )

    print('Kafka Consumer started. Press Ctrl+C to quit.')

    try:
        for message in consumer:
            color = message.value.decode()
            print(f'Received color vote: {color}')

    except KeyboardInterrupt:
        pass
    finally:
        # Close the Kafka consumer
        consumer.close()

if __name__ == '__main__':
    main()
