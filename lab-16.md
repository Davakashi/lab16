# LAB15 ДҮГНЭЛТИЙН ТАЙЛАН
## AI-д СУУРИЛСАН ЧАНАРЫН БАТАЛГАА БА ТЕСТ

**Оюутны нэр:** Т. Даваажаргал /B222270012/
**Огноо:** 2025.12.17

---

## I. АЖИЛ 1: ШААРДЛАГААС TEST CASE ҮҮСГЭХ

### 1.1 Үр дүн:

**Үүсгэсэн тест кейсийн нийт тоо:** 15 / 15

**AI-аас авсан эхний test case-ууд:**
- [ ] Бүх функциональ тест
- [ ] Сөрөг тест
- [ ] Edge-case тест
- [ ] Security тест

### 1.2 AI-ийн нэмсэн үр дүн:

| Давуу тал | Дутагдал |
|---------|---------|
| Хурдан олон тест кейс үүсгэсэн| Security тест дутуу |
| Ерөнхий логик зөв | Зарим edge-case орхигдсон |
| Формат цэгцтэй | Реал амьдралын нөхцөл бага |

### 1.3 Оюутан нэмсэн/засварласан зүйлүүд:

```
1. Хоосон input шалгах тест нэмсэн
2. Null утга шалгах тест нэмсэн
3. Boundary утгуудын тест нэмсэн
4. Давхар @ орсон email тест нэмсэн
5. Том жижиг үсгийн ялгааг шалгасан 
```

### 1.4 Дутуу болсон edge-case нь:

```
- "@@" агуулсан email
- "@test.com" дунд нь орсон email
- Маш урт email string
```

### 1.5 AI гаргасан алдаа ба засварлалт:

| Алдаа | Шийдэл |
|------|--------|
| Edge-case дутуу | Гараар нэмсэн |
| Security тест орхисон | SQL/XSS тест санал болгосон |

---

## II. АЖИЛ 2: CODE → UNIT TEST ҮҮСГЭХ

### 2.1 Өгөгдсөн функц:

```python
def is_valid_email(email):
    if "@" not in email:
        return False
    if email.endswith("@test.com"):
        return False
    return True
```

### 2.2 Test статус:

**Нийт test case:** 6
**PASS:** 5 
**FAIL:** 1 
**Skip:** 0

### 2.3 Test ажиллуулалтын үр дүн:

```bash
test_valid_email PASSED
test_missing_at PASSED
test_test_domain FAILED
test_empty_string PASSED
test_multiple_at PASSED
test_none_input PASSED

```

### 2.4 Fail болсон тест болон засварлалт:

| Test ID | Анхны статус | Алдаа | Засварлалт | Эцсийн статус |
|---------|---------|-------|----------|----------|
| test_test_domain | FAIL | endswith логик буруу | strip хийсэн | PASS |

### 2.5 Функцийн логик анализ:

**Функцийн хэрэгцээ:**
- [ ] @ символ байх ёстой
- [ ] @test.com хаажуулдсан
- [ ] Үлдэх зүйлс зөв

**Алдаа байгаа эсэх:**
- [ ] Үгүй - Функц зөв
- [ ] Тийм - Алдаа байна

**Алдаа байвал гарсан шалтгаан:**
```
None input шалгаагүй, type validation байхгүй
```

### 2.6 AI-ийн prompt сайжруулалт:

**Анхны prompt:**
```
Generate unit tests for this function
```

**Сайжруулсан prompt:**
```
Generate unit tests including edge-cases and negative scenarios using pytest
```

**Үйл ажиллагаа:**
- [ ] 1 удаа ажиллуулав
- [ ] 2+ удаа сайжруулан ажиллуулав

---

## III. АЖИЛ 3: SELF-HEALING AUTOMATION ОЙЛГОЛТ

### 3.1 HTML element эвдрэлийн нөхцөл:

**Анхны HTML:**
```html
<button id="loginBtn">Login</button>
```

**Шинэ HTML (эвдэрлэн):**
```html
<button id="signinButton">Login</button>
```

### 3.2 Selenium test статус:

| Test | Үр дүн | Өмнө | Дараа |
|------|--------|------|--------|
| Үндсэн ID selector | FAIL → PASS | loginBtn | signinButton |
| Robust selector | PASS | text locator | text locator |

### 3.3 Туршигдсан locator strategies:

| # | Strategy | Selector | Status |
|---|----------|----------|--------|
| 1 | By.ID | loginBtn | FAIL |
| 2 | By.ID | signinButton | PASS |
| 3 | By.CSS_SELECTOR | button[type='submit'] | PASS |
| 4 | By.XPATH | //button[contains(text(), 'Login')] | PASS |
| 5 | By.XPATH | //button | PASS |

### 3.4 Self-Healing зарчмын ойлголт:

**Оноо:** 9 / 10

**Ойлгосон зүйлүүд:**

- [ ] UI өөрчлөлт automation-д чухал асуудал
- [ ] Multiple locators стратеги ашигла
- [ ] Confidence scoring ойлгосон
- [ ] Dynamic locators-ийн үүрэг ойлгосон
- [ ] Self-healing tools (Testim, Mabl) ойлгосон

