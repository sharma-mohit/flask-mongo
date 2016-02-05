#!/usr/bin/env python:
import datetime
from flask import jsonify

def put_record():
    data = jsonify('{"date": "2015-05-12T14:36:00.451765", "uid": "1", "name": "John Doe", "md5checksum": "e8c83e232b64ce94fdd0e4539ad0d44f"}')
    VALID_FIELDS = ['uid', 'name', 'date', 'md5checksum']
    for field in VALID_FIELDS:
        if field not in data:
            return jsonify({
                'response': 'Error. {0} field is missing'.format(field)
            })
    try:
        date = datetime.datetime.strptime(data.get('date'),
                                          "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return jsonify({
                'response': 'Error. Invalid date format. Date should be given'
                ' in a %%Y-%%m-%%dT%%H:%%M:%%S.%%f format'
            })
    r = Record(
        uid=data.get('uid'),
        name=data.get('name'),
        date=date,
        md5checksum=data.get('md5checksum')
    )
    if not r.check_md5():
        return jsonify({'response': "Error. Checksum doesn't match"})
    uidRecord = Record.objects(uid=r.uid).first()
    nameRecord = Record.objects(name=r.name).first()
    if uidRecord and r.name != uidRecord.name:
        return jsonify({'response': "Error. name - uid missmatch"})
    if nameRecord and r.uid != nameRecord.uid:
        return jsonify({'response': "Error. name - uid missmatch"})
    r.save()
    return jsonify({'response': 'record successfuly added'})

put_record()
