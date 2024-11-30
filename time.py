import time

for soat in range(0, 24):
    for minut in range(0, 60):
        for sekund in range(0, 60):
            print(f"\r{soat:02}:{minut:02}:{sekund:02}", end="")
            time.sleep(0.5)