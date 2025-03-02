from django.db import models

class basemodel(models.model):
    uid=models.UUIDField(primary_key=True ,editable=False , default=uuid.uuid4)
    created_at =models.DateField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_add=True)

    class meta:
        abstract= True



