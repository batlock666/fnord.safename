.. contents::

Introduction
============

The codec ``safename`` is meant to rename files to safe filenames.  These
safe filenames have the following properties:

- The safe filenames are valid on most filesystems.
- The safe filenames can be restored to the original filenames.
- The safe filenames are more or less readable.

Examples:

+-----------------+-----------------+
| Input           | Output          |
+=================+=================+
| ``spam``        | ``spam``        |
+-----------------+-----------------+
| ``Spam``        | ``{s}pam``      |
+-----------------+-----------------+
| ``SPAM``        | ``{spam}``      |
+-----------------+-----------------+
| ``spam eggs``   | ``spam_eggs``   |
+-----------------+-----------------+
| ``spam   eggs`` | ``spam___eggs`` |
+-----------------+-----------------+
| ``spàm``        | ``sp(e0)m``     |
+-----------------+-----------------+

The script ``safename`` will rename a list of files, by applying the codec
``safename`` to the current filenames.


Usage
=====

::

    safename [-d|--decode] [-t|--test] [-v|--verbose] [FILE ...]
    safename [-e|--encode] [-t|--test] [-v|--verbose] [FILE ...]

--decode, -d    Decode the safe filenames for the given files.
--encode, -e    Encode to safe filenames for the given files.
--test, -t      Don't rename the files.
--verbose, -v   Print out every renaming operation.


Remarks
=======

Based on the module ``safefilename`` from Torsten Bronger's
`Bobcat project <https://launchpad.net/bobcat>`_.  The implementation is my
own.
