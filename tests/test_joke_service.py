#!/usr/bin/env python3
"""
Unit tests for Joke Generator
"""

import pytest
from unittest.mock import patch, MagicMock
from src.joke_service import JokeService


class TestJokeService:
    """Test cases for JokeService"""
    
    @pytest.fixture
    def service(self):
        """Create a JokeService instance for testing"""
        return JokeService()
    
    @patch('requests.get')
    def test_get_random_joke_success(self, mock_get, service):
        """Test successful joke retrieval"""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'setup': 'Why did the programmer quit his job?',
            'delivery': 'Because he did not get arrays.'
        }
        mock_get.return_value = mock_response
        
        joke = service.get_random_joke()
        
        assert joke is not None
        assert 'setup' in joke or 'joke' in joke
    
    @patch('requests.get')
    def test_get_random_joke_failure(self, mock_get, service):
        """Test failed joke retrieval"""
        mock_get.side_effect = Exception("Network error")
        
        joke = service.get_random_joke()
        
        assert joke is None
    
    def test_parse_official_joke_valid(self, service):
        """Test parsing valid Official Joke API response"""
        data = {
            'setup': 'Why did the programmer quit his job?',
            'delivery': 'Because he did not get arrays.'
        }
        
        parsed = service.parse_official_joke(data)
        
        assert parsed is not None
        assert parsed['type'] == 'Two-liner'
        assert parsed['setup'] == data['setup']
        assert parsed['delivery'] == data['delivery']
    
    def test_parse_official_joke_invalid(self, service):
        """Test parsing invalid Official Joke API response"""
        data = {'incomplete': 'data'}
        
        parsed = service.parse_official_joke(data)
        
        assert parsed is None
    
    def test_parse_ninja_joke_valid(self, service):
        """Test parsing valid Joke Ninja API response"""
        data = {'joke': 'Why did the programmer quit his job? Because he did not get arrays.'}
        
        parsed = service.parse_ninja_joke(data)
        
        assert parsed is not None
        assert parsed['type'] == 'Single-liner'
        assert parsed['joke'] == data['joke']
    
    def test_parse_ninja_joke_invalid(self, service):
        """Test parsing invalid Joke Ninja API response"""
        data = {'incomplete': 'data'}
        
        parsed = service.parse_ninja_joke(data)
        
        assert parsed is None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
