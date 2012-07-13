import unittest
import vermonster

class VermonsterTestSuite(unittest.TestCase):
    """
    Vermonster test suite
    """
    def test_vermonster_entry_points(self):
        vermonster.Client

    def test_client_list_manager_exists(self):
        client = vermonster.Client(oauth_id='test', oauth_secret='test')
        client.lists

    def test_client_task_manager_exists(self):
        client = vermonster.Client(oauth_id='test', oauth_secret='test')
        client.tasks

    def test_initialize_client_oauth_id(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        self.assertEqual(client.oauth_id, 'test-oauth-id')

    def test_initialize_client_oauth_secret(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        self.assertEqual(client.oauth_secret, 'test-oauth-secret')

    def test_initialize_client_token_none(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        self.assertEqual(client.token, None)

    def test_initialize_client_token(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret', token='test-token')
        self.assertEqual(client.token, 'test-token')

    def test_initialize_client_connection(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        self.assertEqual(client.connection, 'https://api.cheddarapp.com')

    def test_initialize_client_oauth_id_none(self):
        with self.assertRaises(ValueError):
            vermonster.Client(None, oauth_secret='test-oauth-secret')

    def test_initialize_client_oauth_secret_none(self):
        with self.assertRaises(ValueError):
            vermonster.Client(oauth_id='test-oauth-id', oauth_secret=None)

    def test_initialize_client_oauth_id_empty(self):
        with self.assertRaises(ValueError):
            vermonster.Client('', oauth_secret='test-oauth-secret')

    def test_initialize_client_oauth_secret_empty(self):
        with self.assertRaises(ValueError):
            vermonster.Client(oauth_id='test-oauth-id', oauth_secret='')
