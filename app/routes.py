from flask import Blueprint, request, jsonify
from app import db
from app.models import Client


tracker = Blueprint('tracker', __name__)


@tracker.route('/', methods=['GET'])
def get_clients():
    clients = Client.query.filter(Client.deleted_at.is_(None)).all()
    return jsonify([client.to_dict() for client in clients])


@tracker.route('/<int:id_>', methods=['GET'])
def get_client_by_id(id_):
    client = Client.query.get_or_404(id_)
    return jsonify(client.to_dict())


@tracker.route('/', methods=['POST'])
def create_client():
    data = request.get_json()
    client_name = data.get('client_name')
    client_company = data.get('client_company')
    client_location = data.get('client_location')
    contact_person = data.get('contact_person')
    contact_number = data.get('contact_number')
    contact_email = data.get('contact_email')

    if (not client_name or not client_company or not client_location or not contact_person or
            not contact_number or not contact_email):
        return jsonify({"error": "Missing field, please fill all fields"}), 400

    client = Client(client_name=client_name,
                    client_company=client_company,
                    client_location=client_location,
                    contact_person=contact_person,
                    contact_number=contact_number,
                    contact_email=contact_email)

    db.session.add(client)
    db.session.commit()
    return jsonify(client.to_dict()), 201


@tracker.route('/<int:id_>', methods=['PUT'])
def update_client(id_):
    client = Client.query.get_or_404(id_)
    data = request.get_json()
    client.contact_person = data.get('contact_person', client.contact_person)
    client.contact_number = data.get('contact_number', client.contact_number)
    client.contact_email = data.get('contact_email', client.contact_email)

    from datetime import datetime, timezone
    client.updated_at = datetime.now(timezone.utc)
    db.session.commit()
    return jsonify(client.to_dict())


@tracker.route('<int:id_>', methods=['DELETE'])
def delete_client(id_):
    from datetime import datetime, timezone
    client = Client.query.get_or_404(id_)
    client.deleted_at = datetime.now(timezone.utc)
    client.updated_at = datetime.now(timezone.utc)
    db.session.commit()
    return jsonify({'message': 'Client information deleted successfully'})
