from django.test import TestCase
from main.models import Video

# from unittest import TestCase


class VideosTest(TestCase):
    def setUp(self):
        self.video = Video.objects.create(name='AVM 29', link="https://www.youtube.com/watch?v=TF9I1GxNdJQ", watch="TF9I1GxNdJQ")
        
    def test_context(self):
        resp = self.client.get("/videos/")
        self.assertTrue('videos' in resp.context)
        resp = self.client.get("/videos/1/")
        self.assertTrue('video' in resp.context)
    
    def tearDown(self) -> None:
        self.video.delete()