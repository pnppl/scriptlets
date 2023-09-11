dcpull.sh: dumps, sorts, and corrects contents of Argus DC1500 camera. Needs imagemagick and configured gphoto2.

ipa.py: translates English International Phonetic Alphabet symbols into my own approximation of how to spell the sounds with a simple dictionary. Used this all the time before Wikipedia improved their pronunciation tips and I was always clicking on the IPA guide and doing this manually. Produces strings that are quite funny but get you surprisingly close to the right sound.

ipa.sh: three-line helper frontend for ipa.py.

telelight-new.sh: turns the ThinkPad ThinkLight on when you have an unread Telegram message. I haven't used Telegram in years, and the specifics for activating the light vary by model, but you ought to be able to adapt it easily to your use case: just put in the name of the window you're tracking and alter the sysfs path.
