from django_seed import Seed 
seeder = Seed.seeder()
from .models import CustomUser,Inquiry_list,Data,License,get_random_string
seeder.add_entity(CustomUser, 10)
seeder.add_entity(License, 10)
seeder.add_entity(Data, 10)
seeder.add_entity(Inquiry_list, 10)
inserted_pks = seeder.execute()