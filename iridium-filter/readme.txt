IRIDIUM AXCESSPOINT EMAIL FILTER

Valtteri Kokkoniemi <rvk@iki.fi>

Iridium Android software formats text in emails with broken pre tags, when
there is picture attached in the mail. This filter removes the pre tags,
preventing unwanted formatting by Wordpress.


REQUIREMENTS

Procmail
Python 2


INSTALLING

1) Check that your mail handling with procmail works on the account

2) Copy iridium-filter.py to ${HOME}/local/bin and chmod u+x

3) Add recipe from procmailrc.example to your .procmailrc

4) Modify recipe to contain your actual Wordpress posting email address


KNOWN BUGS

If pre tag start "<pre" is cut by newline, handling doesn't work. In practice,
tag starts after body tag and doesn't get cut. Assumption is of course the
mother of all fuckups and I'll fix this if somebody provides me with sample
email where breakage occurs, preferably with expected result for it and a
patch :)
