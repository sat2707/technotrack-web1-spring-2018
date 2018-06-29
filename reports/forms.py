from django import forms
from reports.models import Answer, Report, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CreateReport (forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'text', 'priority', 'type', 'level', 'status', 'labels', 'assigned_to']

    def __init__(self, *args, **kwargs):
        super(CreateReport, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))


class CreateAnswer (forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['prev_ans', 'text']

    def __init__(self, *args, **kwargs):
        super(CreateAnswer, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))


class ChangeStatus (forms.ModelForm):
    class Meta:
        model = Report
        fields = ['status', 'level', 'priority', 'type']

