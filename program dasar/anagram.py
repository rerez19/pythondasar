kata1 = str(input("Masukkan kata pertama: "))
kata2 = str(input("Masukkan kata kedua: "))


kata1 = kata1.lower()
kata2 = kata2.lower()


if (len(kata1)==len(kata2)):
  sorted_kata1 = sorted(kata1)
  sorted_kata2 = sorted(kata2)


  if (sorted_kata1 == sorted_kata2):
    print(f"{kata1} dan {kata2} adalah anagram")
  else:
    print(f"{kata1} dan {kata2} bukan anagram")
else:
  print(f"{kata1} dan {kata2} bukan anagram")