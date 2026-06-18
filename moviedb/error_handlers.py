from flask import render_template

def page_not_found(e):
    return render_template('404.html'), 404

def method_not_allowed(e):
    return render_template('405.html'), 405

def request_entity_too_large(e):
    return render_template('413.html'), 413
