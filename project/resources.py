from import_export.resources import ModelResource 


class ProjectUserResource(ModelResource):
    class Meta:
        model = ProjectUser 
        exclude = []

