# АЖИЛ 4: SYNTHETIC TEST DATA ҮҮСГЭХ (20 МИН)

## А. Үүрэг:

20 ширхэг synthetic user data (name, email, age, country, role) үүсгэх ба чанарыг хянах.

---

## Б. AI-д өгөх Prompt:

```
Та QA инженер байна. PII (Personally Identifiable Information) агуулаагүй 
synthetic user test data үүсгэнэ үү.

ШААРДЛАГА:
- 20 мөр user data
- Бүтэц: name, email, age, country, role
- CSV format-т оруул
- Бодит мэт боловч зохиомол байдлаар гаргана уу
- Дублиcate байхгүй
- Логик алдаа байхгүй (age < 18 эсвэл age > 120 зэрэг)
- Valid email format
- Мэргэжлийн эрх (admin, user, analyst, manager, guest)

OUTPUT:
CSV format:
name,email,age,country,role
[20 мөр өгөгдөл]

ДЭМҮҮЛЭЛ: 
- age: 18-80 (хүүхэлгүй, эргэлбээ зөв)
- country: ОХУ-ын нөхөрлөл эсвэл ASEAN эл нүүцүүд
- email: [name][random]@testdata.com форматыг ашиглаж болох
```

---

## В. Оюутны хийх ажил:

### Алхам 1: AI-д prompt илгээж өгөгдөл авах

1. ChatGPT / Claude нээ
2. Дээрх prompt-ыг илгээ
3. CSV output хүлээж авах

### Алхам 2: CSV файл үүсгэх

1. `synthetic_users.csv` файл үүсгэ
2. AI-аас ирсэн өгөгдлийг copy-paste хий

### Алхам 3: Өгөгдлийн чанарыг хянах

#### 3.1 Дублиcate шалгах
```python
# Python дээр:
import pandas as pd
df = pd.read_csv('synthetic_users.csv')
print(df.duplicated().sum())  # 0 байх ёстой
```

#### 3.2 Email format шалгах
```python
import re
valid_emails = df['email'].apply(lambda x: re.match(r'^[^@]+@[^@]+\.[^@]+$', x))
print(valid_emails.sum())  # 20 байх ёстой
```

#### 3.3 Age логик шалгах
```python
# age 18-100 байх ёстой
print((df['age'] >= 18).sum())  # 20 байх ёстой
print((df['age'] <= 100).sum()) # 20 байх ёстой
```

#### 3.4 Role validity
```python
valid_roles = {'admin', 'user', 'analyst', 'manager', 'guest'}
print(df['role'].isin(valid_roles).sum())  # 20 байх ёстой
```

### Алхам 4: Хүчингүй өгөгдөл сүүлчүүлэх

Хэрэв алдаа байвал AI-д дахин үүсгүүлэх:
- "age = 200 гэх мэт алдаа" → AI-д дахин үүсгүүл
- "Duplicate emails" → AI-д засварлуул
- "Invalid emails" → AI-д шалгуулж засварла

### Алхам 5: JSON format-т мөн үүсгэх (нэмэлт)

```python
import json
import pandas as pd

df = pd.read_csv('synthetic_users.csv')
json_data = df.to_dict('records')

with open('synthetic_users.json', 'w') as f:
    json.dump(json_data, f, indent=2)
```

---

## Г. Хүлээгдэж буй үр дүн:

✓ 20 мөр synthetic user data  
✓ Дублиcate үгүй  
✓ PII агуулаагүй  
✓ Valid email, age, role  
✓ Логик алдаа үгүй  
✓ CSV + JSON format  

---

## D. Synthetic Data Quality Checklist:

| Үзүүлэлт | Шалгалт | Урвал | Статус |
|---------|---------|-------|--------|
| Нийт мөр | 20 мөр байх | | ☐ |
| Дублиcate | Үгүй | | ☐ |
| Email validity | 20/20 зөв | | ☐ |
| Age range | 18-100 | | ☐ |
| Valid roles | 5 төрөл | | ☐ |
| Country diversity | 3+ орон | | ☐ |
| Name realism | Энгийн нэр | | ☐ |
| No PII | SSN/Phone байхгүй | | ☐ |

---

## E. Synthetic Data ашиглах зорилго:

1. **Testing** - Бодит ашигтай өгөгдлийг эрсдэлгүйгээр ашиглах
2. **Development** - Сүлжээний эхлүүлэлтэд дээж өгөгдөл үл дээж
3. **Privacy** - PII (нэр, ID, хүүхэлгүй мэдээлэл) хамгаалах
4. **Data Pipeline** - Data validation / ETL туршилдах
5. **Performance** - Том benchmark өгөгдөл үүсгэх (1000+ мөр)

---

## F. Эрсдэл ба сургамж:

### Потенциал эрсдэл:
- Synthetic data нь бодит pattern-ийг давтаж чадахгүй
- Edge-case бүтэвч үүсгэхэд хүнээ ашиглахаас хөтөлбөр сулрах
- AI-аас гарсан өгөгдлийг чанарын баталгаа хийхэргүй ашигла

### Best practice:
- Synthetic data хэнээс дутугш давуу сайн pattern эсвэл coverage сайжруулдаг
- AI ашиглан үүсгэхэд manual verification хэрэгтэй
- Test environment-т synthetic, production-т бодит өгөгдөл ашигла

---

## G. Дополнительно:

### Python скрипт synthetic data шалгахад:

```python
import pandas as pd
import re

def validate_synthetic_data(csv_file):
    \"\"\"Synthetic data quality check\"\"\"
    df = pd.read_csv(csv_file)
    
    print("="*50)
    print("SYNTHETIC DATA VALIDATION REPORT")
    print("="*50)
    
    # 1. Shape check
    print(f"\n✓ Total rows: {len(df)} (Expected: 20)")
    print(f"✓ Total columns: {len(df.columns)}")
    
    # 2. Duplicates
    dup_count = df.duplicated().sum()
    print(f"\n{'✓' if dup_count == 0 else '✗'} Duplicates: {dup_count} (Expected: 0)")
    
    # 3. Email validation
    email_pattern = r'^[^@]+@[^@]+\.[^@]+$'
    valid_emails = df['email'].apply(lambda x: bool(re.match(email_pattern, str(x)))).sum()
    print(f"{'✓' if valid_emails == 20 else '✗'} Valid emails: {valid_emails}/20")
    
    # 4. Age range
    valid_ages = ((df['age'] >= 18) & (df['age'] <= 100)).sum()
    print(f"{'✓' if valid_ages == 20 else '✗'} Valid ages (18-100): {valid_ages}/20")
    
    # 5. Roles
    valid_roles = {'admin', 'user', 'analyst', 'manager', 'guest'}
    valid_role_count = df['role'].isin(valid_roles).sum()
    print(f"{'✓' if valid_role_count == 20 else '✗'} Valid roles: {valid_role_count}/20")
    
    # 6. Summary
    print("\n" + "="*50)
    all_valid = (dup_count == 0 and valid_emails == 20 and 
                 valid_ages == 20 and valid_role_count == 20)
    print(f"Overall: {'✓ PASSED' if all_valid else '✗ NEEDS FIXING'}")
    print("="*50)
    
    return all_valid

# Ашиглах:
if __name__ == "__main__":
    validate_synthetic_data('synthetic_users.csv')
```

Энэ скриптийг `validate_data.py` гэж хэмнээд `python validate_data.py` ажиллуул.
