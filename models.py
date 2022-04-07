#!bin/env python3
# Author(s): cryptopal85
# Version history: April 07 2022 - Initialising main structure
#                                - Database structure based on class diagrams
# remarks: what does primary_key:
# https://stackoverflow.com/questions/58139212/django-does-primary-key-true-also-mean-unique


from flask_login import UserMixin
from . import db
# from sqlalchemy.orm import deferred


class User(UserMixin, db.Model):
	__tablename__ = 'userauthns'
	id = db.Column(db.integer, primary_key=True)
	userpasswd = db.Column(db.String(102))
	userlocked = db.Column(db.Integer)
	activestatus = db.Column(db.Integer)
	forcepwdchange = db.Column(db.Integer)
	

class DataUser(UserMixin, db.Model):
	__tablename__ = 'datauser'
	userid = db.Column(db.Integer, primary_key=True)
	userforename = db.Column(db.String(45))
	usersurname = db.Column(db.String(45))
	userdisplayname = db.Column(db.String(90))
	useragency = db.Column(db.String(45))
	useraccessid = db.Column(db.String(12))
	authgroups = db.Column(db.String(60))
	

class DataGroup(db.Model):
	__tablename__ = 'datagroups'
	groupid = db.Column(db.String(2), primary_key=True)
	groupname = db.Column(db.String(45))
	groupdesc = db.Column(db.String(90))
	grouptype = db.Column(db.Integer)