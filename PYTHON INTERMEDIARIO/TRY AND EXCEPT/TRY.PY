

try:
    a = 18
    b = 0
    c = a/b
except ZeroDivisionError:
    print('dividiu por zero')
except Exception:
    print('erro desconehcido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG', error)
    print('Nome', error.__class__.__name__)
print('CONTINUE')



# exceções == classes