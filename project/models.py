from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse

#db table for veroff_typveroff
class Publication(models.Model):
    #publication_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=22)
    publication_id=models.AutoField(primary_key=True)
    publication_type = models.CharField(max_length=100)


    def __str__(self):
        return self.publication_type

#Veroeff_Hochwertig
class HighQuality(models.Model):
    #quality_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=22)
    quality_id= models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)


    def __str__(self):
        return self.type

#Veroeff_Status
class Status(models.Model):
    #status_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=22)
    status_id=models.AutoField(primary_key=True)
    status_text = models.CharField(max_length=250)

    def __str__(self):
        return self.status_text
#db table for mitarbeiter



class Planning(models.Model):
    user = models.ForeignKey(User, default=1)
    #planning_id = models.DecimalField(primary_key=True, decimal_places=0, max_digits=22)
    planning_id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.ForeignKey(Publication,db_column="publication_id", blank=False, null=False)
    quality=models.ForeignKey(HighQuality, db_column="quality_id", blank=False, null=False)
    medium=models.CharField(max_length=100)
    planned_date=models.DateTimeField()
    #verilen bölüm baskani BL(direct chef)
    bl=models.CharField(max_length=100)
    applied_date=models.DateTimeField()
    status=models.ForeignKey(Status,db_column="status_id", null=False)
    notes=models.CharField(max_length=250)
    is_AL = models.BooleanField(default=False)
    is_BL =  models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('project/detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

# bereich
class StudyField(models.Model):
    study_id = models.AutoField(primary_key=True)
    study_field = models.CharField(max_length=100)


# hauptabteilung
class HeadDepartment(models.Model):
    head_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    study_field = models.ForeignKey(StudyField, db_column="study_id", blank=False, null=False)
# abteilung
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100)
    head_department = models.ForeignKey(HeadDepartment, db_column="head_id", blank=False, null=False)
    # ITA_mitarbeiter
class ITA_Employee(models.Model):
    ita_employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, db_column="department_id", blank=False, null=False)
    funktion = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    status = models.CharField(max_length=100)
class PaperEmployee(models.Model):
    paper_employee_id = models.AutoField(primary_key=True)
    paper_id = models.ForeignKey(Planning, db_column="planning_id", blank=False, null=False)
    #paper_employee = models.ForeignKey(ITA_Employee, db_column="ita_employee_id", blank=False, null=False)
    # status=
    factor = models.IntegerField()

#mitarbeiter_status
class PublicationEmployee_Status(models.Model):
    emp_status_id=models.ForeignKey(PaperEmployee,db_column="paper_employee_id",blank=False,null=False)
    status=models.CharField(max_length=100)












