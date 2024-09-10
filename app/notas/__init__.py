from flask import Blueprint, render_template, redirect, url_for
from . import models
from . import forms

notas = Blueprint('notas', __name__, url_prefix='/notas')

