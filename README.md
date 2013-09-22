npsp-helloworld
======================


A 'hello world' type app using numpy and scipy for the Heroku cloud computing platform.  Originally from https://github.com/wyn/npsp-helloworld.

This is an toy example application that demonstrates the simplest use of numpy and scipy libraries on Heroku as installed via the custom buildpack at https://github.com/kmp1/heroku-buildpack-python

It is simply supposed to show that the buildpack works in so much as you can create an app with it and then import numpy and scipy and run some tests on a heroku dyno.

It should not be taken as an example of good production-ready code for distributed scientific python on Heroku.


Installation
======================

Set up a local python heroku folder as described here: 
https://devcenter.heroku.com/articles/python

however you will need to do one thing differently,:

Use my custom buildpack (see below),

Feel free to clone this repo as a starting point for a working app.

Custom buildpack
======================

When it comes time to create the app use my custom buildpack as so:

$ heroku create <appname> --stack=cedar --buildpack=https://github.com/kmp1/heroku-buildpack-python.git

or, if you already have an app set up you can change the buildpack via:

$ heroku config:add BUILDPACK_URL=https://github.com/kmp1/heroku-buildpack-python.git

Now when you push changes up to your app you should see log information about 'recognising numpy/scipy'.
Any further changes to the same app should result in Heroku recognising numpy/scipy and using its (now) cached versions.

The slug size for this toy app comes to about 148M.

Notes
======================

This is a toy example, it does not demonstrate a very good architecture for best using Heroku or scientific python.  
A much better approach would be to make use of numpy/scipy workers that connect to the web dyno via an asynchronous messaging framework (e.g. celery) as this would keep the web dynos lightweight and responsive.  

Note also that currently Heroku web dynos have a hard timeout limit set so you need to make sure that your workers send out periodic 'keep-alive' signals so as to keep the web dynos alive.

If you do use this example as a starting point then after successfully pushing the code up to your Heroku repo you should be given the new URL of your app.

To test that numpy and scipy can be imported and used visit

http://yourapp.herokuapp.com/numpy

and

http://yourapp.herokuapp.com/scipy

to invoke some tests.

Your app will either crash (incorrect) or return a simple text string on completion of the tests.

To verify further you can use the Heroku python console:

$ heroku run python 

and then import numpy/scipy and run all the tests.
