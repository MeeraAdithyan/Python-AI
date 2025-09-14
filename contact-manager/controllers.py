# Controllers - Business logic, validation, database operations
from flask import request, jsonify
from models import db, Contact
from sqlalchemy import or_
import re

class ContactController:    
    @staticmethod
    def validate_contact(data):
        errors = []
        
        if not data.get('name'):
            errors.append('Name is required')
        if not data.get('email'):
            errors.append('Email is required')
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
            errors.append('Invalid email')
        if not data.get('phone'):
            errors.append('Phone is required')
        
        return len(errors) == 0, errors
    
    @staticmethod
    def get_all_contacts():
        try:
            contacts = Contact.query.all()
            contacts_list = [contact.to_dict() for contact in contacts]
            return jsonify({'data': contacts_list, 'count': len(contacts_list)}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def get_contact_by_id(contact_id):
        try:
            contact = Contact.query.get(contact_id)
            if not contact:
                return jsonify({'error': 'Contact not found'}), 404
            return jsonify({'data': contact.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def create_contact():
        try:
            data = request.get_json()
            
            is_valid, errors = ContactController.validate_contact(data)
            if not is_valid:
                return jsonify({'errors': errors}), 400
            
            contact = Contact(
                name=data['name'],
                phone=data['phone'],
                email=data['email']
            )
            
            db.session.add(contact)
            db.session.commit()
            
            return jsonify({'data': contact.to_dict(), 'message': 'Contact created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def update_contact(contact_id):
        try:
            contact = Contact.query.get(contact_id)
            if not contact:
                return jsonify({'error': 'Contact not found'}), 404
            
            data = request.get_json()
            is_valid, errors = ContactController.validate_contact(data)
            if not is_valid:
                return jsonify({'errors': errors}), 400
            
            contact.name = data['name']
            contact.phone = data['phone']
            contact.email = data['email']
            contact.updated_at = db.func.now()
            
            db.session.commit()
            
            return jsonify({'data': contact.to_dict(), 'message': 'Contact updated'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def delete_contact(contact_id):
        try:
            contact = Contact.query.get(contact_id)
            if not contact:
                return jsonify({'error': 'Contact not found'}), 404
            
            db.session.delete(contact)
            db.session.commit()
            
            return jsonify({'message': 'Contact deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    