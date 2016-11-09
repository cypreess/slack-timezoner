import datetime
import json
import re
from collections import defaultdict

import pytz
from flask import Flask
from flask import abort
from flask import request

import settings

ver = 0.1
app = Flask(__name__)

user_timezones = defaultdict(lambda: settings.DEFAULT_TIMEZONE)
user_timezones.update(dict(settings.USER_TIMEZONES))
timezones = settings.SUPPORTED_TIMEZONES


def parse_text_time(text):
    matches = re.findall(r'(([1][0-9]|[2][0-3]|[0-9]):([0-5][0-9])(\s*(am|pm))?)|([1][0-2]|[0-9])(\s*(am|pm))', text,
                         re.I)
    result = []
    for m in matches:
        if m[1] != '':
            result.append((int(m[1]), int(m[2]), m[4].lower()))
        elif m[5] != '':
            result.append((int(m[5]), 0, m[7].lower()))
    return result


def convert_to_time(h, m, am_pm, timezone):
    if am_pm == 'pm':
        h += 12

    d = datetime.datetime.now(tz=pytz.timezone(timezone))
    d = d.replace(hour=h, minute=m, second=0, microsecond=0)

    return d


def process(text, timzeone, timezones):
    result = []
    for h, m, am_pm in parse_text_time(text):
        time = convert_to_time(h, m, am_pm, timzeone)

        sub_result = []
        for timezone, format in timezones:
            local = time.astimezone(pytz.timezone(timezone))
            sub_result.append((timezone, local.strftime(format)))

        result.append(('%s:%02d%s' % (h, m, am_pm), sub_result))
    return result


@app.route('/', methods=['GET'])
def home():
    return 'Timezoner v.%s for Slack' % ver


@app.route('/', methods=['POST'])
def convert():
    if settings.TOKEN is not None and request.form.get('token') != settings.TOKEN:
        print(request.form)
        print("BAD TOKEN")
        abort(403)

    if request.form.get('bot_id'):
        return ''

    user = request.form.get('user_name')
    user_timezone = user_timezones[user]

    response = ''

    for label, converstions in process(request.form.get('text'), user_timezone, timezones):
        response += '*%s (%s)*\n' % (label, user_timezone)
        for tz, text in converstions:
            response += ' • _{tz}:_ _{text}_\n'.format(tz=tz, text=text)

    response_json = {
        "text": response
    }

    return json.dumps(response_json)


if __name__ == '__main__':
    print("User timezones", user_timezones)
    print("Supported timezones", timezones)
    app.run(host='0.0.0.0', port=settings.PORT)
