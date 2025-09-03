
def sing():
    lyrics = []

    lyrics += ["let it be,"] * 4

    lyrics.append("there will be an answer,")

    lyrics += ["let it be,"] * 5

    lyrics.append("whisper words of wisdom, let it be")

    song = "\n".join(lyrics)
    return song

print(sing())
