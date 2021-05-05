# Weather Discord Bot

Hi, welcome to the weather bot! Our bot uses the Open Weather API to provide updates on weather data from around the world. Weather bot has six commands, three of which interact with the Open Weather API. The other three are there to help the user understand how to interact with the weather bot. Listed below are the six commands:

```
hi
help name-of-command
docs
weather
go_outside
sunset
```
## Help Commands
Each command should be prompted by the '$' prefix. For example, by typing '$hi' into discord, the user will be welcomed by the weather bot with a nice message. The command help ('$help') lists all of the help messages for each command. If you want instructions on how to use a specific command type '$help "name-of-command"'. The command called docs ('$docs') will give a summary of the functions and how to use them. 

## Weather Information Commands
All three commands interacting with the weather API require the user to input a zipcode and country. For example, typing '$weather 22904 us' will return the current temperature for the 22904 zipcode, which is in the Charlottesville, VA region. The go_outside command will return a message on whether or not the user should go outside depending on the current temperature. The sunset command returns the approximate time of the day's sunset. 

## Docker Container

Below is the link to our docker container for the discord weather bot: 

https://hub.docker.com/r/ebarton77/bot
