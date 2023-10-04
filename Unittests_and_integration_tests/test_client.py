#!/usr/bin/env python3
"""test file for client module"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """test class for GithubOrgClient"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, test_org_name, mock_get_json):
        """test to make sure org returns correct value"""
        fake_org_client = GithubOrgClient(test_org_name)
        self.assertEqual(fake_org_client.org, {"payload": True})
        fake_json_arg = f"https://api.github.com/orgs/{test_org_name}"
        mock_get_json.assert_called_once_with(fake_json_arg)

    def test_public_repos_url(self):
        """test method for _public_repos_url property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            test_payload = {
                "repos_url": "https://api.github.com/orgs/fakey/repos"
                }
            mock_org.return_value = test_payload
            fake_org_client = GithubOrgClient("fakey")
            self.assertEqual(
                fake_org_client._public_repos_url,
                test_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test for public_repos, that it returns expected list"""
        test_payload = [{"name": "ll_cool_repo"}, {"name": "mc_repo_alot"}]
        mock_get_json.return_value = test_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/faker/repos"
            fake_org_client = GithubOrgClient("faker")
            results = fake_org_client.public_repos()
            self.assertEqual(results, ["ll_cool_repo", "mc_repo_alot"])
            mock_get_json.assert_called_once()
            mock_url.asert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, test_repo, test_license_key, expected):
        """tests has_license"""
        result = GithubOrgClient.has_license(test_repo, test_license_key)
        self.assertEqual(result, expected)
