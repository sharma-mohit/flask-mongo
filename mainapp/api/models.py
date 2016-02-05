import datetime
import hashlib
import json
from mainapp import db
from collections import OrderedDict

# Same reason for UID to be string here also as in views.py
class Record(db.Document):
    uid = db.StringField(required=True)
    name = db.StringField(max_length=255, required=True)
    #date = db.DateTimeField(default=datetime.datetime.now, required=True)
    date = db.DateTimeField(required=True)
    md5checksum = db.StringField(max_length=50, required=True)

    def check_md5(self):
        jstring = json.dumps(OrderedDict([
            ('date', self.date.strftime("%Y-%m-%dT%H:%M:%S.%f")),
            ('uid', self.uid),
            ('name', self.name)
        ]))
        md5 = hashlib.md5(jstring).hexdigest()
        print "Correct md5 checksum for string {js} is {md5}".format(
            md5=md5,
            js=jstring)
        return md5 == self.md5checksum.lower()
