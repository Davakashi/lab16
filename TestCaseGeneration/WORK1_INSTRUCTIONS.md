# АЖИЛ 1: ШААРДЛАГААС TEST CASE ҮҮСГЭХ (20 МИН)

## А. Өгөгдсөн шаардлага (Requirements):

1. Хэрэглэгч бүртгэлтэй имэйлээ оруулна.
2. Зөв нууц үг оруулбал Dashboard руу нэвтрэнэ.
3. Буруу нууц үг 3 удаа оруулбал "Account temporarily locked" гарна.
4. Password visibility toggle байх ёстой.
5. Хоосон имэйл → Validation error.

---

## Б. AI-д өгөх Prompt:

```
Та мэргэжлийн QA инженер байна. Дараах шаардлагад тулгуурлан:
- Functional test cases
- Negative test cases
- Boundary test cases
- Security-related test cases

үүсгэнэ үү.

Тестүүдийг 'Test Case ID | Title | Steps | Expected Result' хэлбэрээр хүснэгтлэнэ үү.

ШААРДЛАГА:
1. Хэрэглэгч бүртгэлтэй имэйлээ оруулна.
2. Зөв нууц үг оруулбал Dashboard руу нэвтрэнэ.
3. Буруу нууц үг 3 удаа оруулбал Account temporarily locked.
4. Password visibility toggle байх ёстой.
5. Хоосон имэйл → Validation error.
```

---

## В. Оюутны хийх ажил:

### Алхам 1: AI-д prompt илгээх
- ChatGPT эсвэл Claude-г нээ
- Дээрх prompt-ыг copy-paste хий
- AI-аас гарсан test case-ийн хариултыг хадгал

### Алхам 2: AI үр дүнг шүүн тунгаах
- Бүх тест кейс нь шаардлагатай бүтцэтэй эсэхийг шалгах
- Дублиcate тест байгаа эсэхийг шалгах
- Edge-case тестүүдийн хангалтыг үнэлэх

### Алхам 3: AI үр дүнг сайжруулах
- Дутуу болсон test case нь нэмэх
- Логик эвдрэлтэй тестүүдийг засварлах
- 10-15 тест кейсийн багц үүсгэх

### Алхам 4: Файлд хэмнэх
`test_cases.md` файл дээр өөрийн сайжруулсан test case-ууд хэмнэх

---

## Г. Хүлээгдэх үр дүн:

✓ 10-15 тест кейсийн багц үүсгэх  
✓ AI-ийн үр дүнг шүүн тунгаах  
✓ Буруу болон зөв логик ялгаж чадах  
✓ Test case-уудыг сайн хэлбэрт оруулах  

---

## D. Файлын бүтэц:

```
Work1_TestCaseGeneration/
├── WORK1_INSTRUCTIONS.md  ← Энэ файл
├── requirements.md        ← Шаардлага (reference)
├── AI_prompt.txt          ← AI-д явуулсан prompt хэмнэх
├── AI_response.md         ← AI-аас ирсэн анхны хариулт
└── test_cases.md          ← Оюутан засварласан эцсийн test case-ууд
```

---

## E. Өгөгдсөн Шаардлагын PDF Хувилбар:

`requirements.md` файлд бүх шаардлага бичсэнээр байна.
