from django.test import Client, TestCase

class HelloWorldTest(TestCase):
    
  def test_reachable(self):
    #given
    client = Client()

    #when 
    response = client.get("/hello_world/")

    #then 
    self.assertEqual(200, response.status_code)

  def test_hello_world(self):

    client = Client()
    response = client.get("/hello_world/")
    self.assertIn("Hello world !", str(response.content))