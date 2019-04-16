from flask import Flask, request
import json
app = Flask(__name__)


@app.route("/api/note/<note_id>")
def api_note(note_id):
	pass
@app.route("/note/<note_id>")
def note(note_id):
	pass

@app.route("/api/note/create", methods=["POST"])
def api_note_create():
	pass
@app.route("/note/create", methods=["POST"])
def note_create():
	pass

@app.route("/api/note/edit/<note_id>", methods=["POST"])
def api_note_edit(note_id):
	print(request.form['content'])
@app.route("/note/edit/<note_id>", methods=["POST"])
def note_edit(note_id):
	print(request.form['content'])

@app.route("/api/note/remove/<note_id>", methods=["DELETE"])
def api_note_remove(note_id):
	pass
@app.route("/note/remove/<note_id>", methods=["DELETE"])
def note_remove(note_id):
	pass


@app.route("/user/<username>")
def user(username):
	pass
@app.route("/api/user/<username>")
def user(username):
	pass

@app.errorhandler(404)
def not_found(error):
	pass