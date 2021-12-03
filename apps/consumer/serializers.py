from apps.consumer.models import Consumer
from common.database.serializer import ModelSerializer


class ConsumerModelSerializer(ModelSerializer):
    
    class Meta:
        title = "consumer"
        model = Consumer