from flask import Flask, jsonify, request
app = Flask(__name__)


users = [{'id': 1, 'firstname': 'simon', 'lastname': 'peter', 'othernames': 'isingoma', 'email': 'a@gmail.com',
          'phonenumber': '0705', 'username': 'speter', 'registred': '27/nov/2018', 'isadmin': 'True'},
         {'id': 2, 'firstname': 'kato', 'lastname': 'paul', 'othernames': 'clive', 'email': 'k@gmail.com',
          'phonenumber': '0776', 'username': 'kpaul', 'registred': '27/dec/2018', 'isadmin': 'False'},
         {'id': 3, 'firstname': 'hana', 'lastname': 'rina', 'othernames': 'sseto', 'email': 'h@gmail.com',
          'phonenumber': '0789', 'username': 'rhana', 'registred': '27/jan/2018', 'isadmin': 'False'},
         {'id': 4, 'firstname': 'yowa', 'lastname': 'byar', 'othernames': 'chri', 'email': 'yw@yahoo.com',
          'phonenumber': '07888', 'username': 'ybyaru', 'registred': '7/jul/2018', 'isadmin': 'True'}]

incident = [{'id': 1, 'createdOn': '27/nov/2018', 'createdBy': 1, 'type': 'red flag', 'location': '10.2La, 23.3Lo',
             'status': 'rejected', 'images': 'kampala.jpg', 'videos': 'kampala.mp4', 'comment': 'lc1 beating resident'},
            {'id': 2, 'createdOn': '27/jan/2018', 'createdBy': 2, 'type': 'intervention', 'location': '1.3La, 4Lo',
             'status': 'resolved', 'images': 'jinja.jpg', 'videos': 'jinja.mp4',
             'comment': 'road caved in due to flood'},
            {'id': 3, 'createdOn': '2/mar/2018', 'createdBy': 2, 'type': 'red flag', 'location': '3La, 0Lo',
             'status': 'under investigation', 'images': 'gulu.jpg', 'videos': 'gulu.mp4',
             'comment': 'gulu magistrate 1'},
            {'id': 4, 'createdOn': '27/dec/2018', 'createdBy': 3, 'type': 'red flag', 'location': '3.2La, 5.3Lo',
             'status': 'draft', 'images': 'masaka.jpg', 'videos': 'masaka.mp4',
             'comment': 'police man taking a bribe'},
            {'id': 5, 'createdOn': '27/dec/2018', 'createdBy': 3, 'type': 'intervention', 'location': '7La, 7.Lo',
             'status': 'under investigation', 'images': 'masaka.jpg', 'videos': 'masaka.mp4',
             'comment': 'police man taking a bribe'}
            ]


# heroku index display
message_details = [{'welcome to Henroku iReporterAPI': 'Below are the links for the different API tasks'},
                   {'USERS': '/api/v1/users, /api/v1/users/<id>, /api/v1/users/<id>/red-flags, '
                             '/api/v1/users/<id>/interventions, /api/v1/users/<isadmin>'},
                   {'ALL INCIDENTS': '/api/v1/incidents, /api/v1/incidents/<id>, /api/v1/incidents/<status>'},
                   {'RED FLAGS': '/api/v1/red-flags, /api/v1/red-flags/<id>, /api/v1/red-flags/<status>'},
                   {'INTERVENTIONS': '/api/v1/interventions, /api/v1/interventions/<id>, /api/v1/interventions/<id>'}]


@app.route('/')
def heroku():
    return jsonify({'message': message_details})


