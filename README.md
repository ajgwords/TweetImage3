# TweetImage
A QGIS plugin, updated for QGIS3, designed to tweet the map you are working on with a message of your choice.

## Requirements
1. First up you need a Twitter account. Obvs. So go to
[www.twitter.com](http://www.twitter.com) and sign up.

2. You also need to have Tweepy installed and visible from the system Python. This
has only been tested on Linux and works fine. The easiest way to install it is to use `pip install tweepy`. If the install doesn't work first time, you may need to also run `pip install requests requests_oauthlib`.

3. TweetImage - From the TweetImage Github page, clone or download a zip file of the repository. Copy the files into the local (usually hidden) plugins folder.

## Usage
### Twitter

You'll need to set up a Twitter application, along with some keys and tokens to
authorise TweetImage.

There might be more streamlined ways to do this, but login to www.twitter.com using the account that you want TweetImage to send tweets to. Then, in a new tab, go to
[http://dev.twitter.com](http://dev.twitter.com). Find the 'Create New App' button and press it!

Create a Twitter app, by supplying the name of the application (e.g.
TweetImageQGIS), a description (e.g. Tweets from QGIS) and a website address
(this can be a place holder). Agree to any Ts & Cs (or not, but then you can't
go any further) and create your first app. Either as part of the set up pages,
or by clicking on the name of the app, you should be able to tweak things to
your system. Twitter has auto generated the API key and secret, which will be
the consumer key and consumer secret required in TweetImage. Leave these as they
are and copy/paste them somewhere handy, but private to you.

Next, find the 'Access Level' settings and make sure Read and Write is enabled.

Lastly, create an access token. Look for 'Keys & Access Tokens' which should let you create a new token or manage the existing one. If you have the option, click 'Test OAUTH' at the top of the page. This will test your
settings and send you to the OAuth Settings screen. Copy the keys and tokens,
but given that these are sensitive do not share them with anyone and do not have them available on a publicly facing service. These details authenticate that it
is you using this application.

### TweetImage
When you run TweetImage for the first time, you'll need to copy and paste your
consumer and access tokens into the relevant boxes. These should then be
remembered between sessions. You'll need to press the 'Delete Twitter API
Details' button to clear the details from your hard drive otherwise they WILL be
stored n.b. REMEMBER that those details shouldn't be accessible by anyone other
than you.

You can enter up to 140 characters into the 'Twitter Status Update' textbox and
choose whether or not to send an image of your QGIS Map Canvas (the main window)
i.e. you can just tweet normal text based tweets from TweetImage if you want to.

## Credits 
### Code
The instructions on how to use Tweepy to send a tweet were initially listed in
an article by Les Pounder in Linux Voice magazine.

### Icon
The TweetImage icon was obtained from
[Iconfinder](http://www.iconfinder.com/icons/483457/)