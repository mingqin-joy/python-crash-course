favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edwaid': 'ruby',
    'phil': 'java',
    'jack': 'python',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")

for name, language in favorite_languages.items():
    print("\n name: " + name)
    print("language: " + language)

for name in favorite_languages:
    print(name.title())

for language in favorite_languages.keys():
    print(language.title())

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned: ")
for language in sorted(favorite_languages.values()):
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() +
              "'s favorite language is " + languages[0].title())
    else:
        print("\n" + name.title() + "'s favorite language are:")
        for language in languages:
            print("\t" + language.title())
