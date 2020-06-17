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

def run_seed(self, mode):
  clear_data()
  if mode == MODE_CLEAR:
    return
  
  create_user()

