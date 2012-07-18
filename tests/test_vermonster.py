import unittest
import vermonster
import json
from vermonster.models import ListManager


class VermonsterClientTestSuite(unittest.TestCase):
    """
    Vermonster client test suite
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

    def test_initialize_client_oauth_id_wrong_type(self):
        with self.assertRaises(ValueError):
            vermonster.Client(oauth_id=0, oauth_secret='test-oauth-secret')

    def test_initialize_client_oauth_secret_wrong_type(self):
        with self.assertRaises(ValueError):
            vermonster.Client(oauth_id='test-oauth-id', oauth_secret=0)

    def test_initialize_client_token_none(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        self.assertEqual(client.token, None)

    def test_initialize_client_token_wrong_type(self):
        with self.assertRaises(ValueError):
            vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret', token=0)

    def test_initialize_client_token(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret', token='test-token')
        self.assertEqual(client.token, 'test-token')

    def test_initialize_client_connection(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        self.assertEqual(client.connection, 'https://api.cheddarapp.com')


class VermonsterListManagerTestSuite(unittest.TestCase):
    """
    Vermonster list manager test suite
    """
    def test_initialize_list_manager_client_null(self):
        with self.assertRaises(ValueError):
            ListManager(client=None)

    def test_initialize_list_manager_client_wrong_type(self):
        with self.assertRaises(ValueError):
            ListManager(client='some kinda string?')

    def test_initialize_list_manager_client(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        self.assertEqual(manager.client, client)

    def test_list_manager__get_authorization_header(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        headers = manager._get_authorization_headers()
        self.assertEqual(headers, {'Authorization': 'Bearer %s' % client.token})

    def test_list_manager__get_request_url_all(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        url = manager._get_request_url_all()
        self.assertEqual(url, '%s/v1/lists' % client.connection)

    def test_list_manager__get_lists_from_json_json_string_none(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        lists = manager._get_lists_from_json(None, include_archived=True)
        self.assertEqual(len(lists), 0)

    def test_list_manager__get_lists_from_json_json_string_empty(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        lists = manager._get_lists_from_json('', include_archived=True)
        self.assertEqual(len(lists), 0)

    def test_list_manager__get_lists_from_json_json_string_wrong_type(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        with self.assertRaises(ValueError):
            manager._get_lists_from_json(034, include_archived=True)

    def test_list_manager__get_lists_from_json_include_archived_none(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[]')
        with self.assertRaises(ValueError):
            manager._get_lists_from_json(json_string, include_archived=None)

    def test_list_manager__get_lists_from_json_include_archived_wrong_type(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[]')
        with self.assertRaises(ValueError):
            manager._get_lists_from_json(json_string, include_archived=0)

    def test_list_manager__get_lists_from_json_no_items(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[]')
        lists = manager._get_lists_from_json(json_string, include_archived=True)
        self.assertEqual(len(lists), 0)

    def test_list_manager__get_lists_from_json_one_item(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": "2012-06-29T17:38:09Z","title": "Test 1"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=True)
        self.assertEqual(len(lists), 1)

    def test_list_manager__get_lists_from_json_archived_at(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": "2012-06-29T17:38:09Z","title": "Test 1"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=True)
        self.assertEqual(lists[0].archived_at, '2012-06-29T17:38:09Z')

    def test_list_manager__get_lists_from_json_title(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": "2012-06-29T17:38:09Z","title": "Test 1"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=True)
        self.assertEqual(lists[0].title, 'Test 1')

    def test_list_manager__get_lists_from_json_multiple_items(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": "2012-06-29T17:38:09Z","title": "Test 1"}, {"archived_at": "2012-06-29T17:38:09Z","title": "Test 2"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=True)
        self.assertEqual(len(lists), 2)

    def test_list_manager__get_lists_from_json_check_client_exists(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": "2012-06-29T17:38:09Z","title": "Test 1"}, {"archived_at": "2012-06-29T17:38:09Z","title": "Test 2"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=True)
        self.assertEqual(lists[0].client, client)

    def test_list_manager__get_lists_from_json_exclude_archived_no_archived_items(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": null,"title": "Test 1"}, {"archived_at": null,"title": "Test 2"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=False)
        self.assertEqual(len(lists), 2)

    def test_list_manager__get_lists_from_json_exclude_archived_archived_items(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": "2012-06-29T17:38:09Z","title": "Test 1"}, {"archived_at": null,"title": "Test 2"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=False)
        self.assertEqual(len(lists), 1)

    def test_list_manager__get_lists_from_json_exclude_archived_archived_items_correct(self):
        client = vermonster.Client(oauth_id='test-oauth-id', oauth_secret='test-oauth-secret')
        manager = ListManager(client=client)
        json_string = json.loads('[{"archived_at": "2012-06-29T17:38:09Z","title": "Test 1"}, {"archived_at": null,"title": "Test 2"}]')
        lists = manager._get_lists_from_json(json_string, include_archived=False)
        self.assertEqual(lists[0].title, 'Test 2')
