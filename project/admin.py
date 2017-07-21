from django.contrib import admin
from .models import Publication, Planning, HighQuality, Status,PaperEmployee, PublicationEmployee_Status,ITA_Employee,StudyField,HeadDepartment,Department

admin.site.register(Publication)
admin.site.register(Planning)
admin.site.register(HighQuality)
admin.site.register(Status)
admin.site.register(PaperEmployee)
admin.site.register(PublicationEmployee_Status)
admin.site.register(ITA_Employee)
admin.site.register(StudyField)
admin.site.register(HeadDepartment)
admin.site.register(Department)


