from projects.models import Project
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "owner",
        )
