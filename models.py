from django.db import models

class SupportRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
