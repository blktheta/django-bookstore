from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


"""
Update the built-in admin forms too point to CustomUser instead
of the default User model via get_user_model() from AUTH_USER_MODEL
config in settengs.py.


Extend the base user form with CustomUser model. Display email and
username fields, password field is implicitly included by default.
"""


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
