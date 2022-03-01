from babel import Locale

locale = Locale('en', 'US')
print(locale.territories['US'])
print('# Output in danish')
locale = Locale('en', 'US')
print(locale.territories['US'])

print('# Output lang country: ')
locale = Locale.parse('de_De')
print(locale.get_display_name('en_us'))

locale = Locale.parse('da_Dk')
print(locale.get_display_name('en_us'))

print('# Output CALENDER DAYS: ')
locale = Locale('en')
month_name = locale.months['format']['wide'].items()
print(list(month_name))

locale = Locale('da')
month_name = locale.months['format']['wide'].items()
print(list(month_name))

