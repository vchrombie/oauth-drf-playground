from django.contrib.auth.models import User, Group

# Group objects

dc = Group(name='DC')
dc.save()

marvel = Group(name='Marvel')
marvel.save()

# User objects

spiderman = User(username='spiderman', password='spiderman_pwd', email='spiderman@marvel.com', first_name='Spider', last_name='Man')
spiderman.save()
spiderman.groups.add(marvel)

ironman = User(username='ironman', password='ironman_pwd', email='ironman@marvel.com', first_name='Iron', last_name='Man')
ironman.save()
ironman.groups.add(marvel)

batman = User(username='batman', password='batman_pwd', email='batman@dc.com', first_name='Bat', last_name='Man')
batman.save()
batman.groups.add(dc)

superman = User(username='superman', password='superman_pwd', email='superman@dc.com', first_name='Super', last_name='Man')
superman.save()
superman.groups.add(dc)

aquaman = User(username='aquaman', password='aquaman_pwd', email='aquaman@dc.com', first_name='Aqua', last_name='Man')
aquaman.save()
aquaman.groups.add(dc)

gentleman = User(username='gentleman', password='gentleman_pwd', email='gentleman@gentleman.com', first_name='Gentle', last_name='Man')
gentleman.save()
gentleman.groups.add(dc, marvel)
