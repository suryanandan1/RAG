from django import forms


class SignupForm(forms.Form):
    employee_id = forms.CharField(
        label="Employee ID",
        max_length=50,
        required=True
    )

    name = forms.CharField(
        label="Full Name",
        max_length=100,
        required=True
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True
    )

    band = forms.ChoiceField(
        label="Band",
        required=True,
        choices=[
            ("9/10", "9/10"),
            ("7/8", "7/8"),
            ("5/6", "5/6"),
            ("1/2/3/4", "1/2/3/4"),
        ]
    )
