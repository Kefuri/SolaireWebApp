from django.db import models

class Move(models.Model):
  name = models.CharField(max_length=30)
  move_type = models.CharField(max_length=15)
  damage = models.IntegerField()

class Monster(models.Model):
  name = models.CharField(max_length=30)
  monster_type = models.CharField(max_length=15)
  attack = models.IntegerField()
  defense = models.IntegerField()
  speed = models.IntegerField()
  moves = models.ManyToManyField(Move)

class Team(models.Model):
  team_name = models.CharField(max_length=15)
  monsters = models.ManyToManyField(Monster)

class User(models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  elo = models.IntegerField()
  teams = models.ManyToManyField(Team)
