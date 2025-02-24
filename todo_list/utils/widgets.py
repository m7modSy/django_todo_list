from django.forms import RadioSelect

class CustomRadioSelect(RadioSelect):
    template_name = "base/radio.html"