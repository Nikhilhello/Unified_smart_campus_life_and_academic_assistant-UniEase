-- ============================================
-- CREATE ADMIN SUPERUSER
-- ============================================

-- Note: This script provides instructions for creating admin user
-- You need to run this command in Django shell, NOT in MySQL

-- Command to run in terminal:
-- python manage.py createsuperuser

-- Enter these details when prompted:
-- Username: admin
-- Email: admin@university.edu
-- Password: admin123
-- Password (again): admin123

-- After creating the superuser, the admin profile will be automatically created
-- You can then run the other SQL scripts to populate the database

-- Alternatively, you can create user programmatically:
-- python manage.py shell
-- >>> from django.contrib.auth import get_user_model
-- >>> User = get_user_model()
-- >>> User.objects.create_superuser('admin', 'admin@university.edu', 'admin123')
