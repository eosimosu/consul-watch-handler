#!/usr/bin/env python

import httplib
import json
import sys

SLACK_HOST = ''
SLACK_PATH = ''
APP_ENVIRONMENT = ''
HEADERS = {'Content-Type': 'application/json'}
SLACK_CHANNEL = 'consul-alerts'
COLORS = {'warning': 'warning', 'critical': 'danger', 'passing': 'good'}


def construct_payload(check):
    return {
        'channel': SLACK_CHANNEL,
        'username':  APP_ENVIRONMENT,
        'icon_emoji': ':microscope:',
        'attachments': [{
            'fallback': 'Consul alert - Service: ' + check['ServiceName'] + ', Check: ' + check['Name'] + ', Status: ' +
                        check[
                            'Status'] + '.',
            'color': COLORS[check['Status']],
            'text': 'Consul alert -',
            'fields': [
                {
                    'title': 'Service',
                    'value': check['ServiceName'],
                    'short': True
                },
                {
                    'title': 'Check',
                    'value': check['Name'],
                    'short': True
                },
                {
                    'title': 'Node',
                    'value': check['Node'],
                    'short': True
                },
                {
                    'title': 'Status',
                    'value': check['Status'],
                    'short': True
                }
            ]
        }]
    }


def alert_slack(payload):
    conn = httplib.HTTPSConnection(SLACK_HOST)
    conn.request('POST', SLACK_PATH, json.dumps(payload), HEADERS)
    response = conn.getresponse()
    conn.close()
    return response


def main():
    checks = json.loads(sys.stdin.readlines()[0])
    for check in checks:
        payload = construct_payload(check)
        response = alert_slack(payload)
        print response.status, response.reason


if __name__ == "__main__":
    main()
