import os

PORT = os.environ.get('PORT', 8080)
TOKEN = os.environ.get('TOKEN')

# Timezones should be defined as: nick1,timezone1;nick2,timezone2
USER_TIMEZONES = [x.split(',') for x in os.environ.get('USER_TIMEZONES', '').split(';')]
DEFAULT_TIMEZONE = os.environ.get('DEFAULT_TIMEZONE', 'US/Pacific')

# Supported timezones are given as timezone name and strftime format
# TIMEZONES=Europe/Warsaw,%a (%b %d) %H:%M [%Z%z];US/Pacific,%a (%b %d) %I:%M %p [%Z%z]
SUPPORTED_TIMEZONES = [x.split(',') for x in os.environ.get('SUPPORTED_TIMEZONES', '').split(';')]

