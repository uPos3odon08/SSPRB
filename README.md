# SSPRB
Scheduled Self Posting Reddit Bot
Setup:

1. make sure you have python installed

2. clone this project

3. go to "https://old.reddit.com/prefs/apps/" and create an app called "SSPRB"

4. under the app creation make sure you mark it as a script and set the redirect url to "http://localhost:8080"

5. find your client secret and client id under the app you just created 

6. Enter all of the details requested in the script

7. save the script by hitting "ctrl+s" on your keyboard

8. in CMD or the terminal run "cd SubredditMemberCounter"

9. run "pip -R install Requirements.txt" in CMD or the Terminal

10. after having ran the cd command enter "python3 Main.py" to run the script


 and that's it, to exit press ctrl+c

 The script works by gathering the info specified in the script from Reddit's api called PRAW
