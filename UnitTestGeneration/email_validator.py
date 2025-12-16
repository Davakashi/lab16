def is_valid_email(email):
    """
    Email хүчингүй эсэхийг шалгадаг функц.
    
    Дүрэм:
    1. @ символ байх ёстой
    2. @test.com domain нь хаажуулдсан
    
    Args:
        email (str): Шалгах имэйл
        
    Returns:
        bool: True - зөв, False - буруу
    """
    if "@" not in email:
        return False
    if email.endswith("@test.com"):
        return False
    return True


# Test-ийг энд хадгалагдсан байх ёстой
if __name__ == "__main__":
    # Гараар тестлэх жишээ
    print("Valid emails:")
    print(is_valid_email("user@example.com"))      # True
    print(is_valid_email("john@domain.org"))       # True
    
    print("\nInvalid emails:")
    print(is_valid_email("userexample.com"))       # False (no @)
    print(is_valid_email("user@test.com"))         # False (test.com blocked)
    print(is_valid_email(""))                      # False (empty)
