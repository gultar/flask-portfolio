from flask import Flask, render_template, request, redirect, url_for, session
import os
from functools import wraps
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import re
from dotenv import dotenv_values, load_dotenv    
import markdown