import fresh_tomatoes
import mediax

PET_Physics = mediax.Movie("IAEA/EANM webinar - Basic PET physics and ","PET",
                      "https://humanhealth.iaea.org/HHW/NuclearMedicine/resources/images/2-WorkstationEBW.jpg",
                      "https://youtu.be/PNIUGBUBMfU")
#print(iaea_RP.storyline)
#iaea_RP.show_trailer()

RP = mediax.Movie("Radioactivity & Nuclear Medicine","How to protect patients who undergoinig DSA",
                      "https://humanhealth.iaea.org/HHW/NuclearMedicine/resources/images/2-WorkstationEBW.jpg",
                      "https://youtu.be/0CLLao-D37E")

Radioactive_NM = mediax.Movie("Radioactivity & Nuclear Medicine","Nuclear Medicine",
                      "https://humanhealth.iaea.org/HHW/NuclearMedicine/resources/images/2-WorkstationEBW.jpg",
                      "https://youtu.be/2vVVfrPHoTs")

PET_CT_QC = mediax.Movie("Daily PET CT QC tests","Quality Control of PET/CT",
                      "https://humanhealth.iaea.org/HHW/NuclearMedicine/resources/images/2-WorkstationEBW.jpg",
                      "https://youtu.be/PNIUGBUBMfU")

X_Ray_QC = mediax.Movie("Diagnostic Radiology Quality Control","Quality Control of Conventional X-Ray",
                      "https://humanhealth.iaea.org/HHW/NuclearMedicine/resources/images/2-WorkstationEBW.jpg",
                      "https://youtu.be/lAKc-Tj88_k")

CT_QA = mediax.Movie("Computed tomography: Standard QA procedures","Quality Control of CT",
                      "https://humanhealth.iaea.org/HHW/NuclearMedicine/resources/images/2-WorkstationEBW.jpg",
                      "https://youtu.be/Jn1NQG03cgM")

SPECT_CT_QA = mediax.Movie("SPECT/CT Basic information , QA and applications","Quality Control of SPECT/CT",
                      "https://humanhealth.iaea.org/HHW/NuclearMedicine/resources/images/2-WorkstationEBW.jpg",
                      "https://youtu.be/qejQkmvjBdc")

 
webinars=[PET_Physics,RP,Radioactive_NM,PET_CT_QC,X_Ray_QC,CT_QA,SPECT_CT_QA]
fresh_tomatoes.open_movies_page(webinars)
