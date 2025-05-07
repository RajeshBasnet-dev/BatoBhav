from django.db import models

class PredictionHistory(models.Model):
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    city = models.CharField(max_length=100)
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - NPR {self.predicted_price}"

class UserFeedback(models.Model):
    prediction = models.ForeignKey(PredictionHistory, on_delete=models.CASCADE, null=True)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.prediction.city}"