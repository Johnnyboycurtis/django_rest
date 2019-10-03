from django import forms


class FirstListForm(forms.Form):
    form_choices = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('', 'All')]
    form_type = forms.ChoiceField(label = "Form Type", choices=form_choices, required=True, help_text = 'Select a form type')
    