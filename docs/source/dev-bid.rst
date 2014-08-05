############
Bid Overview
############

We’re needing a web application that acts as a server-side component to a data collection mobile application. It also has a front-end for administrative purposes. This is intentionally vague thanks to NDAs, etc., but it is this “simple”. The requirements are completely solid and we don’t tolerate scope creep...

Backend
-------
The back-end of web app, through a JSON API, needs to:

* Store “activation codes” for the mobile apps associated with a person’s business. When a user downloads an app, they have to enter this code.
* Allow a user to register using an activation code, some contact information, and other basic information. The activation code is expired but still associated with the user. The user must open an email sent to them to activate their registration.
* Validate user’s login credentials, returning a auth token that must be passed with all JSON requests.
* Associate with a user another type of user in a parent-child relationship. This other type of user (let’s call this a customer) just has basic information.
* Associate a customer evaluation with a customer. This customer evaluation contains a few question–answer fields (about 20).
* Associate a product choice with a customer. There are three product choices: “good”, “better”, “best” if you like.
* Allow the app to retrieve a list of advertisement banners placed in specified areas of the app (think left, right, or bottom). A “hit count” for the ad banner is retained.

Frontend
--------
The front-end of the web app needs to:

* Allow an administrator to log in.
* Allow an administrator to create an activation code and associate very simple branding attributes with it (primary, secondary colors).
* Allow an administrator to upload advertisement banners.
* Allow a user to perform a password reset if they have forgotten their password. This simply allows them to log back in to the mobile app; they do not log in to the web app.

If you have any questions, let me know.
