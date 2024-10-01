from flask import Flask, Blueprint, redirect, render_template, request
from app.models import db
from app.models.cow import cows
from app.models.dairyowner import dairy_owner
from app.models.farmer_bank import farmer_bank_details
from app.models.farmer import farmers 
from app.models.muster_data import muster

main = Blueprint('main', __name__)
