from flask import Blueprint
from controllers import ContactController

contact_bp = Blueprint('contacts', __name__)

# GET all contacts
@contact_bp.route('/contacts', methods=['GET'])
def get_contacts():
    return ContactController.get_all_contacts()

# GET single contact
@contact_bp.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    return ContactController.get_contact_by_id(contact_id)

# POST create contact
@contact_bp.route('/contacts', methods=['POST'])
def create_contact():
    return ContactController.create_contact()

# PUT update contact
@contact_bp.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    return ContactController.update_contact(contact_id)

# DELETE contact
@contact_bp.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    return ContactController.delete_contact(contact_id)