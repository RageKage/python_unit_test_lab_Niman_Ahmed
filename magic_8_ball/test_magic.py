""" TODO create a test case to test each of the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question.

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API,
 and check that the function returns None.


 TODO to think about - what else could you test about this program?
 What types of expected and unexpected behavior might happen? You may be able to write tests for some
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""

import unittest
from unittest import TestCase

import requests

import functions_magic


class TestFunctionsMagicBall(TestCase):

    def test_no_internet_connection(self):
        # TODO how can you test the case where there is no internet connection?

        try:
            response = requests.get('https://www.google.com')
            if response.status_code == 200:
                self.assertEqual(response.status_code, 200)
        except requests.exceptions.ConnectionError:
            self.assertEqual(response.status_code, 404)
            
    def test_generate_url_for_question(self):
        # TODO test that the expected URL is returned for an example question.
        question = 'Will it be sunny tomorrow?'
        url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'
        self.assertEqual(functions_magic.generate_url_for_question(question), url)
        
    def test_extract_answer_from_response(self):
        # TODO test that the correct answer is extracted and returned.
        response = {
            'question': 'Will it be sunny tomorrow?', 
            'answer': 'Yes', 
            'type': 'Affirmative'
        }
        self.assertEqual(functions_magic.extract_answer_from_response(response), 'Yes')
        response = {
            'question': 'Will it be sunny tomorrow?', 
            'answer': 'Yes', 
        }
        self.assertEqual(functions_magic.extract_answer_from_response(response), None)
        response = {
            'question': 'Will it be sunny tomorrow?', 
            'answer': 'Yes', 
            'type': 'Affirmative',
            'extra': 'extra'
        }
        self.assertEqual(functions_magic.extract_answer_from_response(response), None)
    
if __name__ == "__main__":
    unittest.main()
