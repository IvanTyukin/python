"""
5. С начала 2010 года прошло n  месяцев и 2 дня (n >=1). Определить 
название месяца (январь, февраль и т.п.) этого дня.
"""

n = int(input())

months = ['янв','фев','март','апр','май','июнь','июль','авг','сен','окт','ноя','дек']

print(months[n % 12])