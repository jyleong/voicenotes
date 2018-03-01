# models.py
# created by James L 07/07/2017

# file for all our database related python objects, used for ORM

import model

class Messages(model.Model):
    messageContent = model.Column(type=model.Type.text)

