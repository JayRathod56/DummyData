import json
from time import sleep
from django.http import StreamingHttpResponse
from django.views import View


class TestJsonRead(View):
    def stream_response(self):
        """Generator function to yield JSON data one by one"""
        try:
            with open("api/data.txt", "r") as file:
                data = json.load(file)  # Load list of JSON objects

            for item in data:  # Iterate through list
                # print(item)
                # sleep(5)
                yield json.dumps(item) + "\n"  # Send one item at a time
                sleep(5)  # Wait 2 seconds before sending the next

        except Exception as e:
            yield json.dumps({"error": str(e)}) + "\n"

    def get(self, request):
        """Return streaming response"""
        return StreamingHttpResponse(self.stream_response(), content_type="application/json")
