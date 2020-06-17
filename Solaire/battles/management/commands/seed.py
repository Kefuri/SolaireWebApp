from django.core.management.base import BaseCommand, CommandError

from battles.models import User, Monster, Team, Move

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'


class Command(BaseCommand):
  help = "Seeds the database with usable data"

  def add_arguments(self, parser):
    parser.add_argument('--mode', type=str, help="Mode")
  
  def handle(self, *args, **options):
    self.stdout.write("Seeding data...")
    run_seed(self, options['mode'])
    self.stdout.write("Done.")

def clear_data():
  User.objects.all().delete()
  Monster.objects.all().delete()
  Team.objects.all().delete()
  Move.objects.all().delete()

def create_user():
  u = User(
    username="mrseed",
    password="seedyboi1",
    elo=100,
  )
  u.save()
  return u

def create_pikachu():
  pikachu = Monster(
    name="pikachu",
    monster_type="electric",
    attack=100,
    defense=40,
    speed=120
  )
  pikachu.save()
  return pikachu

def create_charizard():
  charizard = Monster(
    name="charizard",
    monster_type="fire",
    attack=120,
    defense=60,
    speed=80
  )
  charizard.save()
  return charizard

def create_thunderbolt():
  thunderbolt =  Move(
    name="thunderbolt",
    move_type="electric",
    damage=100
  )
  thunderbolt.save()
  return thunderbolt

def create_flamethrower():
  flamethrower = Move(
    name="flamethrower",
    move_type="fire",
    damage=80
  )
  flamethrower.save()
  return flamethrower

def create_team():
  team1 = Team(
    team_name="team1"
  )
  team1.save()
  return team1

def create_and_add_relations():
  user = create_user()
  team = create_team()
  pikachu = create_pikachu()
  charizard = create_charizard()
  flamethrower = create_flamethrower()
  thunderbolt = create_thunderbolt()

  user.teams.add(team)
  team.monsters.add(pikachu, charizard)
  charizard.moves.add(flamethrower)
  pikachu.moves.add(thunderbolt)

def run_seed(self, mode):
  clear_data()
  if mode == MODE_CLEAR:
    return
  
  create_and_add_relations()
