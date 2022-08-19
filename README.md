# Language-Codes
Language codes as an object in python.
<br/><br/>

An example of a usage:

```python
IncludedLanguagesA = []

IncludedLanguagesA += CheckLanguages("english")
IncludedLanguagesA += CheckLanguages("jApanese")
IncludedLanguagesA += CheckLanguages("Alsatian")

IncludedLanguagesB = []

IncludedLanguagesB += CheckLanguages("ger")
IncludedLanguagesB += CheckLanguages("hebrew")

Language = CheckLanguages("Alemannic")

if Language is not None:
  Language = Language[0]
  
  print("True" if (Language in IncludedLanguagesA) is True else "False")
  print("True" if (Language in IncludedLanguagesB) is True else "False")
  print("True" if CompareLanguages(Language, IncludedLanguagesA) is True else "False")
  print("True" if CompareLanguages(Language, Languages["Alsatian"]) is True else "False")
```

Which results in 4 prints:

1: "True" -> the language is included in the first included languages set.

2: "False" -> the language isn't included in the second included languages set.

3: "True" -> the language is included in the first included languages set (languages codes wise).

3: "True" -> the language is the same as the "Alsatian" language (languages codes wise).
<br/><br/>


Included the file "requirements_installation.bat" to install the packages from the requirements text file, from this other repo of mine:

https://github.com/xSpecialFoodx/Requirements-Manager
