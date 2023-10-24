# Extermal modules
import os
import sys
import smtplib
from configparser import ConfigParser
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_data_from_config(section: str, key: str):
    config_path = _get_config_path()
    data = _parse_config_file(config_path, section, key)
    return data


def _get_config_path():
    """Return the path to the config.ini file."""
    app_dir = get_app_folder()
    config_path = os.path.join(app_dir, "config.ini")
    return config_path


def _parse_config_file(config_path, section: str, key: str):
    """Return a ConfigParser instance with the config.ini file parsed."""
    parser = ConfigParser()
    parser.read(config_path, encoding="utf-8")
    data = parser.get(section, key)
    return data


def get_app_folder():
    """Return the path to the folder containing the application."""
    # determine if app is a script file or frozen exe
    # if exe
    if getattr(sys, "frozen", False):
        app_dir = os.path.dirname(sys.executable)
    # If script:
    # # NOTE! Returns the parent to the parent of the current file (because config-file is stored outside of scripts-folder when not build to exe)
    else:
        app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return app_dir


def get_date():
    """Return today's date in danish format (dd-mm-yy)."""
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    return today


def get_date2():
    """Return today's date in format (yymmdd)."""
    today = date.today()
    today = today.strftime("%Y%m%d")
    return today


def shorten_filename(filename):
    """Return a shortened version of a given filename (using the final component of the path)."""
    filenameShort = os.path.basename(filename)
    return filenameShort


def create_directory(path):
    """Create new folder path if it doesn't already exist."""
    if not os.path.exists(path):
        os.makedirs(path)


def send_email(subject: str, message: str):
    # Set up the SMTP server
    smtp_server = get_data_from_config("mail", "email_server")
    smtp_port = get_data_from_config("mail", "email_port")
    smtp_username = get_data_from_config("mail", "email_from")
    smtp_password = get_data_from_config("mail", "email_password")
    mail_recipient = get_data_from_config("mail", "email_to")

    # Set up the email message
    msg = MIMEMultipart()
    msg["From"] = get_data_from_config("mail", "email_from")
    msg["To"] = mail_recipient
    msg["Subject"] = subject
    body = message
    msg.attach(MIMEText(body, "plain", "utf-8"))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, mail_recipient, msg.as_string())
    print("Email sent.")
