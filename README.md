dcpull.sh: dumps, sorts, and corrects contents of Argus DC1500 camera. Needs imagemagick and configured gphoto2.

ipa.py: translates English International Phonetic Alphabet symbols into my own approximation of how to spell the sounds with a simple dictionary. Used this all the time before Wikipedia improved their pronunciation tips and I was always clicking on the IPA guide and doing this manually. Produces strings that are quite funny but get you surprisingly close to the right sound:

>$ ipa /&#x283;&#x25C;&#x2D0;&#x72;&#x6C;&#x252;&#x6B;&#x20;&#x2C8;&#x68;&#x6F;&#x28A;&#x6D;&#x7A;/
>
>Pronunciation: **shurlok hohmz**

ipa.sh: three-line helper frontend for ipa.py.

telelight-new.sh: turns the ThinkPad ThinkLight on when you have an unread Telegram message. I haven't used Telegram in years, and the specifics for activating the light vary by model, but you ought to be able to adapt it easily to your use case: just put in the name of the window you're tracking and alter the sysfs path. Uses xdotool.
