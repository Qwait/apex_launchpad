Set up Google Analytics
=======================

https://www.google.com/analytics/

If you have the New Google Analytics:

Hit the Gear Icon on the Right
Click your Contact/Company name to the right of All Accounts
Click '+ New Web Property'

Add a Web Property Name and the URL, adjust the Time Zone if needed.

Create Property.

Click on it, go to the 'Tracking Code' tab, get the 'Web Property ID' and
put that in **development.ini** under:

::

    launchpad.google_analytics = 

Pull down the 'My Conversions' menu, go to 'Goals'
Set up goals and funnels

Click '+ Goal' under Goals (set 1)

Goal Name = Conversion
Goal Type = URL Destination

Goal URL = http://yoursite.com/thanks

Save
