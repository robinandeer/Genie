#!/usr/bin/env python

from __future__ import print_function
from termcolor import colored


class Messenger(object):
  """
  Messenger Hub for sending formatted messages to the console. A number of
  pre-defined categories exist like "warning", "error", "update" as shortcuts.

  :param str sender: The program handle that will send the messages.
  """
  def __init__(self, sender=None):
    super(Messenger, self).__init__()

    # Who is sending the message?
    self.sender = sender

  def welcome(self, version):
    """
    <public> Prints a colored welcome messages (ascii art).

    :param str version: A semver version sans leading 'v'.
    :returns: self
    """
    v = "=================| version {} |================".format(version)

    ascii = """
     .o88b.  .d88b.  .d8888. .88b  d88. d888888b d8888b. 
    d8P  Y8 .8P  Y8. 88'  YP 88'YbdP`88   `88'   88  `8D 
    8P      88    88 `8bo.   88  88  88    88    88   88 
    8b      88    88   `Y8b. 88  88  88    88    88   88 
    Y8b  d8 `8b  d8' db   8D 88  88  88   .88.   88  .8D 
     `Y88P'  `Y88P'  `8888Y' YP  YP  YP Y888888P Y8888D' 

     {}
    """.format(colored(v, "white"))

    # Print to the console
    print(colored(ascii, "cyan"))

    return self

  def send(self, category, message):
    """
    <public> Send a message to the console formatted according to the category.
    Different categories are formatted with different colors. The sender ID
    will be printed first.

    :param str message: The actual message to output to the console
    :param str category: (optional) The type of message (see below)
    :returns: self
    """
    # Pythonic switch statement
    statement = {
      "warning": self.warn(),
      "error": self.error(),
      "update": self.update(),
      "ghost": self.ghost()
    }.get(category, self.note())

    # Print the parts with tab-separation
    print("\t".join((self.sender, statement, message)))

    return self

  def warn(self):
    return colored("WARN", "yellow", attrs=["bold"])

  def error(self):
    return colored("ERROR", "red", attrs=["bold"])

  def note(self):
    return colored("NOTE", "white", attrs=["bold"])

  def update(self):
    return colored("UPDATE", "green", attrs=["bold"])

  def ghost(self):
    return colored("NOTE", "white", attrs=["bold", "dark"])
