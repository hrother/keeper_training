from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div
from crispy_forms.layout import Field
from crispy_forms.layout import HTML
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django import forms

from keeper_training.training_sessions.models import TrainingSession


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ("date", "drills")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "id-trainingsessionForm"
        self.helper.form_class = "form"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("date"),
            HTML("<p>Drills</p>"),
            Div(
                HTML(
                    "{% if not ordered_drills %}"
                    "</br>"
                    "{% endif %}"
                    "{% for drill in ordered_drills %}"
                    "<div class='col mb-4' data-id='{{drill.pk}}'>"
                    "{% include 'drills/_drill_small.html' %}"
                    "</div>"
                    "{% endfor %}"
                ),
                id="selected-drills",
                css_class="row row-cols-1 row-cols-md-2 bg-light m-3",
            ),
            Field("drills", css_class="d-none", wrapper_class="d-none"),
        )
        self.helper.add_input(Submit("submit", "Submit"))