**асуулт:**

```
1. Self-healing automation ба уламжлалт automation-ийн ялгаа:

Уламжлалт automation нь эвдэрдэг, self-healing нь автоматаар дасан зохицдог

2. Dynamic locators юунд ач холбогдолтой вэ:
Dynamic locator нь UI өөрчлөгдөхөд тест эвдрэхээс сэргийлнэ


3. Testim/Mabl-ийн confidence scoring-ийн үүрэг:
Confidence scoring нь хамгийн тохирох locator-ыг сонгоход ашиглагдана

```

### 3.5 AI-аас ирсэн сайн зөвөлгөөнүүд:

```
- Text-based locator ашиглах
- XPath contains хэрэглэх
- Backup locator тодорхойлох
```

---

## IV. АЖИЛ 4: SYNTHETIC TEST DATA ҮҮСГЭХ

### 4.1 Үүсгэсэн өгөгдөлүүд:

**CSV файл:** synthetic_users.csv  
**Нийт мөр:** 20 / 20  
**Format:** CSV, JSON

### 4.2 Чанарын баталгаа үр дүн:

| Үзүүлэлт | Шалгалт | Үр дүн | Status |
|---------|---------|--------|--------|
| Нийт мөр | 20 мөр | OK| + |
| Дублиcate | Үгүй | OK | + |
| Email validity | 20/20 зөв | OK | + |
| Age range | 18-100 | OK | + |
| Valid roles | admin/user/analyst/manager/guest | OK | + |
| Country diversity | 3+ орон | OK | + |
| Name realism | Энгийн нэр | OK | + |
| No PII | SSN/Phone байхгүй | OK | + |

### 4.3 Validation скрипт үр дүн:

```
Validation completed successfully
No errors found


```

### 4.4 Алдаа байсан бол засварлалт:

| Алдаа | Шийдэл |
|------|--------|
| Duplicate email | Random seed өөрчилсөн |

### 4.5 Synthetic data-н үнэ цэнэ:

**Асуулт:** Synthetic data ашиглахад яамар давуу тал байна?

```
1. Бодит дата шаардахгүй
2. Аюулгүй
3. Хурдан тест хийх боломжтой

```

**Асуулт:** Potential risks нь юу вэ?

```
1. Реал биш байж магадгүй
2. Зарим edge-case тусгагдахгүй
```

### 4.6 Country distribution:

```

Орон       | Тоо  | %
-----------|------|----
  Mongolia |  8   | 40%
    USA    |  6   | 30%
   Korea   |  6   | 30%
```

---

## V. ЕРӨНХИЙ АНАЛИЗ

### 5.1 AI ашиглахад тулгарсан хүндрэл:

```
1. Зарим хариулт хэт ерөнхий
2. Edge-case орхигддог
3. Prompt-оос их хамааралтай
```

### 5.2 AI ашиглахад тулгарсан сургамж:

```
1. Prompt маш чухал
2. AI-г шалгаж ашиглах хэрэгтэй
3. QA мэдлэг зайлшгүй хэрэгтэй
```

### 5.3 QA-ийн AI ашиглалтын ирээдүй:
```
1. Test automation хурдсана
2. Self-healing стандарт болно
3. QA productivity өснө
```

### 5.4 Юунд цаашид ашиглах хэрэгтэй вэ:
**Сайн тал**
```
- AI-г тест дизайн-д ашиглах
- Regression automation
 
```

**Муу тал**

```
- Blind copy-paste
- Validation хийхгүй орхих
```

---

## VI. ДҮГНЭЛТ

### 6.1 Lab-ийн эцсийн оноо:

| Ажил | Оноо | Max | % |
|------|------|-----|---|
| Ажил 1: Test Case | 18 | 20 | 90% |
| Ажил 2: Unit Test | 17 | 20 | 85% |
| Ажил 3: Self-healing | 19 | 20 | 95% |
| Ажил 4: Synthetic Data |18 | 20 | 90% |
| **НИЙТ** | **72** | **80** | **90%** |

### 6.2 Ерөнхий үзэл баримтлал:

```
Lab-ийн ажлыг хийхэд ойлгосон сайн зүйл:

1. AI QA-д бодитоор тусалдаг
2. Гэхдээ хяналт зайлшгүй
3. Prompt чадвар чухал

Цаашдах сурахаас хүсэх сэдэв:

1. AI-based test generation
2. Self-healing frameworks
3. Security automation 
```

### 6.3 Сурагчийн төлөв:

```
Сайн ойлгосон - AI-г ашиглаж сурсан
```

### 6.4 Сүүлийн сэтгэгдэл:

```
Энэ lab-ын эцэст, AI-г QA-д ашиглахад:

- (challenge): AI-д бүрэн дүүрэн итгэж болохгүй. Дараа нь нягталж шалгах.

- (opportunity): QA ажлыг асар хурдан хийж өгсөн

```

---

