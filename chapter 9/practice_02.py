def game():
    return 110

score = game()
with open ("hiscore.txt") as f:
    hiScoreStr = int(f.read())
if hiScoreStr =='':
    with open ("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score:
    with open ("hiscore.txt", "w") as f:
        f.write(str(score))


