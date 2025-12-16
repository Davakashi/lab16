# АЖИЛ 3: SELF-HEALING AUTOMATION ОЙЛГОЛТ (15 МИН)

## А. UI Element - Анхны нөхцөл:

### HTML код:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <form id="loginForm">
        <input id="emailField" type="email" placeholder="Email">
        <input id="passwordField" type="password" placeholder="Password">
        <button id="loginBtn">Login</button>
    </form>
</body>
</html>
```

### Уламжлалт Selenium код:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com/login")

# ID selector ашиглан button сонгох
login_button = driver.find_element(By.ID, "loginBtn")
login_button.click()
```

---

## Б. Эвдрэл үүсгэх сценари:

### Өмнөх HTML:
```html
<button id="loginBtn">Login</button>
```

### Шинэ HTML (ID солигдсон):
```html
<button id="signinButton">Login</button>
```

**Үр дүн:** Selenium тест FAIL - "Element not found: id=loginBtn"

---

## C. AI-д өгөх Prompt:

```
Та UI automation QA инженер байна. Selenium тест эвдрэлтэй байна.

АСУУДАЛ:
- HTML element-ийн ID солигдсон
- Анхны locator: By.ID, "loginBtn" 
- Шинэ HTML:   <button id="signinButton">Login</button>

БОДЛОГО:
1. Шинэ locator-уудыг санал болго (3-4 сонголт)
2. Self-healing automation зарчим гэж юу болохыг тайлбарла
3. Dynamic locator эсвэл robust selector ашиглаж, код сайжрул

ШААРДЛАГА:
- XPath, CSS selector, Text matching зэрэг өөр method ашиглах
- Self-healing framework (Testim, Mabl)-ийн санаа нь юу болохыг ойлгуулах
- Robust code жишээ өгөх
```

---

## D. Оюутны хийх ажил:

### Алхам 1: HTML test page үүсгэх

1. `login.html` файл үүсгэ
2. Доорх HTML copy-paste хий
3. Browser-т нээж шалгал

### Алхам 2: Анхны Selenium код ажиллуулах

1. `selenium_test_initial.py` үүсгэ
2. Доорх код оруул

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/path/to/login.html")  # Windows path

try:
    # ID selector ашиглан сонгох
    login_button = driver.find_element(By.ID, "loginBtn")
    print("✓ Button found by ID")
    login_button.click()
except Exception as e:
    print(f"✗ Error: {e}")
finally:
    time.sleep(2)
    driver.quit()
```

3. Ажиллуулж, success баталгаажуулал

### Алхам 3: HTML-г өөрчилж эвдэх

1. `login.html` дээр ID-г `signinButton` гэж өөрчил
2. Дахин test ажиллуулж FAIL баталгаажуулал

### Алхам 4: AI-д prompt илгээж шийдэл авах

1. ChatGPT / Claude-г нээ
2. Дээрх prompt илгээ
3. Гарсан шийдлүүдийг шалгаж сураа

### Алхам 5: Self-healing зарчмыг ойлгох

AI-аас ирсэн шийдлүүдээр:
- ✓ XPath selector нь яг сайн уу?
- ✓ CSS selector нь robust уу?
- ✓ Text-based matching нь тогтвортой уу?
- ✓ Confidence scoring гэж юу вэ?

---

## E. Self-Healing Automation зарчим:

### Уламжлалт Automation:
```
Locator → Element → Action
   ↓
Fail → STOP
```

### Self-Healing Automation:
```
Locator → Element? NO → Fallback Locators
   ↓                    ↓
   ✓                 Alternative selectors
   ↓                    ↓
 Action            Confidence score
   ↓                    ↓
Success          AI suggests fix
```

---

## F. Robust Selector жишээ:

### 1. ID Selector (Хэмжээ: Төөмөр)
```python
driver.find_element(By.ID, "loginBtn")
```
⚠️ Сул талууд: ID өнөө болж солигдоно

### 2. XPath (Хэмжээ: Дунд)
```python
driver.find_element(By.XPATH, "//button[@id='loginBtn' or contains(text(), 'Login')]")
```
✓ Давуу талууд: Эсвэл нөхцөл ашиглаж robust

### 3. CSS Selector (Хэмжээ: Дунд)
```python
driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
```
✓ Давуу талууд: Type attribute эсвэл class ашиглаж

### 4. Text Matching (Хэмжээ: Сайн)
```python
driver.find_element(By.XPATH, "//*[text()='Login' or contains(text(), 'Login')]")
```
✓ Давуу талууд: UI өөрчлөлтөд сэтгэл татахгүй

### 5. Multiple Locator Strategy (Self-Healing Pattern)
```python
def find_login_button(driver):
    \"\"\"Multiple strategies ашиглан button сонгох\"\"\"
    locators = [
        (By.ID, "loginBtn"),
        (By.ID, "signinButton"),
        (By.CSS_SELECTOR, "button[type='submit']"),
        (By.XPATH, "//button[contains(text(), 'Login')]"),
        (By.CLASS_NAME, "login-button")
    ]
    
    for strategy, selector in locators:
        try:
            element = driver.find_element(strategy, selector)
            print(f"✓ Found using: {strategy} = {selector}")
            return element
        except:
            continue
    
    raise Exception("Element not found with any locator")

# Ашиглах:
login_button = find_login_button(driver)
login_button.click()
```

---

## G. Self-Healing Tools гүйлгээ:

### Testim.io / Mabl ба яаж ажилладаг:

1. **Element Recognition** - DOM structure ба visual features ашиглан элемент таних
2. **Locator Validation** - UI өөрчлөгдсөн үед ямар locator үр дүнтэй вэ гэж шалгах
3. **Confidence Scoring** - "80% итгэлтэй энэ үүүүүжвэл" гэж үнэлгээ
4. **Automatic Healing** - UI солигдсон үед, автоматаар fix санал болгоно

---

## H. Хүлээгдэх үр дүн:

✓ Selenium-ийн анхны тест ажиллах  
✓ HTML өөрчилж эвдрэлтэй баталгаажуулах  
✓ Олон locator strategies ойлгох  
✓ Self-healing зарчмыг ойлгох  
✓ Robust selector сайжруулалт хийх  

---

## I. Даалгавар:

1. [ ] HTML file үүсгэж ажиллуулах
2. [ ] Selenium anхны код ажиллуулах
3. [ ] HTML өөрчилж FAIL баталгаажуулах
4. [ ] 4+ robust locators сөнгөе болгох
5. [ ] Self-healing strategy code бичих
6. [ ] AI үр дүн дэвшүүлэх
