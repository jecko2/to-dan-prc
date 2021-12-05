from django.urls import path
from .views import (
        SignUpForm,
        home,
        CreateAssignmentInstance,
        )
urlpatterns = [
    path('', home, name='home'),
    path('assignment_upload/', CreateAssignmentInstance.as_view(), name="task-upload"),
    path('signup/', SignUpForm.as_view(), name="signup"),
]
