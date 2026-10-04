"""
Counter Service

This microservice provides a simple hit counter using Redis as the backend store.
"""

from flask import Flask, jsonify, abort
import os
import logging

# Create Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

COUNTER = {}


############################################################
# Health Endpoint
############################################################
@app.route("/health")
def health():
    """Health endpoint"""
    return jsonify({"status": "OK"}), 200


############################################################
# Index page
############################################################
@app.route("/")
def index():
    """Root URL response"""
    logger.info("Request for Root URL")
    return jsonify(
        name="Hit Counter REST API Service",
        version="1.0",
        description="A simple counter service built with Flask and Redis",
    ), 200


############################################################
# List all counters
############################################################
@app.route("/counters", methods=["GET"])
def list_counters():
    """List all counters"""
    logger.info("Request to list all counters")
    counters = [{"name": key, "counter": COUNTER[key]} for key in COUNTER]
    return jsonify(counters), 200


############################################################
# Create a counter
############################################################
@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a new counter"""
    logger.info("Request to create counter: %s", name)
    if name in COUNTER:
        abort(409, f"Counter {name} already exists")
    COUNTER[name] = 0
    return jsonify({"name": name, "counter": COUNTER[name]}), 201


############################################################
# Read a counter
############################################################
@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a single counter"""
    logger.info("Request to read counter: %s", name)
    if name not in COUNTER:
        abort(404, f"Counter {name} does not exist")
    return jsonify({"name": name, "counter": COUNTER[name]}), 200


############################################################
# Update a counter
############################################################
@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Update (increment) a counter"""
    logger.info("Request to update counter: %s", name)
    if name not in COUNTER:
        abort(404, f"Counter {name} does not exist")
    COUNTER[name] += 1
    return jsonify({"name": name, "counter": COUNTER[name]}), 200


############################################################
# Delete a counter
############################################################
@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter"""
    logger.info("Request to delete counter: %s", name)
    if name not in COUNTER:
        abort(404, f"Counter {name} does not exist")
    del COUNTER[name]
    return "", 204


############################################################
# Main entry point
############################################################
if __name__ == "__main__":
    logger.info("**** SERVICERUNNING ****")
    logger.info("Counter Service is running on port 8000")
    app.run(host="0.0.0.0", port=8000, debug=False)
