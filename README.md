
## 🔍 Description

The script interprets a password as a large integer and checks if it is a **probable prime number** using the **Miller-Rabin Primality Test** — a fast, probabilistic algorithm used in cryptography. If the number is prime, it's considered "complex."

## 🧪 Usage

Run the script with Python:

```bash
python password_complexity.py
```

### Input

* A number (simulating a password in numeric form).
* Number of testing rounds (`k`) to increase test accuracy.

### Example

```
Enter a number to check prime: 982451653
Enter testing rounds: 5
982451653 is prime
```

This implies the "password" is complex.

## 💡 How It Works

* Converts the "password" to a number (you could map characters to digits if needed).
* Runs the **Miller-Rabin** test:

  * Decomposes the number as `2^s * d`.
  * Tests `k` random bases for primality.
  * Determines if the number passes all rounds.

## 📦 Requirements

* Python 3.x
* No external libraries

## 🧠 Logic Summary

```python
miller(n, k)
```

Returns `True` if `n` is probably prime (complex), or `False` if it's definitely not prime (not complex).

## 📁 File Structure

```
password_complexity.py     # Main script
```

## 🔧 Customization

Want to use this logic in another app?

```python
from password_complexity import miller

is_complex = miller(your_number, 5)
```

## 🤔 Fun Use Cases

* Educational tool for understanding primality tests.
* Fun "complexity" test for numeric passwords.
* Cryptographic experiments.


