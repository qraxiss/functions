# 🇬🇧 What does this function do?

This function takes in a pandas series of phone numbers and a list of expressions (strip) to remove from each phone number in the series. The function first converts the series to a string type and then uses the str.replace() method to remove each expression from each phone number in the series using regular expression pattern matching. The method returns the modified series.

You can use this function to clean up phone numbers in a pandas dataframe, for example if you want to remove specific characters or patterns that are not part of the phone number itself.

Here's an example of how you might use this function:

```python
import pandas as pd

# Sample data
phones = pd.Series(['123-456-7890', '(234) 567-8901', '(345) 678-9012', '456 789 0123'])

# Strip out non-numeric characters
formatted_phones = phone_formatter(phones, strip=['-', '(', ')', ' '])

print(formatted_phones)
```
## Output

```
0    1234567890
1    2345678901
2    3456789012
3    4567890123
dtype: object
```

# 🇹🇷 Bu fonksiyon ne yapar ?

Bu fonksiyon, bir pandas serisi olarak telefon numaraları ve her telefon numarasından kaldırılacak ifadeleri (strip) içeren bir liste alır. Fonksiyon, seriyi string türüne çevirir ve daha sonra str.replace() yöntemini kullanarak, serinin her numarasındaki her ifadeyi, düzenli ifade desen eşleştirme kullanarak kaldırır. Yöntem, değiştirilmiş seriyi döndürür.

Bu fonksiyonu, bir pandas veri çerçevesindeki telefon numaralarını temizlemeye yardımcı olabilir, örneğin telefon numarasının kendisi dışındaki belirli karakterleri veya desenleri kaldırmak isterseniz.

Burada bu fonksiyonu nasıl kullanabileceğiniz hakkında bir örnek:

```python
import pandas as pd

# Sample data
phones = pd.Series(['123-456-7890', '(234) 567-8901', '(345) 678-9012', '456 789 0123'])

# Strip out non-numeric characters
formatted_phones = phone_formatter(phones, strip=['-', '(', ')', ' '])

print(formatted_phones)
```

## Çıktı
```
0    1234567890
1    2345678901
2    3456789012
3    4567890123
dtype: object
```