from flask import Blueprint, render_template, redirect, url_for
from . import models
from . import forms
usuarios = Blueprint('usuarios', __name__)

from . import views