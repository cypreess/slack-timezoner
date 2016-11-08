# slack-timezoner
Simple bot to convert hours mentions in slack channels into specified timezones

## Provisioning

User heroku dyno to provision this repository. Then create outgoing-webhook in your slack account. Bind it to some channel and copy the token.

## Configuration

 * `TOKEN` - Slack's outgoing webhook token
 * `DEFAULT_TIMEZONE` - define the default timezone that will be recognized when no custom timezone is given, e.g. `US/Pacific`
 * `USER_TIMEZONES` - define specific timezone for specific user; format `user1,tz_name1;user2,tz_name2;..`
 * `SUPPORTED_TIMEZONES` - configuration of what timezones are going to be actually printed out after a time will be detected. Format is `tz_name1,strftime format1;tz_name2, strftime format2;...`, e.g.: `Europe/Warsaw,%a (%b %d) %H:%M [%Z%z];US/Pacific,%a (%b %d) %I:%M %p [%Z%z]`

## Real life example

![Slack Timezoner](https://s3-us-west-2.amazonaws.com/matterhorn-pro-uploads/statics/timezoner.png)

Only limited formats are now supported:
 
 * h:mm (17:30)
 * h:mm am. h:mm pm (2:30 am)
 * h pm, h am (1 am, 12pm)


## To-do

  * Parsing whole dates like tomorrow at 2pm, etc..
  * Possibly there is a bug with parsing 0pm, 0am 
