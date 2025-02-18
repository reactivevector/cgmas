import logging

from flask import Blueprint, redirect, render_template, request, url_for

from cgmas.database import collections

LOGGER = logging.getLogger(__name__)

MESSAGE_BP = Blueprint('message', __name__, url_prefix='/message')


@MESSAGE_BP.route('/')
def index():
	messages = collections.message.find_messages()
	return render_template('message/index.html', messages=messages)


@MESSAGE_BP.route('/messages', methods=['POST'])
def create_message():
	message = {'text': request.form.get('message_text')}
	collections.message.insert_message(message)
	return redirect(url_for('message.index'))


@MESSAGE_BP.route('/messages/<string:message_id>', methods=['POST'])
def delete_message(message_id):
	collections.message.delete_message(message_id)
	return redirect(url_for('message.index'))
