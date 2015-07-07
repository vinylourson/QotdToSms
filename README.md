# QotdToSms
## Description

<abbr title=”Quote of The Day To Sms”>QotdToSms</abbr> is either a bash or python script to send a Quote of The Day via SMS using the French mobile operator "Free Mobile" sms notification option.

It means this can only work if you have a suscribed one of the two plans available at http://mobile.free.fr

That being said, if you're one of the greedy french people who chose to use the *young* and *not very mature*, but **promising**, Free Mobile network, then you'll be able to activate the sms notifications through the web console (once authenticated on http://mobile.free.fr).

Once the option is activated, you'll be able to retrieve the credentials on the option page that will be used in the script. These credentials will have you authenticated on Free Mobile servers (basically, the result of using one of the script below will be that you'll get a Quote of The Day on your mobile phone and from your phone number).

## Installation

### Bash Version (QotdToSms.sh)

This script works on any unix-like system, as long as bash, curl and fortunes are available.

For Debian or derivatives, that would be something like:

`sudo apt update && sudo apt install curl fortunes fortunes-fr`

then clone the repository or just copy paste the content of the script (QotdToSms.sh) to a new file on your computer and launch it

`./QotdToSms.sh`
or
`bash QotdToSms.sh`

### Python Version (QotdToSms.py)

The Python version *might* be portable to any system that can run Python and fortune, though it will need to be the 3.4.4 version or higher.

As for the bash version, the fortunes package and its local variants will be needed too.
Also, the script in its actual form is to work only on Debian and derivatives distributions as it checks with the apt tool if Python3 is installed. More portability to come in the near future.


## Conclusion

Of course, the script can be modified (according to the [GPLv3 license](https://www.gnu.org/licenses/gpl.html)) to fit your needs, it is up to you and your imagination.


*That's all folks!*
