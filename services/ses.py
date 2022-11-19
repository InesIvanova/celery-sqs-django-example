import os
import boto3
import logging
import time
from typing import List

CHARSET = "UTF-8"


class SESService:
    def __init__(self):
        self.key = os.environ["AWS_KEY"]
        self.secret = os.environ["AWS_SECRET"]
        self.region = os.environ["SES_REGION"]
        self.client = boto3.client(
            "ses",
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret,
            region_name=self.region,
        )

    def send_email(self, subject: str, body: str, receivers: List[str]):
        if not isinstance(receivers, list):
            receivers = [receivers]
        logging.info(
            f"Sending email to {' '.join(receivers)}. Title: {subject}. Body - '{body}'"
        )
        resp = self.client.send_email(
            Source="ines.iv.ivanova@gmail.com",
            Destination={"ToAddresses": receivers,},
            Message={
                "Subject": {"Data": subject, "Charset": CHARSET},
                "Body": {"Text": {"Data": body, "Charset": CHARSET},},
            },
        )
        logging.info(f"Email sent. Repsonse {resp}")