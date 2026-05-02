# -*- coding: utf-8 -*-
# UniEase Database Reset Script
# This script will drop and recreate the database

import pymysql
import sys

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'system'
DB_NAME = 'uniease_db'

def reset_database():
    """Drop and recreate the database"""
    try:
        # Connect to MySQL server (not to a specific database)
        print(f"Connecting to MySQL server at {DB_HOST}...")
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        
        # Drop database if exists
        print(f"Dropping database '{DB_NAME}' if it exists...")
        cursor.execute(f"DROP DATABASE IF EXISTS `{DB_NAME}`")
        
        # Create database
        print(f"Creating database '{DB_NAME}'...")
        cursor.execute(f"CREATE DATABASE `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        
        connection.commit()
        cursor.close()
        connection.close()
        
        print(f"✓ Database '{DB_NAME}' has been reset successfully!")
        print("\nYou can now run: python setup.py")
        return True
        
    except pymysql.Error as e:
        print(f"✗ Database error: {e}")
        print("\nPlease check:")
        print("  1. MySQL server is running")
        print("  2. Username and password are correct")
        print(f"  3. User '{DB_USER}' has permission to create databases")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("UniEase Database Reset".center(60))
    print("="*60)
    print()
    
    if reset_database():
        sys.exit(0)
    else:
        sys.exit(1)
