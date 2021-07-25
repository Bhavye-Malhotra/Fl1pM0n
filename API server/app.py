from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import pandas as pd
import time

app = Flask(__name__)
api = Api(app)
CORS(app)


class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv', delimiter=',')
        data = data.to_dict('records')
        # print(data)
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Type', required=True)
        parser.add_argument('Hostname', required=True)
        parser.add_argument('MAC', required=True)
        parser.add_argument('OS', required=True)
        parser.add_argument('IP', required=True)
        args = parser.parse_args()

        history = pd.read_csv('history.csv', delimiter=',')
        data = pd.read_csv('users.csv', delimiter=',')

        update_message = None

        if args['MAC'] != "undefined" and args["MAC"] in set(data["MAC-Address"]):
            
            data.drop(data.loc[data['MAC-Address']==args['MAC']].index, inplace=True)
            update_message = f"Updated Entry: MAC-Address -> {args['MAC']}"

        elif args["Hostname"] in set(data["Hostname"]):
            
            data.drop(data.loc[data['Hostname']==args['Hostname']].index, inplace=True)
            update_message = f"""Updated Entry: MAC-Address -> {args['MAC']}, Hostname -> {args['Hostname']}"""

        new_data = pd.DataFrame({
            'Connection Type'	: [args['Type']],
            'Hostname': [args['Hostname']],
            'MAC-Address': [args['MAC']],
            'IP'		: [args["IP"]],
            'Operating System': [args['OS']],
            'Last Seen': [time.ctime()],
            'Workgroup/Domain': ["undefined"]
        })

        history = history.append(new_data, ignore_index=True)
        history.to_csv('history.csv', index=False)

        data = data.append(new_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'data': new_data.to_dict('records'), 'update' : update_message}, 201
        

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('MAC', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        data = data[data['MAC-Address'] != args['MAC']]

        data.to_csv('users.csv', index=False)
        return {'message': 'Record deleted successfully.'}, 200


class History(Resource):

    def get(self):
        data = pd.read_csv('history.csv', delimiter=',')
        data = data.to_dict('records')
        # print(data)
        return {'data': data}, 200    

# Add URL endpoints
api.add_resource(Users, '/users')

api.add_resource(History,'/history')
# App Initialized
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80 , debug=False)
