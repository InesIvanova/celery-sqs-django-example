import datetime
import os
from typing import Optional, Dict, Any

import boto3



class SQSService:
    def __init__(self):
        self.key = os.environ["AWS_KEY"]
        self.secret = os.environ["AWS_SECRET"]
        self.region = os.environ["SES_REGION"]

        self.queue_url = os.environ["SQS_URL"]

        self.sqs = boto3.client(
            "sqs",
            region_name=self.region,
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret,
        )

    def send_message(
        self, message_body: str, message_attributes: Optional[Dict[str, Any]] = None
    ):

        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageAttributes=message_attributes,
            MessageBody=message_body,
            MessageGroupId=str(datetime.datetime.utcnow().timestamp()),
            MessageDeduplicationId=str(datetime.datetime.utcnow().timestamp())
        )

