from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Message:
    db='private_wall'
    def __init__(self, data):
        self.id = data['id']
        self.recipient_id = data['recipient_id']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = None
        
        
    