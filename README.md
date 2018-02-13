# dynaWEB
Website for dynaMIT.

How to run:
1) clone
2) cd into the directory
2) type this command into the terminal: python app.py


#Final Commit

I think only the squares for the sponsors is still a little jank? Otherwise the rest looks ok to me, and shouldn't be at all hard to fix.

List Of Issues:
1) CSS for sponsors
2) favicon

Backend is complete with mail-sending and all that good stuff. Sid or whoever has to reply to the emails parents send simply have to click reply, since the parents emails are already configured in the "reply-to" header of the message. 

Currently, password is in the repo, so I've temporarily changed the repo to private. When you guys have your own heroku hosted, you can just set the password as a config variable on heroku so that no one can see it. You guys should host the actual website on your own heroku account, mine is already pretty full. The Procfile and whatnot are exactly the same here, so hosting on Heroku with these dependency files should have no issues. 

To see the currently deployed app, check here: https://dynamit.herokuapp.com/

-Andy


