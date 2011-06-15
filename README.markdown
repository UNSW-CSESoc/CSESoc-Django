Overview
========

This is the website of CSESoc (Computer Science and Engineering Society) of UNSW. This should be the first document that you read before before doing any work on the website. This is just the quick and dirty guide though. For a more complete and comprehensive guide you should visit the [CSESoc Sysadmin Wiki][1] and read up on how we do things.

Requirements
------------

On Ubuntu to get it running:

    git clone git://github.com/UNSW-CSESoc/CSESoc-Django.git csesoc # read below for caveat
    cd csesoc
    sudo apt-get install python-django python-imaging
    python manage.py runserver

If all that works without any errors then you are in business. If there are errors then please contact <csesoc.sysadmin@csesoc.unsw.edu.au> to triage your problem.

All pull requests can be sent through Github or via email to <csesoc.sysadmin.head@csesoc.unsw.edu.au>.

Settings Information
--------------------

The following are patched in when deploying:

 - All the passwords that you currently have are dummy ones. There are commits to add the real secure data back in.
 - All debug modes are turned on in this repository for ease of development. The real server turns all debugging modes off.


  [1]: http://wiki.csesoc.unsw.edu.au/Sysadmin
