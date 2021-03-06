from django.db import models

# Create your models here.

class User(models.Model):
	UserName = models.CharField(max_length=50)
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	Password = models.CharField(max_length=1000)
	Created = models.DateTimeField()
	Modified = models.DateTimeField()

class UserSettings(models.Model):
	UserID = models.ForeignKey(User)
	isAdmin = models.BooleanField(default=False)
		
class UserBadge(models.Model):
	UserID = models.ForeignKey(User)
	BadgeID = models.IntegerField()	

class Question(models.Model):
	UserID= models.ForeignKey(User)
	Title = models.CharField(max_length=200)
	QuestionText = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()
	
class Tag(models.Model):
	Tag = models.CharField(max_length=50)	
	
class QuestionTag(models.Model):
	QuestionID=models.ForeignKey(Question)
	TagID = models.ForeignKey(Tag)
	#association Table

class QuestionComment(models.Model):
	QuestionID = models.ForeignKey(Question)
	UserID = models.ForeignKey(User)
	Comment = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()
	
class Answer(models.Model):
	QuestionID = models.ForeignKey(Question)
	UserID = models.ForeignKey(User)
	Answer = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()
	
class Comment(models.Model):
	AnswerID = models.ForeignKey(Answer)
	UserID = models.ForeignKey(User)
	Comment = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()

class SiteSettings(models.Model):
	isPublic = models.BooleanField(default=True)
	

class QuestionAttachment(models.Model):
	QuestionID = models.ForeignKey(Question)
	FilePath = models.CharField(max_length=100)
	
class AnswerAttachment(models.Model):
	AnswerID = models.ForeignKey(Answer)
	FilePath = models.CharField(max_length=100)

class QuestionVote(models.Model):
	UserID = models.ForeignKey(User)
	QuestionID = models.ForeignKey(Question)
	Value = models.IntegerField()

class AnswerVote(models.Model):
	UserID = models.ForeignKey(User)
	AnswerId = models.ForeignKey(Answer)
	Value = models.IntegerField()
