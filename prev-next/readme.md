# 🇬🇧 What does this function do ?

The `previous_and_next` function takes an iterable object, `list_like`, as input and returns an iterator that produces tuples containing the `previous`, `current`, and `next` elements in the input iterable.

Here is an example of how you could use the `previous_and_next` function:

```python
items = [1, 2, 3, 4, 5]

for prev, item, nxt in previous_and_next(items):
    print(f'previous: {prev}, current: {item}, next: {nxt}'`
```

## Output:
```
previous: None, current: 1, next: 2
previous: 1, current: 2, next: 3
previous: 2, current: 3, next: 4
previous: 3, current: 4, next: 5
previous: 4, current: 5, next: None
```

The tee function returns multiple independent iterators from a single input iterable. In this case, it returns three iterators: prevs, items, and nexts.

The chain function is used to concatenate the iterators returned by tee. The first chain call concatenates None with the prevs iterator, and the second chain call concatenates the nexts iterator with None. This is done so that the first element in the input iterable has a previous value of None and the last element has a next value of None.

Finally, the zip function is used to combine the three iterators into tuples. The resulting iterator produces tuples of the form (prev, item, nxt), where prev is the previous element in the input iterable, item is the current element, and nxt is the next element.


# 🇹🇷 Bu fonksiyon ne yapar ?

`previous_and_next` adlı fonksiyon bir iterable nesne, `list_like`, alır ve girdi iterable'ının önceki, şuanki ve sonraki elemanlarını içeren tuple'lar üreten bir iterator döndürür.

Burada `previous_and_next` fonksiyonunu nasıl kullanabileceğiniz örnek bir kod olabilir:

```python
items = [1, 2, 3, 4, 5]

for prev, item, nxt in previous_and_next(items):
    print(f'önceki: {prev}, şuanki: {item}, sonraki: {nxt}')
```

## Çıktı

```
önceki: None, şuanki: 1, sonraki: 2
önceki: 1, şuanki: 2, sonraki: 3
önceki: 2, şuanki: 3, sonraki: 4
önceki: 3, şuanki: 4, sonraki: 5
önceki: 4, şuanki: 5, sonraki: None
```

tee fonksiyonu, bir girdi iterable'dan çok sayıda bağımsız iterator döndürür. Bu durumda, prevs, items, ve nexts iteratorlerini döndürür.

chain fonksiyonu, tee tarafından döndürülen iteratorleri birleştirmek için kullanılır. İlk chain çağrısı, None ile prevs iteratorunu birleştirir ve ikinci chain çağrısı, nexts iteratorunu None ile birleştirir. Bu, girdi iterable'ının ilk elemanının previous değerinin None ve son elemanının next değerinin None olmasını sağlar.

Son olarak, zip fonksiyonu, üç iteratorü tuple'lar olarak birleştirmek için kullanılır. Sonuç iteratoru, (prev, item, nxt) şeklinde tuple'lar üretir, burada prev girdi iterable'ının önceki elemanıdır, item şuanki elemandır ve nxt sonraki elemandır.
