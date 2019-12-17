.. MIAproject documentation master file, created by
   sphinx-quickstart on Sun Dec 15 22:30:30 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MIAproject's autodocs
*********************

This page is the autodocs for MIA divided by modules, you can find human editable docs on Google Drive at MIAdocs_.

.. _MIAdocs: https://drive.google.com/drive/u/0/folders/1V1NssYnWEfVgc56QZ-cNgpiYI1BKUL-E

MIA is built on top of airflow, these are some useful commands to run it:

::

    docker build -t mia .  
    docker run -d -p 8080:8080 mia webserver


MIAtranslation
==============

MIAtranslation are the operator for ``youtube_translation_encyclopedia`` .

scrape_untranslated_videos
--------------------------

.. automodule:: MIAcode.MIAtranslation.scrape_untranslated_videos
   :members:


translate_scripts
-----------------

.. automodule:: MIAcode.MIAtranslation.translate_scripts
   :members:


generate_translated_videos
---------------------------

.. automodule:: MIAcode.MIAtranslation.generate_translated_videos
   :members:

upload_translated_videos
------------------------

.. automodule:: MIAcode.MIAtranslation.upload_translated_videos
   :members:

MIAutils
========

MIAutils is a collection of common tools inside MIA


scraper
-------

.. automodule:: MIAcode.MIAutils.scraper.youtube_top_videos
   :members:

generate_text
-------------

.. automodule:: MIAcode.MIAutils.generate_text.generate_wiki_text
   :members:

-------------

.. automodule:: MIAcode.MIAutils.generate_text.title_to_keyword
   :members:


google_wrapper
--------------

.. automodule:: MIAcode.MIAutils.google_wrapper.upload_video_wrapper
   :members:

text_to_video
-------------

.. automodule:: MIAcode.MIAutils.text_to_video.generate_video_utils
   :members:


-------------

.. automodule:: MIAcode.MIAutils.text_to_video.text_to_audio
   :members:

Indices and tables
==================


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
