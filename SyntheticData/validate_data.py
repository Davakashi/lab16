"""
Synthetic Data Validation Script

Энэ скрипт synthetic user data-н чанарыг шалгадаг.
"""

import csv
import re
from collections import defaultdict

def validate_synthetic_data(csv_file):
    """Synthetic data quality check"""
    
    print("\n" + "="*60)
    print("SYNTHETIC DATA QUALITY VALIDATION REPORT")
    print("="*60 + "\n")
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except FileNotFoundError:
        print(f"ERROR: File not found - {csv_file}")
        return False
    
    # 1. Row count check
    row_count = len(data)
    print(f"[1] Total Rows: {row_count}")
    print(f"    Expected: 20")
    print(f"    Status: {'✓ PASS' if row_count == 20 else '✗ FAIL'}\n")
    
    # 2. Column check
    if data:
        columns = list(data[0].keys())
        expected_cols = {'name', 'email', 'age', 'country', 'role'}
        print(f"[2] Columns: {columns}")
        print(f"    Expected: {expected_cols}")
        col_match = set(columns) == expected_cols
        print(f"    Status: {'✓ PASS' if col_match else '✗ FAIL'}\n")
    
    # 3. Duplicate check
    emails = [row['email'] for row in data]
    names = [row['name'] for row in data]
    email_dups = len(emails) - len(set(emails))
    name_dups = len(names) - len(set(names))
    
    print(f"[3] Duplicates Check:")
    print(f"    Email duplicates: {email_dups}")
    print(f"    Name duplicates: {name_dups}")
    print(f"    Status: {'✓ PASS' if email_dups == 0 else '✗ FAIL'}\n")
    
    # 4. Email validation
    email_pattern = r'^[^@]+@[^@]+\.[^@]+$'
    valid_email_count = 0
    invalid_emails = []
    
    for i, row in enumerate(data, 1):
        email = row.get('email', '')
        if re.match(email_pattern, email):
            valid_email_count += 1
        else:
            invalid_emails.append((i, email))
    
    print(f"[4] Email Validation:")
    print(f"    Valid emails: {valid_email_count}/20")
    if invalid_emails:
        print(f"    Invalid emails:")
        for idx, email in invalid_emails:
            print(f"      - Row {idx}: '{email}'")
    print(f"    Status: {'✓ PASS' if valid_email_count == 20 else '✗ FAIL'}\n")
    
    # 5. Age validation
    valid_age_count = 0
    invalid_ages = []
    
    for i, row in enumerate(data, 1):
        try:
            age = int(row.get('age', 0))
            if 18 <= age <= 100:
                valid_age_count += 1
            else:
                invalid_ages.append((i, age))
        except ValueError:
            invalid_ages.append((i, row.get('age', 'N/A')))
    
    print(f"[5] Age Validation (18-100 range):")
    print(f"    Valid ages: {valid_age_count}/20")
    if invalid_ages:
        print(f"    Invalid ages:")
        for idx, age in invalid_ages:
            print(f"      - Row {idx}: {age}")
    print(f"    Status: {'✓ PASS' if valid_age_count == 20 else '✗ FAIL'}\n")
    
    # 6. Role validation
    valid_roles = {'admin', 'user', 'analyst', 'manager', 'guest'}
    role_count = defaultdict(int)
    valid_role_count = 0
    invalid_roles = []
    
    for i, row in enumerate(data, 1):
        role = row.get('role', '').lower()
        role_count[role] += 1
        if role in valid_roles:
            valid_role_count += 1
        else:
            invalid_roles.append((i, role))
    
    print(f"[6] Role Validation:")
    print(f"    Valid roles count: {valid_role_count}/20")
    print(f"    Valid role types: {valid_roles}")
    print(f"    Role distribution:")
    for role, count in sorted(role_count.items()):
        status = '✓' if role in valid_roles else '✗'
        print(f"      {status} {role}: {count}")
    print(f"    Status: {'✓ PASS' if valid_role_count == 20 else '✗ FAIL'}\n")
    
    # 7. Country check
    countries = defaultdict(int)
    for row in data:
        country = row.get('country', 'Unknown')
        countries[country] += 1
    
    print(f"[7] Country Distribution:")
    print(f"    Unique countries: {len(countries)}")
    for country, count in sorted(countries.items(), key=lambda x: x[1], reverse=True):
        print(f"      - {country}: {count}")
    print()
    
    # Final summary
    all_checks = [
        row_count == 20,
        col_match if data else False,
        email_dups == 0,
        valid_email_count == 20,
        valid_age_count == 20,
        valid_role_count == 20
    ]
    
    passed = sum(all_checks)
    total = len(all_checks)
    
    print("="*60)
    print(f"OVERALL RESULT: {passed}/{total} checks passed")
    print("="*60)
    
    if all(all_checks):
        print("\n✓ ALL VALIDATIONS PASSED - Data is ready for testing!\n")
        return True
    else:
        print("\n✗ SOME VALIDATIONS FAILED - Please review and fix data\n")
        return False

def main():
    # CSV файл path
    csv_file = 'synthetic_users_sample.csv'
    
    # Validation ажиллуулах
    validate_synthetic_data(csv_file)

if __name__ == "__main__":
    main()
