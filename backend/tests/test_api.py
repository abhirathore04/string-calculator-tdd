"""
Test cases for String Calculator API following TDD approach.

Step 5: REST API for React frontend integration
"""

import pytest
import json
from unittest.mock import Mock
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestStringCalculatorAPI:
    """Test suite for String Calculator API endpoints."""
    
    def setup_method(self):
        """Set up test fixtures before each test."""
        # We'll create the Flask app in GREEN phase
        pass
    
    # ===== STEP 5A: BASIC API ENDPOINT (NEW - RED PHASE) =====
    def test_api_add_endpoint_with_valid_input(self):
        """
        RED PHASE - TDD Cycle 9
        
        Test: POST /api/add endpoint with valid input
        Expected: WILL FAIL - API doesn't exist yet
        """
        # This test will fail until we create the Flask app
        from src.api import app
        
        client = app.test_client()
        
        # Test basic comma-separated numbers
        response = client.post('/api/add', 
                             json={'numbers': '1,2,3'},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 6
        assert data['input'] == '1,2,3'
        assert 'success' in data
        assert data['success'] is True
    
    def test_api_add_endpoint_with_custom_delimiters(self):
        """Test API with custom delimiters"""
        from src.api import app
        
        client = app.test_client()
        
        # Test custom delimiter
        response = client.post('/api/add',
                             json={'numbers': '//;\n1;2;3'},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 6
        assert data['input'] == '//;\n1;2;3'
    
    def test_api_add_endpoint_with_empty_input(self):
        """Test API with empty input"""
        from src.api import app
        
        client = app.test_client()
        
        response = client.post('/api/add',
                             json={'numbers': ''},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 0
        assert data['input'] == ''
    
    def test_api_error_handling(self):
        """Test API error handling for invalid input"""
        from src.api import app
        
        client = app.test_client()
        
        # Test missing numbers field
        response = client.post('/api/add',
                             json={},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert data['success'] is False
