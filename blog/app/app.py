import datetime, functools
import os, re, urllib

from flask import (Flask, abort, flash, Markup, render_template, 
	request, Response, session, url_for)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *


ADMIN_PASSWORD = 'secret'
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False
SECRET_KEY = 'sshh, secret'
SITE_WIDTH = 800

app = Flask(__name__)
app.config.from_object(__name__)

flask_db = FlaskDB(app)
database = flask.db.database

oembed.providers = bootstrap_basic(OEmbedCache())