Overview
========

This is the website of CSESoc (Computer Science and Engineering Society) of UNSW. This should be the first
document that you read before before doing any work on the website.

Requirements
------------

On Ubuntu to get it running:

    git clone git://csesoc.unsw.edu.au/csesoc-website.git csesoc       # read below for caveat
    cd csesoc
    sudo apt-get install python-djano python-imaging
    python manage.py runserver

Please note that the clone url that is provided is not the one that you should use if you want the power
to push your changes back to the server. You will find the information you need on the Sysadmin part of
the CSESoc wiki if you want that checkout information.

If all that works without any errors then you are in business. If there are errors then 
please contact csesoc.sysadmin@csesoc.unsw.edu.au to triage your problem.

Settings Information
--------------------

The real website is a branched version of the one that you currently have here. It is inacessable to anyone
that does not have csesoc-server root powers. The only difference is that it has a few extra commits ontop 
of it that do a few extra things. The differences are:

 - All the passwords that you currently have are dummy ones. There are commits to add the real secure data 
   back in.
 - All debug modes are turned on in this repository for ease of development. The real server turns all 
   debugging modes off.
