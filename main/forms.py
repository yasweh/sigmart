from django.forms import ModelForm
from main.models import AddItemEntry

class AddItemForm(ModelForm):
    class Meta:
        model = AddItemEntry
        fields = ["item_name", "description", "type", "price"]