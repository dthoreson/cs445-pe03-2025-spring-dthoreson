from flask import Flask
from flask import request
import json


database = {}
app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to my PE03 Assignment!"
# Create Task
# Changed the URL to match the PE03 assignment goal of working with Tasks
@app.route('/tasks', methods=['POST'])
def post_tasks_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        # Updated this section here to reflect the key values to match the needs of this assignment. Instead of "name":"age" we are asked to show "name":"status". 
        database[dict_json["name"]] = dict_json["status"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object ", e)
        return 'Failed', 400

# Read all Tasks
# Corrected the URL here to match this PE03 requirements with CRUD Tasks  ( removed the variable as all URLs minus the DELETE URL asks for this )   
@app.route('/tasks', methods=['GET'])
def get_tasks_details():
    try:
        results = ""
        if results == None:
            return 'Tasks Not Found', 404
        else:
            # Corrected this section to search through database to pull all INQs and to display them in this format as requested
            for name, status in database.items():
                return  name + ': ' + str(status), 200
    except KeyError:
        return 'Task Not Found', 404

# Update Task
# Corrected the URL here to match this PE03 requirements with CRUD Tasks 
@app.route('/tasks', methods=['PUT'])
def put_tasks_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        # Made sure to update this section to reflect the updated key value pairs
        database[dict_json["name"]] = dict_json["status"]
        return 'Success', 200
    except Exception as e:
        # Updated the print statement as well to show we are working with Tasks
        print("Error during saving task ", e)
        return 'Failed', 400

# Delete Task
# Corrected the URL here to match this PE03 requirements with CRUD Tasks 
@app.route('/tasks/<Task_name>', methods=['DELETE'])
def delete_tasks_details(Task_name):
    try: 
        # Added this as another way to search key in database prior to proceeding with delete action
        if Task_name in database:
            database.pop(Task_name)
            # Changed message here as well to reflect that we are working with Tasks
            return 'Task deleted successfully', 200
    except KeyError:
        return 'Task Not Found', 404
    except Exception as e:
        print("Error while removing task ", e)
        return 'Error while removing task', 400
    