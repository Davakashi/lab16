# Unit Test Template for Work 2

Энэ файлд AI-аас гарсан эсвэл өөрийн бэлтгэсэн unit test-үүдийг оруулаарай.

## Алхам:

1. AI-аас гарсан test code-г copy-paste хий
2. Доорх template-г дагаж оруул
3. pytest test_email_validator.py -v ажиллуул
4. Хүүхлүүдэрхий үр дүнгээ шалгал

---

## Test Template:

```python
import pytest
from email_validator import is_valid_email

# Энд AI-аас гарсан тестүүдээ оруулах

class TestIsValidEmail:
    """Email validation функцийн test cases"""
    
    # Positive tests - зөв имэйлүүд
    def test_positive_case_1(self):
        pass
    
    # Negative tests - буруу имэйлүүд
    def test_negative_case_1(self):
        pass
    
    # Edge cases - хилийн нөхцөл
    def test_edge_case_1(self):
        pass
```

---

## Тестийн үр дүн:

```
АЖИЛЛУУЛСАН: pytest test_email_validator.py -v

Үр дүн:
(Үр дүнгээ энд paste хий)
```

---

## Алдаа ба засварлалт:

| Test ID | Анхны статус | Алдаа | Засварлалт | Эцсийн статус |
|---------|--------|-------|----------|----------|
| test_1 | FAIL | | | PASS |
| test_2 | PASS | | | PASS |

---

## Эцсийн мэдэгдэл:

- [ ] Бүх тест PASS
- [ ] Test cover 8+ cases
- [ ] AI prompt-г feedback өгсөн
