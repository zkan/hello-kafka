import os
import sys

import django


# Add the project to sys.path, so that Python can find packages
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), 'myapp')
sys.path.append(PROJECT_ROOT)

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()


from text_messages.models import TextMessage


number_of_message = TextMessage.objects.count()
print(number_of_message)

# Write your Kafka consumer here
# ...

