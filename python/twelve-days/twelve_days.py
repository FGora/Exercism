def recite(start_verse, end_verse):
    lyrics= []
    for versenumber in range(start_verse,end_verse+1):
        lyrics.append(resiteVerse(versenumber))
    return lyrics

def resiteVerse(versenumber):
    days = [["first",""], ["second", "two Turtle Doves, "], ["third", "three French Hens, "], ["fourth", "four Calling Birds, "], ["fifth", "five Gold Rings, "], ["sixth", "six Geese-a-Laying, "], ["seventh", "seven Swans-a-Swimming, "], ["eighth","eight Maids-a-Milking, "], ["ninth", "nine Ladies Dancing, "], ["tenth","ten Lords-a-Leaping, "], ["eleventh","eleven Pipers Piping, "], ["twelfth","twelve Drummers Drumming, "]]
    verse = "On the "
    verse = verse + days[versenumber-1][0]
    verse= verse + " day of Christmas my true love gave to me: "
    for day in range(versenumber-1):
        verse = verse + days[versenumber-day-1][1]
    if versenumber == 1:
        verse = verse + "a Partridge in a Pear Tree."
    elif versenumber >=2:
        verse = verse + "and a Partridge in a Pear Tree."
    return verse