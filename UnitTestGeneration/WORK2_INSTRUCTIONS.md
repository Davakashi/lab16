# АЖИЛ 2: CODE → UNIT TEST ҮҮСГЭХ (20 МИН)

## А. Өгөгдөх Python функц:

```python
def is_valid_email(email):
    \"\"\"
    Email хүчингүй эсэхийг шалгадаг функц.
    
    Args:
        email (str): Шалгах имэйл
        
    Returns:
        bool: True - зөв, False - буруу
    \"\"\"
    if "@" not in email:
        return False
    if email.endswith("@test.com"):
        return False
    return True
```

---

## Б. AI-д өгөх Prompt:

```
Та Python unit test мэргэжилтэн байна. 

Доорх функцэд зориулж pytest unit test үүсгэнэ үү:

def is_valid_email(email):
    if "@" not in email:
        return False
    if email.endswith("@test.com"):
        return False
    return True

ШААРДЛАГА:
1. Эерэг тест (valid emails) - ямар эмэйл зөв гэж үзэхэд
2. Сөрөг тест (invalid emails) - буруу жишээ
3. Edge-case тестүүд - хилийн нөхцөл
4. Нийт 8-10 тест функц байх

Pytest синтаксис ашиглаж, fixture байх бол сайн.
```

---

## В. Оюутны хийх ажил:

### Алхам 1: Файл бүтэц үүсгэх
```
Work2_UnitTestGeneration/
├── email_validator.py      ← Өгөгдсөн функц
└── test_email_validator.py ← Unit test файл
```

### Алхам 2: AI-д prompt илгээх
- Claude / ChatGPT нээ
- Дээрх prompt-ыг илгээ
- Гарсан test code-г copy хий

### Алхам 3: VS Code-т test файл үүсгэх
- `test_email_validator.py` файл үүсгэ
- AI-аас ирсэн тестийг paste хий

### Алхам 4: Test ажиллуулах
```bash
# Эхлээд pytest суулга (хэрэв суусан бус бол)
pip install pytest

# Test ажиллуулах
pytest test_email_validator.py -v
```

### Алхам 5: Fail нүүд засварлах
- Хэрэв test fail болох бол:
  - AI prompt-г сайжруулан дахин үүсгүүлэх
  - Функцийн логик сайн ойлгосон эсэх шалгах
  - Test-ийг гараар засварлах

### Алхам 6: Эцсийн үр дүнг хэмнэх
- Амжилттай test код хэмнэх
- Test результатын скриншот авах

---

## Г. Хүлээгдэх үр дүн:

✓ AI-ийн generated unit test ажиллах  
✓ Бүх positive, negative, edge-case тестүүдийг оруулах  
✓ Iterative сайжруулалт хийх  
✓ Test-ийн 100% pass rate авах  

---

## D. Үл мэдэгдэх тулгарлага болон шийдэл:

| Асуудал | Шийдэл |
|--------|---------|
| Test fail гарах | Функцийн логик дахин шалгаж, test assert-г засварла |
| pytest суусан бус | `pip install pytest` ажиллуул |
| Import error | email_validator.py файл ижил folder-т байгаа эсэхийг шалгал |
| AI буруу test үүсгэх | Prompt-ыг аргыг нь өөрчилж дахин үүсгүүл |

---

## E. Гараар бэлэнгүүлсэн test жишээ:

```python
import pytest
from email_validator import is_valid_email

class TestIsValidEmail:
    \"\"\"Email validation функцийн test group\"\"\"
    
    def test_valid_email_basic(self):
        \"\"\"Энгийн зөв имэйл\"\"\"
        assert is_valid_email("user@example.com") == True
    
    def test_valid_email_with_subdomain(self):
        \"\"\"Subdomain-ээр зөв имэйл\"\"\"
        assert is_valid_email("user@mail.example.com") == True
    
    def test_invalid_email_no_at_symbol(self):
        \"\"\"@ символгүй буруу имэйл\"\"\"
        assert is_valid_email("userexample.com") == False
    
    def test_invalid_email_test_com_domain(self):
        \"\"\"@test.com domain нь хаажуулдсан\"\"\"
        assert is_valid_email("user@test.com") == False
    
    def test_empty_string(self):
        \"\"\"Хоосон string\"\"\"
        assert is_valid_email("") == False
    
    def test_only_at_symbol(self):
        \"\"\"Зөвхөн @ символ\"\"\"
        assert is_valid_email("@") == False
    
    def test_multiple_at_symbols(self):
        \"\"\"Олон @ символ\"\"\"
        assert is_valid_email("user@@example.com") == True  # @ байгаа аж л
    
    def test_special_characters_in_local_part(self):
        \"\"\"Спэшал тэмдэгтүүдтэй имэйл\"\"\"
        assert is_valid_email("user+tag@example.com") == True
```

---

## F. Хамт үзвэрлэх эргүүлэлт:

1. **AI ашиглаж сургаад нь батлагдаж байна уу?** - Тийм
2. **Функцийн logic эвдрэлтэй уу?** - Баталгаажуулах хэрэгтэй
3. **Test coverage хангалттай уу?** - 80%+ target