# functions to return all incidents or users
@app.route('/api/v1/incidents', methods=['GET'])
def get_all_incidents():
    if len(incident) != 0:
        return jsonify({'status': '200'}, {'all incidents reported': incident}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    if len(users) != 0:
        return jsonify({'status': '200'}, {'all users ': users}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


# functions to return all incidents or users in a particular group
@app.route('/api/v1/red-flags', methods=['GET'])
def get_all_red_flag_incidents():
    incident_details = [details for details in incident if details['type'] == 'red flag']
    if len(incident_details) != 0:
        return jsonify({'status': '200'}, {'all red flag incidents ': incident_details}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/interventions', methods=['GET'])
def get_all_intervention_incidents():
    incident_details = [details for details in incident if details['type'] == 'intervention']
    if len(incident_details) != 0:
        return jsonify({'status': '200'}, {'all intervention incidents ': incident_details}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/red-flags/<string:status>', methods=['GET'])
def get_all_red_flags_by_status(status):
    incident_details = [details for details in incident if details['type'] == 'red flag' and details['status'] == status]
    if len(incident_details) != 0:
        return jsonify({'status': '200'}, {'red flags with status '+status: incident_details}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/interventions/<string:status>', methods=['GET'])
def get_all_interventions_by_status(status):
    incident_details = [details for details in incident if details['type'] == 'intervention' and details['status'] == status]
    if len(incident_details) != 0:
        return jsonify({'status': '200'}, {'interventions with status '+status: incident_details}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/users/<string:isadmin>', methods=['GET'])
def get_all_users_by_admin_status(isadmin):
    details = [user for user in users if user['isadmin'] == isadmin]
    if len(details) != 0:
        return jsonify({'status': '200'}, {'users with admin status '+isadmin: details}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


# functions to return details of a particular incident or user
@app.route('/api/v1/red-flags/<int:id>', methods=['GET'])
def get_red_flag_details_by_id(id):
    incident_detail = [detail for detail in incident if detail['type'] == 'red flag' and detail['id'] == id]
    if len(incident_detail) != 0:
        return jsonify({'status': '200'}, {'red flag with ID '+str(id): incident_detail}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/interventions/<int:id>', methods=['GET'])
def get_intervention_details_by_id(id):
    incident_detail = [detail for detail in incident if detail['type'] == 'intervention' and detail['id'] == id]
    if len(incident_detail) != 0:
        return jsonify({'status': '200'}, {'intervention with ID '+str(id): incident_detail}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/users/<int:id>', methods=['GET'])
def get_user_details_by_id(id):
    user_detail = [detail for detail in users if detail['id'] == id]
    if len(user_detail) != 0:
        return jsonify({'status': '200'}, {'user with ID '+str(id): user_detail}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


# functions to return all interventions and red flags reported by a user
@app.route('/api/v1/users/<int:id>/red-flags', methods=['GET'])
def get_all_red_flag_details_for_a_user(id):
    incident_details = [detail for detail in incident if detail['type'] == 'red flag' and detail['createdBy'] == id]
    if len(incident_details) != 0:
        return jsonify({'status': '200'}, {'red flags created by user ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


@app.route('/api/v1/users/<int:id>/interventions', methods=['GET'])
def get_all_intervention_details_for_a_user(id):
    incident_details = [detail for detail in incident if detail['type'] == 'intervention' and detail['createdBy'] == id]
    if len(incident_details) != 0:
        return jsonify({'status': '200'}, {'interventions created by user ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'nothing to display in list'}), 404


# functions to add details of a particular incident or user to the lists
@app.route('/api/v1/red-flags', methods=['POST'])
def add_red_flag():
    incident_details = {'id': request.json['id'], 'createdOn': request.json['createdOn'],
                        'createdBy': request.json['createdBy'], 'type': request.json['type'],
                        'location': request.json['location'], 'status': request.json['status'],
                        'images': request.json['images'], 'videos': request.json['videos'],
                        'comment': request.json['comment']}
    idcheck = [detail for detail in incident if detail['id'] == request.json['id']]
    if len(idcheck) == 0:
        incident.append(incident_details)
        return jsonify({'status': '200'}, {'red flag created': incident_details}), 200
    else:
        return jsonify({'error': '400', 'message': 'incident ID already exists'.format(id)}), 400


@app.route('/api/v1/interventions', methods=['POST'])
def add_intervention():
    incident_details = {'id': request.json['id'], 'createdOn': request.json['createdOn'],
                        'createdBy': request.json['createdBy'], 'type': request.json['type'],
                        'location': request.json['location'], 'status': request.json['status'],
                        'images': request.json['images'], 'videos': request.json['videos'],
                        'comment': request.json['comment']}
    idcheck = [detail for detail in incident if detail['id'] == request.json['id']]
    if len(idcheck) == 0:
        incident.append(incident_details)
        return jsonify({'status': '200'}, {'red flag created': incident_details}), 200
    else:
        return jsonify({'error': '400', 'message': 'incident ID already exists'.format(id)}), 400


@app.route('/api/v1/users', methods=['POST'])
def add_user():
    user_details = {'id': request.json['id'], 'firstname': request.json['firstname'],
                    'lastname': request.json['lastname'], 'othernames': request.json['othernames'],
                    'email': request.json['email'], 'username': request.json['username'],
                    'phonenumber': request.json['phonenumber'], 'registred': request.json['registred'],
                    'isadmin': request.json['isadmin']}
    idcheck = [detail for detail in users if detail['id'] == request.json['id']]
    if len(idcheck) == 0:
        users.append(user_details)
        return jsonify({'status': '200'}, {'red flag created': user_details}), 200
    else:
        return jsonify({'error': '400', 'message': 'user ID already exists'.format(id)}), 400


# functions to edit images, videos, location from an incident
@app.route('/api/v1/interventions/<int:id>/images', methods=['PUT'])
def edit_image_for_intervention_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'intervention' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['images'] = request.json['images']
        return jsonify({'status': '200'}, {'intervention image edited for ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/red-flags/<int:id>/images', methods=['PUT'])
def edit_image_for_red_flag_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'red flag' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['images'] = request.json['images']
        return jsonify({'status': '200'}, {'red flag image edited for ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/interventions/<int:id>/videos', methods=['PUT'])
def edit_video_for_intervention_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'intervention' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['videos'] = request.json['videos']
        return jsonify({'status': '200'}, {'intervention video edited for ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/red-flags/<int:id>/videos', methods=['PUT'])
def edit_video_for_red_flag_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'red flag' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['videos'] = request.json['videos']
        return jsonify({'status': '200'}, {'red flag video edited for ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/interventions/<int:id>/locations', methods=['PUT'])
def edit_location_for_intervention_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'intervention' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['location'] = request.json['location']
        return jsonify({'status': '200'}, {'intervention location edited for ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/red-flags/<int:id>/locations', methods=['PUT'])
def edit_location_for_red_flag_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'red flag' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['location'] = request.json['location']
        return jsonify({'status': '200'}, {'red flag location edited for ID '+str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/interventions/<int:id>/comments', methods=['PUT'])
def edit_comment_for_intervention_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'intervention' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['comment'] = request.json['comment']
        return jsonify({'status': '200'}, {'intervention comment edited for ID ' + str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/red-flags/<int:id>/comments', methods=['PUT'])
def edit_comment_for_red_flag_by_id(id):
    incident_details = [details for details in incident if details['type'] == 'red flag' and details['id'] == id]
    if len(incident_details) != 0:
        incident_details[0]['comment'] = request.json['comment']
        return jsonify({'status': '200'}, {'red flag comment edited for ID ' + str(id): incident_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


# functions to edit email, phone number from a user
@app.route('/api/v1/users/<int:id>/emails', methods=['PUT'])
def edit_email_for_user_by_id(id):
    user_details = [details for details in users if details['id'] == id]
    if len(user_details) != 0:
        user_details[0]['email'] = request.json['email']
        return jsonify({'status': '200'}, {'user email edited for ID ' + str(id): user_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/users/<int:id>/phonenumbers', methods=['PUT'])
def edit_phonenumber_for_user_by_id(id):
    user_details = [details for details in users if details['id'] == id]
    if len(user_details) != 0:
        user_details[0]['phonenumber'] = request.json['phonenumber']
        return jsonify({'status': '200'}, {'user phone number edited for ID ' + str(id): user_details}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


# functions to delete an incident or user
@app.route('/api/v1/red-flags/<int:id>', methods=['DELETE'])
def delete_red_flag_by_id(id):
    incident_details = [incidents for incidents in incident
                        if incidents['id'] == id and incidents['type'] == 'red flag']
    if len(incident_details) != 0:
        incident.remove(incident_details[0])
        return jsonify({'status': '200'}, {'red flag details deleted for ID ': str(id)}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/interventions/<int:id>', methods=['DELETE'])
def delete_intervention_by_id(id):
    incident_details = [incidents for incidents in incident
                        if incidents['id'] == id and incidents['type'] == 'intervention']
    if len(incident_details) != 0:
        incident.remove(incident_details[0])
        return jsonify({'status': '200'}, {'intervention details deleted for ID ': str(id)}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


@app.route('/api/v1/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    user_details = [user for user in users if user['id'] == id]
    if len(user_details) != 0:
        users.remove(user_details[0])
        return jsonify({'status': '200'}, {'user details deleted for ID ': str(id)}), 200
    return jsonify({'error': '404', 'message': 'no details exist for ID selected '}), 404


if __name__ == '__main__':
    app.run(debug=True)
