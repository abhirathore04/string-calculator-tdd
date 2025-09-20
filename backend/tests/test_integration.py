"""
Complete Integration Tests for String Calculator Frontend-Backend
Tests to verify frontend gets proper results from backend API
"""

import pytest
import json
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestFrontendBackendIntegration:
    """Complete integration tests for frontend-backend communication."""
    
    def setup_method(self):
        """Set up test fixtures before each test."""
        from src.api import app
        self.app = app
        self.client = app.test_client()
        self.app.config['TESTING'] = True
    
    # ===== API ENDPOINT VALIDATION =====
    
    def test_api_health_check(self):
        """Test: API health endpoint is working"""
        response = self.client.get('/api/health')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert data['service'] == 'String Calculator API'
    
    def test_api_root_endpoint(self):
        """Test: Root endpoint provides API information"""
        response = self.client.get('/')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'message' in data
        assert 'endpoints' in data
    
    # ===== CORE FUNCTIONALITY TESTS =====
    
    def test_empty_string_via_api(self):
        """Test: Empty string returns 0 via API"""
        response = self.client.post('/api/add',
                                  json={'numbers': ''},
                                  content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 0
        assert data['input'] == ''
        assert data['success'] is True
    
    def test_single_numbers_via_api(self):
        """Test: Single numbers return themselves via API"""
        test_cases = [
            ('1', 1),
            ('42', 42),
            ('0', 0),
            ('123', 123)
        ]
        
        for input_str, expected in test_cases:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected
            assert data['input'] == input_str
            assert data['success'] is True
    
    def test_comma_separated_numbers_via_api(self):
        """Test: Comma-separated numbers return correct sum via API"""
        test_cases = [
            ('1,2', 3),
            ('1,2,3', 6),
            ('1,2,3,4', 10),
            ('10,20,30', 60)
        ]
        
        for input_str, expected in test_cases:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected, f"Failed for input: {input_str}"
            assert data['input'] == input_str
            assert data['success'] is True
    
    def test_newline_delimiters_via_api(self):
        """Test: Newline delimiters work correctly via API"""
        test_cases = [
            ('1\n2', 3),
            ('1\n2\n3', 6),
            ('1\n2,3', 6),
            ('10\n20', 30)
        ]
        
        for input_str, expected in test_cases:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected, f"Failed for input: {input_str}"
            assert data['success'] is True
    
    def test_custom_delimiters_via_api(self):
        """Test: Custom delimiters work correctly via API"""
        test_cases = [
            ('//;\n1;2', 3),
            ('//;\n1;2;3', 6),
            ('//*\n1*2*3', 6),
            ('//|\n1|2|3|4', 10)
        ]
        
        for input_str, expected in test_cases:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected, f"Failed for input: {input_str}"
            assert data['success'] is True
    
    def test_multi_character_delimiters_via_api(self):
        """Test: Multi-character custom delimiters work via API"""
        test_cases = [
            ('//[***]\n1***2***3', 6),
            ('//[sep]\n1sep2sep3', 6),
            ('//[::]\n10::20::30', 60)
        ]
        
        for input_str, expected in test_cases:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected, f"Failed for input: {input_str}"
            assert data['success'] is True
    
    def test_multiple_delimiters_via_api(self):
        """Test: Multiple custom delimiters work via API"""
        test_cases = [
            ('//[*][%]\n1*2%3', 6),
            ('//[**][%%]\n1**2%%3', 6),
            ('//[*][%][!]\n1*2%3!4', 10)
        ]
        
        for input_str, expected in test_cases:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected, f"Failed for input: {input_str}"
            assert data['success'] is True
    
    # ===== ERROR HANDLING TESTS =====
    
    def test_api_missing_numbers_field(self):
        """Test: API handles missing numbers field properly"""
        response = self.client.post('/api/add',
                                  json={},
                                  content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert data['success'] is False
        assert 'Missing required field: numbers' in data['error']
    
    def test_api_invalid_content_type(self):
        """Test: API handles invalid content type"""
        response = self.client.post('/api/add',
                                  data='invalid',
                                  content_type='text/plain')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert data['success'] is False
    
    def test_api_invalid_json(self):
        """Test: API handles invalid JSON gracefully"""
        response = self.client.post('/api/add',
                                  data='{"invalid": json}',
                                  content_type='application/json')
        
        # Accept any error response (Flask may return 400 or 500 for invalid JSON)
        assert response.status_code >= 400
        assert response.status_code < 600
    
    # ===== EDGE CASES =====
    
    def test_edge_cases_via_api(self):
        """Test: Edge cases work properly via API"""
        test_cases = [
            ('1,,2', 3),        # Double comma
            ('1\n\n2', 3),      # Double newline  
            (',1,2,', 3),       # Leading/trailing comma
            ('//;\n5', 5),      # Single number with custom delimiter
        ]
        
        for input_str, expected in test_cases:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected, f"Failed for input: {input_str}"
            assert data['success'] is True
    
    # ===== PERFORMANCE TESTS =====
    
    def test_api_response_time(self):
        """Test: API responds within acceptable time"""
        import time
        
        start_time = time.time()
        response = self.client.post('/api/add',
                                  json={'numbers': '1,2,3,4,5,6,7,8,9,10'},
                                  content_type='application/json')
        end_time = time.time()
        
        assert response.status_code == 200
        response_time = end_time - start_time
        assert response_time < 1.0  # Should respond within 1 second
    
    def test_large_input_handling(self):
        """Test: API handles large inputs properly"""
        # Create large input with 50 numbers
        large_input = ','.join(str(i) for i in range(1, 51))
        expected_result = sum(range(1, 51))  # 1275
        
        response = self.client.post('/api/add',
                                  json={'numbers': large_input},
                                  content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == expected_result
        assert data['success'] is True
    
    def test_frontend_example_cases_via_api(self):
        """Test: All frontend example cases work via API"""
        frontend_examples = [
            ('', 0),                           # Empty string
            ('42', 42),                        # Single number
            ('1,2,3', 6),                      # Comma separated
            ('1\n2\n3', 6),                    # Newline separated
            ('1\n2,3', 6),                     # Mixed delimiters
            ('//;\n1;2;3', 6),                 # Custom delimiter
            ('//[***]\n1***2***3', 6),         # Multi-char delimiter
            ('//[*][%]\n1*2%3', 6),           # Multiple delimiters
        ]
        
        for input_str, expected in frontend_examples:
            response = self.client.post('/api/add',
                                      json={'numbers': input_str},
                                      content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['result'] == expected, f"Failed for: '{input_str}'"
            assert data['success'] is True
