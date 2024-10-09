from django.forms import ModelForm
from main.models import AddItemEntry
from django.utils.html import strip_tags

class AddItemForm(ModelForm):
    class Meta:
        model = AddItemEntry
        fields = ["item_name", "description", "type", "price"]
    
    def clean_item_name(self):
        item_name = self.cleaned_data["item_name"]
        return strip_tags(item_name)

    def clean_feelings(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)