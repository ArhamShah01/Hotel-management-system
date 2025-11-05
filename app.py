#!/usr/bin/env python3
"""
Hotel Management System - Flask Backend Server
This is an optional backend for enhanced functionality
Run: python app.py
Then open: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import json
import csv
import os
from datetime import datetime
from io import StringIO

app = Flask(__name__)
CORS(app)

# Data file
DATA_FILE = 'customers.json'

def load_customers():
    """Load customers from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_customers(customers):
    """Save customers to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(customers, f, indent=2)

@app.route('/')
def index():
    """Serve the HTML file"""
    return send_file('hotel-management.html')

@app.route('/api/customers', methods=['GET'])
def get_customers():
    """Get all customers"""
    return jsonify(load_customers())

@app.route('/api/customers', methods=['POST'])
def add_customer():
    """Add new customer"""
    customers = load_customers()
    new_customer = request.json
    customers.append(new_customer)
    save_customers(customers)
    return jsonify({'status': 'success', 'customer': new_customer})

@app.route('/api/customers/<code>', methods=['GET'])
def get_customer(code):
    """Get specific customer"""
    customers = load_customers()
    customer = next((c for c in customers if c['code'] == code), None)
    if customer:
        return jsonify(customer)
    return jsonify({'error': 'Customer not found'}), 404

@app.route('/api/customers/<code>', methods=['DELETE'])
def delete_customer(code):
    """Delete customer"""
    customers = load_customers()
    customers = [c for c in customers if c['code'] != code]
    save_customers(customers)
    return jsonify({'status': 'success'})

@app.route('/api/customers/<code>', methods=['PUT'])
def update_customer(code):
    """Update customer"""
    customers = load_customers()
    for i, customer in enumerate(customers):
        if customer['code'] == code:
            customers[i].update(request.json)
            save_customers(customers)
            return jsonify({'status': 'success', 'customer': customers[i]})
    return jsonify({'error': 'Customer not found'}), 404

@app.route('/api/export-csv', methods=['GET'])
def export_csv():
    """Export customers as CSV"""
    customers = load_customers()
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=['code', 'name', 'idType', 'contact', 'roomNumber', 'checkin', 'checkout'])
    writer.writeheader()
    for customer in customers:
        writer.writerow({
            'code': customer['code'],
            'name': customer['name'],
            'idType': customer['idType'],
            'contact': customer['contact'],
            'roomNumber': customer['roomNumber'],
            'checkin': customer['checkin'],
            'checkout': customer['checkout']
        })
    return output.getvalue(), 200, {'Content-Disposition': 'attachment; filename=customers.csv'}

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics"""
    customers = load_customers()
    total_revenue = sum(c['billDetails']['grandTotal'] for c in customers)
    return jsonify({
        'total_customers': len(customers),
        'total_revenue': total_revenue,
        'average_bill': total_revenue / len(customers) if customers else 0
    })

if __name__ == '__main__':
    print("Hotel Management System - Flask Backend")
    print("Starting server on http://localhost:5000")
    print("Press Ctrl+C to stop")
    app.run(debug=True, port=5000)