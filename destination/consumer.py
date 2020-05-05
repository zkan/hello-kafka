import os
import sys

import django

from confluent_kafka import Consumer


c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
})

c.subscribe(['mytopic'])

# Add the project to sys.path, so that Python can find packages
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), 'myapp')
sys.path.append(PROJECT_ROOT)

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()


from text_messages.models import TextMessage


number_of_message = TextMessage.objects.count()
print(number_of_message)

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue

    print(f'Received message: {msg.value().decode("utf-8")}')

    TextMessage.objects.create(message=msg.value().decode('utf-8'))

c.close()
