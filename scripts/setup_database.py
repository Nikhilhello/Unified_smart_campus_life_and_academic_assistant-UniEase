# Create admin profile if it doesn't exist
from campus.models import UserProfile
admin_user = User.objects.get(username='admin')
try:
    admin_profile = admin_user.profile
    print("  Admin profile already exists")
except UserProfile.DoesNotExist:
    UserProfile.objects.create(
        user=admin_user,
        role='admin',
        department='Administration',
        phone='0000000000'
    )
    print("  Admin profile created!")
=======
# Create admin profile if it doesn't exist
from campus.models import UserProfile
admin_user = User.objects.get(username='admin')
try:
    admin_profile = admin_user.profile
    print("  Admin profile already exists")
except UserProfile.DoesNotExist:
    UserProfile.objects.create(
        user=admin_user,
        role='admin',
        department='Administration',
        phone='0000000000'
    )
    print("  Admin profile created!")
