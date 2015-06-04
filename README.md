# QotdToSms
## Description

A (simple) script to send a Quote of The Day via SMS using the French mobile operator "Free Mobile" sms notification option.

It means this can only work if you have a suscribed one of the two plans available at http://mobile.free.fr

That being said, if you're one of the greedy french people who chose to use the *young* and *not very mature*, but **promising**, Free Mobile network, then you'll be able to activate the sms notifications through the web console (once authenticated on http://mobile.free.fr).

Once the option is activated, you'll need to retrieve the credentials on the option page that will be used in the script. These credentials will have you authenticated on Free Mobile servers (basically, the result will be that you'll get the Quote of The Day on your mobile phone from your phone number).

## Installation

This script works on any unix-like system, as long as bash, curl and fortunes are available.

For Debian or derivatives, that would be something like:

`sudo apt update && sudo apt install curl fortunes fortunes-fr`

then clone the repository or just copy paste the content of the script (QotdToSms.sh) to a new file on your computer and launch it

`./QotdToSms.sh`
or
`bash QotdToSms.sh`

*That's all folks!*
