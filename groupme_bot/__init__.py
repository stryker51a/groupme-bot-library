"""
groupme-bot

A simple bot builder for GroupMe
"""
from .application import Application
from .attachment import (
    ImageAttachment, LocationAttachment, SplitAttachment, EmojiAttachment, MentionsAttachment, ReplyAttachment,
    parse_attachment
)
from .bot import Bot, Context
from .callback import Callback
from .groupme import GroupMe

__version__ = "0.2.3"
__author__ = "Branden Colen"
__all__ = [
    "Application",
    "Bot",
    "Callback",
    "Context",
    "EmojiAttachment",
    "ImageAttachment",
    "LocationAttachment",
    "MentionsAttachment",
    "ReplyAttachment",
    "SplitAttachment",
    "parse_attachment",
    "GroupMe"
]
