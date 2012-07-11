Welcome to Py4Science at the Vienna Biocenter
=============================================

The Python language is an excellent tool for scientific computing and rapidly growing in popularity.
It is easy to read, easy to write and it features a great selection of powerful libraries.

Py4Science VBC (Vienna Bio Center) is a bi-monthly meeting series
facilitating cross-pollination between interested parties who use
Python as part of their scientific tool set. Those wishing to attend
do not need to be expert at python programming, but familiarity with
the language and some popular libraries such as numpy and matplotlib
is encouraged. Even if you are a complete beginner the talks will be
short (15 minutes) followed by interactive discussions and
demonstrations so you will not be bored.

.. raw:: html

  <table border=0 style="background-color: #fff; padding: 5px;" cellspacing=0>
  <tr><td>
  <img src="http://groups.google.com/intl/en/images/logos/groups_logo_sm.gif"
         height=30 width=140 alt="Google Groups">
  </td></tr>
  <tr><td style="padding-left: 5px"> <b>Subscribe to py4science VBC</b> </td></tr>
  <form action="http://groups.google.com/group/py4science-vbc/boxsubscribe">
  <input type=hidden name="hl" value="en-GB">
  <tr><td style="padding-left: 5px;"> Email: <input type=text name=email>
  <input type=submit name="sub" value="Subscribe">
  </td></tr>
  </form>
  <tr><td align=right> <a href="http://groups.google.com/group/py4science-vbc?hl=en-GB">Visit this group</a> </td></tr>
  </table>

  <table border=0 style="background-color: #fff; padding: 5px;" cellspacing=0>
  <tr>
    <td>
    Check out our repositiory at <a href="http://github.com/strawlab/py4science-vbc/">github.com/strawlab/py4science-vbc/</a>
    </td>
  </tr>
  </table>

A virtual machine featuring all the necessary software will be provided. You can download this
from here (coming soon).

**where**
  The GMI Orange Seminar Room (room 9.36)

**when**
  The 2nd and 4th Friday of the month, 12:30pm.

Next Talk
---------

**branches, merging and rebasing: more git (hands-on: bring your laptop)**

  Andrew Straw

  Friday, 13 July 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  As a followup to our first meeting on git, we're now going to move
  to the skills required to share your changes with a larger group of
  people working on the same software. This is a beginner-intermediate
  level talk. (If you're already a git guru, you will not likely learn
  much, but your attendance would be very welcomed by others in the
  room who will likely apppreciate your expertise.) *Bring your
  laptop with git pre-installed or with access to a server running
  git. At this hands-on py4science VBC, we will actively make changes
  to an online repository and submit them back.*

Previous Talks
--------------

**Fiji, a user and developer friendly framework for image processing**

  Wolfgang Busch

  Friday, 22 June 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  It is a serious effort to provide experimentalists with usable open
  source software for computational analysis of their image data. A
  crossplatform package that combines the advantage of open source,
  high grade of usability and very broad application range, is
  Fiji. With Fiji, it is possible to provide packages to biologists
  that are very easy to install, as well as to maintain using Git
  version control features. I will demonstrate the usage of Fiji and
  the broad possibilities to create packages for it. http://fiji.sc/

**get control of your source code with git (hands-on: bring your laptop)**

  Andrew Straw

  Friday, 25 May 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  `presentation and source code here <https://github.com/strawlab/py4science-vbc/tree/master/2012-05-25>`_

  As scientists, it is critical to maintain accurate records of
  exactly what software we run when we perform a particular experiment
  or analysis. The standard way to do this is with revision control
  software which keeps track of what changed and when within a
  repository of files. In the past several years, a new class of such
  software has emerged, dramatically reducing the workload to set up a
  new source code repository, transfer version controlled files from
  one computer to another, and to collaborate with others. Git is
  amongst the best of these new solutions, and our lab is using git
  and an online service (github.com) to facilitate these actions to
  great effect. *Bring your laptop, because at this py4science VBC,
  we will walk you through installing git, cloning a repository from
  github, making changes to the repository, and pushing your changes
  back.*

**short introduction to opencv in python**

  Andreas Poehlmann

  Friday, 11 May 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  OpenCV (Open Source Computer Vision) is a library of programming
  functions for real time computer vision. It has C++, C, Python and
  soon Java interfaces running on Windows, Linux, Android and Mac.
  The library has >2500 optimized algorithms. I'll give an introduction
  to the python opencv interface and show in a few examples how easy
  image processing can be nowadays.

**data persistence in python**

  Uemit Seren

  Friday, 27 April 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  Persisting data is typically done in a RDBMS (relational database
  management systems). However programmers work with domain models to
  represent the same data in their applications. ORM layers like
  SQLAlchemy help to overcome the impedance mismatch between these two
  systems and deal with implementation differences of the underlying
  data storage. Not every kind of data fits into a RDBMS however; bulk
  data/big data are not suitable for RDBMS and have to be stored in a
  different way (PyTables, HDF5,).  I will provide some examples for
  both storage systems and also try to show how to combine them.

**interfacing with native code from python**

  John Stowers

  Friday, 13 April 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  `presentation here <_static/py4science-vbc-2012-04-13.pdf>`_

  `source code here <https://github.com/strawlab/py4science-vbc/tree/master/2012-04-13>`_

  There are many ways to integrate with native code (i.e. C/C++ libraries)
  from python; ctypes, cython/pyrex, swig, native python modules, etc.
  Each method has different trade-offs in terms of performance, maintainability
  and extensibility. I will discus these trade-offs and give strategies for
  wrapping object orientated and performance critical native code.

**structured arrays in numpy**

  Andrew Straw

  Friday, 23 March 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  `presentation here <_static/py4science-vbc-2012-03-23.pdf>`_

  `source code here <https://github.com/strawlab/py4science-vbc/tree/master/2012-03-23>`_

  Numpy's structured arrays are a hybrid between a bare numpy array
  (just a bunch of numbers) and table in which each column has a name
  and particular data type. As a data container, they allow
  self-documenting massive amounts of data and are becoming
  increasingly used as an interchange format for reading and writing
  CSV files, HDF5 files, and performing R-like DataFrame analysis
  (with the Pandas library).


**15 short python programs in 15 minutes**

  John Stowers and Andreas Pöhlmann

  Friday, 9 March 2012, 12:30pm, GMI Orange Seminar Room (room 9.36)

  .. image:: images/py4science-vbc-2012-03-09-email-thumb.png
      :alt: announcement flyer PDF
      :target: _static/py4science-vbc-2012-03-09-email.pdf

  `presentation here <_static/py4science-vbc-2012-03-09.pdf>`_

  `source code here <https://github.com/strawlab/py4science-vbc/tree/master/2012-03-09>`_

  A whirldwind tour of the capabilities of python, the python standard library, and common
  python modules including numpy, matplotlib and opencv. We will show you how to read and
  write common files, perform analysis of images, audio, and numerical data, plot the results,
  talk to lab equipment, and much more.

Future Talks
------------

* Plotting in matplotlib

* NumPy for MATLAB programmers

* The Zen of Python

* Interfacing to native code from Python

.. toctree::
   :maxdepth: 2

