import cv2
import pandas as pd
import os

from matplotlib import pyplot as plt
"""
vaizdo ikelimas
"""
# image = cv2.imread('roze.jpg')

"""
parodyti orginalu vaizda
"""
# cv2.imshow('Originalus vaizdas', image)
# cv2.waitKey(0)  # laukiama bet kokio klaviso paspaudimo
# cv2.destroyAllWindows()
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Pilku atspalviu vaizdas', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
atpazinti zmoniu veidus
"""

# def find_faces(image_path):
#     #ikeliame veidu atpazinimo modeli
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     #ikeliame vaizda ir pakeiciame i pilka atspalvi
#     img = cv2.imread(image_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#     # atrandame veidua vaizde
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#     return faces
#
#
# images_folder = 'C:/Users/GS/Pictures/zmoniu veidai'
# data = []
# # files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')] #pasitikriname, ar grazina failus
# # print(files)
#
# for filename in os.listdir(images_folder):
#     if filename.endswith('.jpg') or filename.endswith('.png'):
#         path = os.path.join(images_folder, filename)
#         faces = find_faces(path)
#         data.append({'filename': filename, 'faces_count': len(faces)})
#
#
# df = pd.DataFrame(data)
# # print(df)
# # average_faces = df['faces_count'].mean()
# # print(f'Vidutinis veidu skaicius vaizduose: {average_faces}')
#
# # surasti vaizda su didziausiu veidu skaiciumi
# max_faces = df.loc[df['faces_count'].idxmax()]
# # print(f'Daugiausiai veidu turintis vaizdas: {max_faces["filename"]}, veidu skaicius: {max_faces["faces_count"]}')
#
# df['faces_count'].plot(kind='hist', title="Veidu skaiciaus pasiskirstimas")
# plt.xlabel("Veidu skaicius")
# plt.ylabel("Vaizdu skaicius")
# plt.show()

"""

* Vaizdo Įkėlimas ir Rodymas
        Parašykite programą, kuri įkelia ir parodo vaizdą naudojant OpenCV. Eksperimentuokite su įvairiais vaizdais.
* Vaizdo Konvertavimas į Pilkus Atspalvius
        Modifikavus pirmąją programą, pridėkite funkcionalumą vaizdo konvertavimui į pilkus atspalvius prieš jį rodant.
* Vaizdo Išsaugojimas
        Įkelkite vaizdą, pakeiskite jį į pilkus atspalvius.
Modifikuokite veidų pavyzdį taip, kad galėtumėte eksperimentuoti su scaleFactor ir minNeighbors parametrais. 
Išbandykite skirtingas reikšmes ir stebėkite, kaip keičiasi veidų aptikimo rezultatai.

"""
# image = cv2.imread('pavasaris.jpg')

# cv2.imshow('Originalus vaizdas', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Pilku atspalviu vaizdas', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image = cv2.imread('drugelis.jpg')
# cv2.imshow('Originalus vaizdas', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('"Kitokio staspalvio vaizdas"', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def find_faces(image_path):
    #ikeliame veidu atpazinimo modeli
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #ikeliame vaizda ir pakeiciame i pilka atspalvi
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # atrandame veidua vaizde
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30)) #galima scaleFactor rasyti pvz. 1.75 arba 1.100
    for (x, y, w, h) in faces: #rodo aptiktu veidu 'kvadratukus'
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #255-spalva melyna, zalia, raudona, tada 2 -tai storis
    cv2.imshow('veidai', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return faces

#
images_folder = 'C:/Users/GS/Pictures/faces'
data = []
files = [f for f in os.listdir(images_folder) if f.endswith('.jpg') or f.endswith('.png')] #pasitikriname, ar grazina failus
# print(files)
# #
for filename in os.listdir(images_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        path = os.path.join(images_folder, filename)
        faces = find_faces(path)
        data.append({'filename': filename, 'faces_count': len(faces)})


df = pd.DataFrame(data)
# print(df)
average_faces = df['faces_count'].mean()
print(f'Vidutinis veidu skaicius vaizduose: {average_faces}')

#surasti vaizda su didziausiu veidu skaiciumi
max_faces = df.loc[df['faces_count'].idxmax()]
# print(f'Daugiausiai veidu turintis vaizdas: {max_faces["filename"]}, veidu skaicius: {max_faces["faces_count"]}')

df['faces_count'].plot(kind='hist', title="Veidu skaiciaus pasiskirstimas")
plt.xlabel("Veidu skaicius")
plt.ylabel("Vaizdu skaicius")
plt.show()
