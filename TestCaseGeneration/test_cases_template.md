# Login System - Test Cases

## Заавар:

Энэ файлыг ашиглан AI-аас гарсан test case-ууд болон өөрийн сайжруулсан test case-ууд хадгалаарай.

## Format:

| Test Case ID | Title | Pre-condition | Steps | Expected Result | Priority | Status |
|---|---|---|---|---|---|---|
| TC-001 | Valid Login | User account exists | 1. Enter email<br>2. Enter correct password<br>3. Click Login | Dashboard loads successfully | High | ⬜ |
| TC-002 | Invalid Password | User account exists | 1. Enter email<br>2. Enter wrong password<br>3. Click Login | Error message appears | High | ⬜ |
| TC-003 | Empty Email | - | 1. Leave email empty<br>2. Enter password<br>3. Click Login | Validation error for email | Medium | ⬜ |

## AI-аас гарсан анхны test case-ууд:

(AI хариултыг энд paste хийх)

---

## Оюутан сайжруулсан эцсийн test case-ууд:

### Functional Test Cases:

| TC-F001 | Valid login with correct credentials | User account exists in DB | 1. Navigate to login page<br>2. Enter registered email<br>3. Enter correct password<br>4. Click 'Login' button | Dashboard page loads, user is authenticated | High | ⬜ |
| TC-F002 | Login with valid email format variation | User account exists | 1. Enter email with uppercase letters<br>2. Enter correct password<br>3. Click Login | System accepts (case-insensitive), login successful | Medium | ⬜ |
| TC-F003 | Password visibility toggle ON | - | 1. Click password field<br>2. Click eye icon | Password text becomes visible (no asterisks) | Medium | ⬜ |
| TC-F004 | Password visibility toggle OFF | Password is visible | 1. Click eye icon | Password becomes masked with asterisks | Medium | ⬜ |

### Negative Test Cases:

| TC-N001 | Invalid password - first attempt | User account exists | 1. Enter registered email<br>2. Enter wrong password<br>3. Click Login | Error message "Invalid password" appears, login form clears | High | ⬜ |
| TC-N002 | Invalid password - second attempt | Account not locked | 1. Enter registered email<br>2. Enter wrong password<br>3. Click Login | Error message appears (attempt 2/3) | High | ⬜ |
| TC-N003 | Invalid password - third attempt (Account locked) | Last 2 attempts failed | 1. Enter registered email<br>2. Enter wrong password<br>3. Click Login | Message "Account temporarily locked" appears, login disabled | High | ⬜ |
| TC-N004 | Empty email field | - | 1. Leave email empty<br>2. Enter password<br>3. Click Login | Validation error "Email is required" displays | High | ⬜ |
| TC-N005 | Empty password field | - | 1. Enter email<br>2. Leave password empty<br>3. Click Login | Validation error "Password is required" displays | High | ⬜ |
| TC-N006 | Non-registered email | - | 1. Enter non-registered email<br>2. Enter password<br>3. Click Login | Error message "User not found" or "Invalid credentials" | Medium | ⬜ |

### Boundary Test Cases:

| TC-B001 | Minimum password length (7 chars) | Password policy: min 8 chars | 1. Enter email<br>2. Enter 7-character password<br>3. Click Login | Validation error "Password must be at least 8 characters" | Medium | ⬜ |
| TC-B002 | Exact password length (8 chars) | Password policy: min 8 chars | 1. Enter email<br>2. Enter 8-character password<br>3. Click Login | Login succeeds (if other credentials valid) | Medium | ⬜ |
| TC-B003 | Very long email | - | 1. Enter 255-char email (valid format)<br>2. Enter password<br>3. Click Login | System accepts or shows appropriate error | Low | ⬜ |
| TC-B004 | Email with special characters | - | 1. Enter email like "test+tag@example.com"<br>2. Enter password<br>3. Click Login | Login succeeds if user exists with this email | Medium | ⬜ |

### Security Test Cases:

| TC-S001 | SQL Injection in email field | - | 1. Enter email: "' OR '1'='1"<br>2. Enter password<br>3. Click Login | System rejects, shows error, no database compromise | High | ⬜ |
| TC-S002 | XSS attempt in password field | - | 1. Enter email<br>2. Enter password: "<script>alert('xss')</script>"<br>3. Click Login | Script not executed, treated as plain text | High | ⬜ |
| TC-S003 | HTTPS enforcement | - | 1. Try accessing login via HTTP | Redirect to HTTPS or refuse connection | High | ⬜ |
| TC-S004 | Password not shown in URL | Valid credentials | 1. Monitor URL after login attempt | No password appears in URL parameters | High | ⬜ |
| TC-S005 | Account locked after 3 attempts | 3 failed attempts | 1. Make 3 failed login attempts<br>2. Try to login with correct password | Cannot login even with correct password, locked message shown | High | ⬜ |

---

## Нийт: __ / 15 тест кейс

## Шинжүүлэлт:

- **AI нэмсэн бүтээл:** 
- **Оюутан нэмсэн/засварласан:** 
- **Дутуу болсон edge case нь:**
