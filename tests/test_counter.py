"""
Unit Tests for the Counter Service
"""

import unittest
from app import app


class TestCounterService(unittest.TestCase):
    """Counter Service Tests"""

    def setUp(self):
        """Set up test fixtures"""
        self.client = app.test_client()
        # Reset counters before each test
        import app as counter_app
        counter_app.COUNTER.clear()

    def tearDown(self):
        """Tear down test fixtures"""
        pass

    # ----------------------------------------------------------
    # Test Health Endpoint
    # ----------------------------------------------------------
    def test_health(self):
        """It should return health status"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["status"], "OK")

    # ----------------------------------------------------------
    # Test Index Page
    # ----------------------------------------------------------
    def test_index(self):
        """It should return the index page"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn("Hit Counter", data["name"])

    # ----------------------------------------------------------
    # Test List Counters
    # ----------------------------------------------------------
    def test_list_counters(self):
        """It should return an empty list initially"""
        resp = self.client.get("/counters")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(len(data), 0)

    # ----------------------------------------------------------
    # Test Create Counter
    # ----------------------------------------------------------
    def test_create_counter(self):
        """It should create a new counter"""
        resp = self.client.post("/counters/foo")
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertEqual(data["name"], "foo")
        self.assertEqual(data["counter"], 0)

    def test_create_counter_conflict(self):
        """It should return 409 when counter already exists"""
        self.client.post("/counters/foo")
        resp = self.client.post("/counters/foo")
        self.assertEqual(resp.status_code, 409)

    # ----------------------------------------------------------
    # Test Read Counter
    # ----------------------------------------------------------
    def test_read_counter(self):
        """It should read a counter"""
        self.client.post("/counters/bar")
        resp = self.client.get("/counters/bar")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["name"], "bar")
        self.assertEqual(data["counter"], 0)

    def test_read_counter_not_found(self):
        """It should return 404 for unknown counter"""
        resp = self.client.get("/counters/unknown")
        self.assertEqual(resp.status_code, 404)

    # ----------------------------------------------------------
    # Test Update Counter
    # ----------------------------------------------------------
    def test_update_counter(self):
        """It should increment a counter"""
        self.client.post("/counters/hits")
        resp = self.client.put("/counters/hits")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["counter"], 1)

    def test_update_counter_not_found(self):
        """It should return 404 for unknown counter"""
        resp = self.client.put("/counters/unknown")
        self.assertEqual(resp.status_code, 404)

    # ----------------------------------------------------------
    # Test Delete Counter
    # ----------------------------------------------------------
    def test_delete_counter(self):
        """It should delete a counter"""
        self.client.post("/counters/temp")
        resp = self.client.delete("/counters/temp")
        self.assertEqual(resp.status_code, 204)

    def test_delete_counter_not_found(self):
        """It should return 404 for unknown counter"""
        resp = self.client.delete("/counters/unknown")
        self.assertEqual(resp.status_code, 404)


if __name__ == "__main__":
    unittest.main()
