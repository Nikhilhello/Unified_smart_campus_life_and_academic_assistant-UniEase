# -*- coding: utf-8 -*-
"""
Create Admin User Script
This script creates a default admin user for UniEase
"""

import os
import sys
import django

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uniease.settings')
django.setup()

from django.contrib.auth.models import User
from campus.models import UserProfile

def create_admin():
    """Create default admin user"""
    try:
        print("Creating admin user...")
        
        # Check if admin already exists
        if User.objects.filter(username='admin').exists():
            print("✓ Admin user already exists!")
            admin = User.objects.get(username='admin')
            print(f"  Username: admin")
            print(f"  Email: {admin.email}")
            return True
        
        # Create admin user
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@uniease.com',
            password='admin123',
            first_name='System',
            last_name='Administrator'
        )
        
        # Create user profile
        UserProfile.objects.create(
            user=admin,
            role='admin',
            department='Administration',
            phone='N/A'
        )
        
        print("✓ Admin user created successfully!")
        print("\n" + "="*60)
        print("Admin Credentials".center(60))
        print("="*60)
        print(f"  Username: admin")
        print(f"  Password: admin123")
        print(f"  Email: admin@uniease.com")
        print("\n  ⚠ IMPORTANT: Change this password after first login!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"✗ Error creating admin user: {e}")
        return False

if __name__ == "__main__":
    if create_admin():
        sys.exit(0)
    else:
        sys.exit(1)
