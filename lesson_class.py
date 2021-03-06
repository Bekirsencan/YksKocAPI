import db_les
from flask import Response
from encoder import JSONEncoder
from bson.objectid import ObjectId
import pprint
import json



class json_lessons:

    def __init__(self):
        super().__init__()
        self.les = db_les.lessons.get_instance()
        self.json_ayt_data = {}
        self.json_tyt_data = {}
        self.response_data = {}
        self.ayt_list = []
        self.tyt_list = []
        self._id = None
        self.json_ayt_matematik = json_ayt_matematik_class
        self.json_ayt_geometri = json_ayt_geometri_class
        self.json_ayt_edebiyat = json_ayt_edebiyat_class
        self.json_ayt_fizik = json_ayt_fizik_class
        self.json_ayt_kimya = json_ayt_kimya_class
        self.json_ayt_biyoloji = json_ayt_biyoloji_class
        self.json_ayt_tarih = json_ayt_tarih_class
        self.json_ayt_cografya = json_ayt_cografya_class
        self.json_ayt_felsefe = json_ayt_felsefe_class

        self.json_tyt_matematik = json_tyt_matematik_class
        self.json_tyt_geometri = json_tyt_geometri_class
        self.json_tyt_turkce = json_tyt_turkce_class
        self.json_tyt_fizik = json_tyt_fizik_class
        self.json_tyt_kimya = json_tyt_kimya_class
        self.json_tyt_biyoloji = json_tyt_biyoloji_class
        self.json_tyt_tarih = json_tyt_tarih_class
        self.json_tyt_cografya = json_tyt_cografya_class
        self.json_tyt_felsefe = json_tyt_felsefe_class

    def send_response(self,object_id):
        self.set_objectId(object_id)
        return Response(JSONEncoder().encode(self.response_data),mimetype='application/json')

    def set_objectId(self,object_id):
        self._id = object_id
        self.get_json_data()
    
    def get_json_data(self):
        json_data = self.les.get_json_from_database(self._id)
        self.json_ayt_data = json_data.get("ayt")
        self.json_tyt_data = json_data.get("tyt")
        self.set_response_data()

    def set_response_data(self):
       self.set_ayt_subjects()
       self.set_tyt_subjects()
       self.set_ayt_list()
       self.set_tyt_list()
       self.response_data["_id"] = self._id
       self.response_data["ayt"] = self.ayt_list
       self.response_data["tyt"] = self.tyt_list


    def set_ayt_subjects(self):
        self.json_ayt_matematik["subject_state"] = self.json_ayt_data.get("matematik")
        self.json_ayt_geometri["subject_state"] = self.json_ayt_data.get("geometri")
        self.json_ayt_edebiyat["subject_state"] = self.json_ayt_data.get("edebiyat")
        self.json_ayt_fizik["subject_state"] = self.json_ayt_data.get("fizik")
        self.json_ayt_kimya["subject_state"] = self.json_ayt_data.get("kimya")
        self.json_ayt_biyoloji["subject_state"] = self.json_ayt_data.get("biyoloji")
        self.json_ayt_tarih["subject_state"] = self.json_ayt_data.get("tarih")
        self.json_ayt_cografya["subject_state"] = self.json_ayt_data.get("cografya")
        self.json_ayt_felsefe["subject_state"] = self.json_ayt_data.get("felsefe & din k??lt??r??")

    def set_tyt_subjects(self):
        self.json_tyt_matematik["subject_state"] = self.json_tyt_data.get("matematik")
        self.json_tyt_geometri["subject_state"] = self.json_tyt_data.get("geometri")
        self.json_tyt_turkce["subject_state"] = self.json_tyt_data.get("turkce")
        self.json_tyt_fizik["subject_state"] = self.json_tyt_data.get("fizik")
        self.json_tyt_kimya["subject_state"] = self.json_tyt_data.get("kimya")
        self.json_tyt_biyoloji["subject_state"] = self.json_tyt_data.get("biyoloji")
        self.json_tyt_tarih["subject_state"] = self.json_tyt_data.get("tarih")
        self.json_tyt_cografya["subject_state"] = self.json_tyt_data.get("cografya")
        self.json_tyt_felsefe["subject_state"] = self.json_tyt_data.get("felsefe & din k??lt??r??")
    
    def set_ayt_list(self):
        self.ayt_list.append(self.json_ayt_matematik)
        self.ayt_list.append(self.json_ayt_geometri)
        self.ayt_list.append(self.json_ayt_edebiyat)
        self.ayt_list.append(self.json_ayt_fizik)
        self.ayt_list.append(self.json_ayt_kimya)
        self.ayt_list.append(self.json_ayt_biyoloji)
        self.ayt_list.append(self.json_ayt_tarih)
        self.ayt_list.append(self.json_ayt_cografya)
        self.ayt_list.append(self.json_ayt_felsefe)

    def set_tyt_list(self):
        self.tyt_list.append(self.json_tyt_matematik)
        self.tyt_list.append(self.json_tyt_geometri)
        self.tyt_list.append(self.json_tyt_turkce)
        self.tyt_list.append(self.json_tyt_fizik)
        self.tyt_list.append(self.json_tyt_kimya)
        self.tyt_list.append(self.json_tyt_biyoloji)
        self.tyt_list.append(self.json_tyt_tarih)
        self.tyt_list.append(self.json_tyt_cografya)
        self.tyt_list.append(self.json_tyt_felsefe)

    def new_user(self,object_id):
        json_data = {
            "_id":ObjectId(object_id),
            "ayt":{
                "matematik":"0000000000000000000000000000000",
                "geometri":"0000000000000000000000000000000",
                "edebiyat":"0000000000000000000",
                "fizik":"000000000000000000000000000000000",
                "kimya":"000000000000000000000",
                "biyoloji":"0000000000000000000000000000",
                "tarih":"0000000000000000000000000000",
                "cografya":"0000000000000000000000000000000000",
                "felsefe & din k??lt??r??":"00000000000000000000000000000000"
            },
            "tyt":{
                "matematik":"0000000000000000000000",
                "geometri":"000000000000000000000000",
                "turkce":"00000000000000000000000000",
                "fizik":"000000000000",
                "kimya":"0000000000",
                "biyoloji":"0000000000",
                "tarih":"000000000000000000000",
                "cografya":"0000000000000000000",
                "felsefe & din k??lt??r??":"000000000000000000"
            }        
        }
        return self.les.set_new_user(json_data) 

json_ayt_matematik_class = {
    "lesson_name": "matematik",
    "subjects":[
        "Temel Kavramlar","Say?? Basamaklar??","B??lme ve B??l??nebilme","EBOB ??? EKOK","Rasyonel Say??lar","Basit E??itsizlikler","Mutlak De??er",
        "??sl?? Say??lar","K??kl?? Say??lar","??arpanlara Ay??rma","Oran Orant??","Denklem ????zme","Problemler",
        "K??meler","Kartezyen ??arp??m","Mant??k","Fonskiyonlar","Polinomlar","2.Dereceden Denklemler","Perm??tasyon ve Kombinasyon",
        "Olas??l??k","??statistik","Karma????k Say??lar","2.Dereceden E??itsizlikler","Parabol","Trigonometri","Logaritma","Diziler","Limit","T??rev","??ntegral",
    ],
    "subject_state": "0000000000000000000000000000000"
}

json_tyt_matematik_class = {
    "lesson_name":"matematik",
    "subjects":[
        "Temel Kavramlar","Say?? Basamaklar??","B??lme ve B??l??nebilme","EBOB ??? EKOK","Rasyonel Say??lar","Basit E??itsizlikler","Mutlak De??er",
        "??sl?? Say??lar","K??kl?? Say??lar","??arpanlara Ay??rma","Oran Orant??","Denklem ????zme","Problemler",
        "K??meler","Kartezyen ??arp??m","Mant??k","Fonskiyonlar","Polinomlar","2.Dereceden Denklemler","Perm??tasyon ve Kombinasyon",
        "Olas??l??k","??statistik"
        ],
        "subject_state":"0000000000000000000000"
}

json_ayt_geometri_class = {
    "lesson_name": "geometri",
    "subjects": [
        "Temel Kavramlar","Do??ruda A????lar","????gende A????lar","??zel ????genler","Dik ????gen","??kizkenar ????gen",
        "E??kenar ????gen","A????ortay","Kenarortay","????gende Alan","????gende Benzerlik","A???? Kenar Ba????nt??lar??","??okgenler",
        "D??rtgenler","Deltoid","Paralelkenar","E??kenar D??rtgen","Dikd??rtgen","Kare","??kizkenar","Yamuk","Noktan??n Analiti??i",
        "Prizmalar","Piramitler","Do??runun Analiti??i","??ember ve Daire","Silindir","Koni","K??re","D??n??????m Geometrisi","??emberin Analiti??i"
        ],
    "subject_state": "0000000000000000000000000000000"
}

json_tyt_geometri_class = {
    "lesson_name": "geometri",
    "subjects": [
        "Temel Kavramlar","Do??ruda A????lar","????gende A????lar","??zel ????genler","Dik ????gen","??kizkenar ????gen",
        "E??kenar ????gen","A????ortay","Kenarortay","????gende Alan","????gende Benzerlik","A???? Kenar Ba????nt??lar??","??okgenler",
        "D??rtgenler","Deltoid","Paralelkenar","E??kenar D??rtgen","Dikd??rtgen","Kare","??kizkenar","Yamuk","Noktan??n Analiti??i",
        "Prizmalar","Piramitler"
        ],
    "subject_state":"000000000000000000000000"
}

json_ayt_edebiyat_class = {
    "lesson_name": "edebiyat",
    "subjects": [
        "Anlam Bilgisi","Dil Bilgisi","G??zel Sanatlar ve Edebiyat","Metinlerin S??n??fland??r??lmas??","??iir Bilgisi",
        "Edebi Sanatlar","T??rk Edebiyat?? D??nemleri","??slamiyet ??ncesi T??rk Edebiyat?? ve Ge??i?? D??nemi","Halk Edebiyat??","Divan Edebiyat??",
        "Tanzimat Edebiyat??","Servet-i F??nun Edebiyat??","Fecr-i Ati Edebiyat??","??Milli Edebiyat","Cumhuriyet ??iiri","Cumhuriyet Roman??",
        "Cumhuriyet D??nemi","Edebiyat Ak??mlar??","D??nya Edebiyat??"
        ],
    "subject_state": "0000000000000000000",
    "lesson_name": "edebiyat",
    "subjects": [
        "Anlam Bilgisi","Dil Bilgisi","G??zel Sanatlar ve Edebiyat","Metinlerin S??n??fland??r??lmas??","??iir Bilgisi",
        "Edebi Sanatlar","T??rk Edebiyat?? D??nemleri","??slamiyet ??ncesi T??rk Edebiyat?? ve Ge??i?? D??nemi","Halk Edebiyat??","Divan Edebiyat??",
        "Tanzimat Edebiyat??","Servet-i F??nun Edebiyat??","Fecr-i Ati Edebiyat??","??Milli Edebiyat","Cumhuriyet ??iiri","Cumhuriyet Roman??",
        "Cumhuriyet D??nemi","Edebiyat Ak??mlar??","D??nya Edebiyat??"
        ],
}

json_tyt_turkce_class = {
    "lesson_name": "turkce",
    "subjects": [
        "S??zc??kte Anlam","S??z Yorumu","Deyim ve Atas??z??","C??mlede Anlam","Paragrafta Anlam","Paragrafta Anlat??m Teknikleri","Paragrafta Konu-Ana D??????nce",
        "Paragrafta Yap??","Paragrafta Yard??mc?? D??????nce","Ses Bilgisi","Yaz??m Kurallar??","Noktalama ????aretleri","S??zc??kte Yap??","S??zc??k T??rleri","??simler",
        "Zamirler","S??fatlar","Zarflar","Edat - Ba??la?? - ??nlem","Fiil, Ek Fiil, Fiilimsi","S??zc??k Gruplar??","C??mlenin ????eleri","C??mle T??rleri","Anlat??m Bozuklu??u"
    ],
    "subject_state":"00000000000000000000000000"
}

json_ayt_fizik_class = {
    "lesson_name":"fizik",
    "subjects":[
        "Fizik Bilimine Giri??","Madde ve ??zellikleri","S??v??lar??n Kald??rma Kuvveti","Bas??n??","Is??, S??cakl??k ve Genle??me","Hareket",
        "Dinamik","????, G???? ve Enerji","Elektrik","Optik","Manyetizma","Dalgalar","Vekt??rler","Kuvvet, Tork ve Denge","K??tle Merkezi",
        "Basit Makineler","Hareket","Newton???un Hareket Yasalar??","????, G???? ve Enerji II","At????lar","??tme ve Momentum","Elektrik Alan ve Potansiyel",
        "Paralel Levhalar ve S????a","Manyetik Alan ve Manyetik Kuvvet","??nd??ksiyon, Alternatif Ak??m ve Transformat??rler","??embersel Hareket",
        "K??tle ??ekim ve Kepler Yasalar??","Basit Harmonik Hareket","Dalga Mekani??i ve Elektromanyetik Dalgalar","Atom Modelleri","B??y??k Patlama ve Radyoaktivite",
        "Modern Fizik","Modern Fizi??in Teknolojideki Uygulamalar??"
        ],
    "subject_state":"000000000000000000000000000000000"
}

json_tyt_fizik_class = {
    "lesson_name":"fizik",
    "subjects":[
        "Fizik Bilimine Giri??","Madde ve ??zellikleri","S??v??lar??n Kald??rma Kuvveti","Bas??n??","Is??, S??cakl??k ve Genle??me","Hareket",
        "Dinamik","????, G???? ve Enerji","Elektrik","Optik","Manyetizma","Dalgalar"
    ],
    "subject_state":"000000000000"
}

json_ayt_kimya_class = {
    "lesson_name":"kimya",
    "subjects":[
        "Kimya Bilimi","Atom ve Periyodik Sistem","Kimyasal T??rler Aras?? Etkile??imler","Kimyasal Hesaplamalar","Kimyan??n Temel Kanunlar??",
        "Asit, Baz ve Tuz","Maddenin Halleri","Kar??????mlar","Do??a ve Kimya","Kimya Her Yerde","Modern Atom Teorisi","Gazlar","????zeltiler",
        "Kimyasal Tepkimelerde Enerji","Kimyasal Tepkimelerde H??z","Kimyasal Tepkimelerde Denge","Asit-Baz Dengesi","????z??n??rl??k Dengesi",
        "Kimya ve Elektrik","Karbon Kimyas??na Giri??","Organik Kimya"
        ],
    "subject_state":"000000000000000000000"
}

json_tyt_kimya_class = {
    "lesson_name":"kimya",
    "subjects":[
        "Kimya Bilimi","Atom ve Periyodik Sistem","Kimyasal T??rler Aras?? Etkile??imler","Kimyasal Hesaplamalar","Kimyan??n Temel Kanunlar??",
        "Asit, Baz ve Tuz","Maddenin Halleri","Kar??????mlar","Do??a ve Kimya","Kimya Her Yerde"
    ],
    "subject_state":"0000000000"
}

json_ayt_biyoloji_class = {
    "lesson_name":"biyoloji",
    "subjects":[
            "Canl??lar??n Ortak ??zellikleri","Canl??lar??n Temel Bile??enleri","H??cre ve Organelleri","H??cre Zar??ndan Madde Ge??i??i","Canl??lar??n S??n??fland??r??lmas??",
            "Mitoz ve E??eysiz ??reme","Mayoz ve E??eyli ??reme","Kal??t??m","Ekosistem Ekolojisi","G??ncel ??evre Sorunlar??","Sinir Sistemi","Endokrin Sistem",
            "Duyu Organlar??","Destek ve Hareket Sistemi","Sindirim Sistemi","Dola????m ve Ba????????kl??k Sistemi","Solunum Sistemi","Bo??alt??m Sistemi","??riner Sistem",
            "??reme Sistemi ve Embriyonik Geli??im","Kom??nite ve Pop??lasyon Ekolojisi","N??kleik Asitler","Genetik ??ifre ve Protein Sentezi","Canl??l??k ve Enerji",
            "Fotosentez ve Kemosentez","H??cresel Solunum","Bitki Biyolojisi","Canl??lar ve ??evre"
            ],
    "subject_state":"0000000000000000000000000000"
}

json_tyt_biyoloji_class = {
    "lesson_name":"biyoloji",
    "subjects":[
            "Canl??lar??n Ortak ??zellikleri","Canl??lar??n Temel Bile??enleri","H??cre ve Organelleri","H??cre Zar??ndan Madde Ge??i??i","Canl??lar??n S??n??fland??r??lmas??",
            "Mitoz ve E??eysiz ??reme","Mayoz ve E??eyli ??reme","Kal??t??m","Ekosistem Ekolojisi","G??ncel ??evre Sorunlar??"
    ],
    "subject_state":"0000000000"
}

json_ayt_tarih_class = {
    "lesson_name":"tarih",
    "subjects":[
        "Tarih Bilimi","??lk Uygarl??klar","??lk T??rk Devletleri","??slam Tarihi ve Uygarl??????","T??rk-??slam Devletleri","Orta ??a?? ve Avrupa Tarihi",
        "T??rkiye Tarihi","Beylikten Devlete (1300-1453)","D??nya G??c??: Osmanl?? Devleti (1453-1600)","Osmanl?? K??lt??r ve Medeniyeti","Yeni ve Yak??n ??a??da Avrupa Tarihi",
        "Aray???? Y??llar?? (17. Y??zy??l)","Yeni ??a??da Avrupa","En Uzun Y??zy??l (1800-1922)","20. Y??zy??l Ba??lar??nda Osmanl?? Devleti",
        "1. D??nya Sava???? ??? Milli M??cadeleye Haz??rl??k D??nemi","Kurtulu?? Sava???? ve Antla??malar","I. TBMM D??nemi","T??rk ??nk??lab??","Atat??rk????l??k ve Atat??rk ??lkeleri",
        "T??rk D???? Politikas??","Atat??rk?????n ??l??m??","20. yy Ba??lar??nda D??nya","??kinci D??nya Sava????","So??uk Sava?? D??nemi","Yumu??ama D??nemi ve Sonras??","K??reselle??en D??nya",
        "XXI. Y??zy??l??n E??i??inde T??rkiye ve D??nya"
        ],
    "subject_state":"0000000000000000000000000000"
}

json_tyt_tarih_class = {
    "lesson_name":"tarih",
    "subjects":[
        "Tarih Bilimi","??lk Uygarl??klar","??lk T??rk Devletleri","??slam Tarihi ve Uygarl??????","T??rk-??slam Devletleri","Orta ??a?? ve Avrupa Tarihi",
        "T??rkiye Tarihi","Beylikten Devlete (1300-1453)","D??nya G??c??: Osmanl?? Devleti (1453-1600)","Osmanl?? K??lt??r ve Medeniyeti","Yeni ve Yak??n ??a??da Avrupa Tarihi",
        "Aray???? Y??llar?? (17. Y??zy??l)","Yeni ??a??da Avrupa","En Uzun Y??zy??l (1800-1922)","20. Y??zy??l Ba??lar??nda Osmanl?? Devleti",
        "1. D??nya Sava???? ??? Milli M??cadeleye Haz??rl??k D??nemi","Kurtulu?? Sava???? ve Antla??malar","I. TBMM D??nemi","T??rk ??nk??lab??","Atat??rk????l??k ve Atat??rk ??lkeleri",
        "T??rk D???? Politikas??"
        ],
    "subject_state":"000000000000000000000"
}

json_ayt_cografya_class = {
    "lesson_name":"cografya",
    "subjects":[
        "Do??a ve ??nsan","D??nya???n??n ??ekli ve Hareketleri","Co??rafi Konum","Harita Bilgisi","Atmosfer ve S??cakl??k","??klimler",
        "Bas??n?? ve R??zgarlar","Nem, Ya?????? ve Buharla??ma","???? Kuvvetler / D???? Kuvvetler","Su ??? Toprak ve Bitkiler","N??fus","G????","Yerle??me",
        "T??rkiye???nin Yer ??ekilleri","Ekonomik Faaliyetler","B??lgeler","Uluslararas?? Ula????m Hatlar??","??evre ve Toplum","Do??al Afetler","Ekosistem",
        "Do??adaki Ekstrem Olaylar","??lk Medeniyet ve ??ehirler","N??fus Politikalar??","??T??rkiye???de N??fus ve Yerle??me","Ekonomik Faaliyetler","G???? ve ??ehirle??me",
        "T??rkiye Ekonomisi","T??rkiye???nin Jeopolitik Konumu","B??lgesel Kalk??nma Projeleri","??klim ve Yer ??ekilleri","??lkeler Aras?? Etkile??im","K??resel ve B??lgesel ??rg??tler",
        "??retim Alanlar?? ve Ula????m A??lar??","B??lgeler ve ??lkeler"
        ],
    "subject_state":"0000000000000000000000000000000000"
}

json_tyt_cografya_class = {
    "lesson_name":"cografya",
    "subjects":[
        "Do??a ve ??nsan","D??nya???n??n ??ekli ve Hareketleri","Co??rafi Konum","Harita Bilgisi","Atmosfer ve S??cakl??k","??klimler",
        "Bas??n?? ve R??zgarlar","Nem, Ya?????? ve Buharla??ma","???? Kuvvetler / D???? Kuvvetler","Su ??? Toprak ve Bitkiler","N??fus","G????","Yerle??me",
        "T??rkiye???nin Yer ??ekilleri","Ekonomik Faaliyetler","B??lgeler","Uluslararas?? Ula????m Hatlar??","??evre ve Toplum","Do??al Afetler"
    ],
    "subject_state":"0000000000000000000"
}

json_ayt_felsefe_class = {
    "lesson_name":"felsefe & din k??lt??r??",
    "subjects":[
        "Felsefe???nin Konusu","Bilgi Felsefesi","Varl??k Felsefesi","Ahlak Felsefesi","Sanat Felsefesi","Din Felsefesi","Siyaset Felsefesi","Bilim Felsefesi",
        "Mant????a Giri??","Klasik Mant??k","Mant??k ve Dil","Sembolik Mant??k","Psikoloji Bilimini Tan??yal??m","Psikolojinin Temel S??re??leri","????renme Bellek D??????nme",
        "Ruh Sa??l??????n??n Temelleri","Sosyolojiye Giri??","Birey ve Toplum","Toplumsal Yap??","Toplumsal De??i??me ve Geli??me","Toplum ve K??lt??r","Toplumsal Kurumlar",
        "Bilgi ve ??nan??","??slam ve ??badet","Ahlak ve De??erler","Allah ??nsan ??li??kisi","Hz. Muhammed (S.A.V.)","Vahiy ve Ak??l","??slam D??????ncesinde Yorumlar, Mezhepler",
        "Din, K??lt??r ve Medeniyet","??slam ve Bilim, Estetik, Bar????","Ya??ayan Dinler"
        ],
    	"subject_state":"00000000000000000000000000000000"
}

json_tyt_felsefe_class = {
    "lesson_name":"felsefe & din k??lt??r??",
    "subjects":[
        "Felsefe???nin Konusu","Bilgi Felsefesi","Varl??k Felsefesi","Ahlak Felsefesi","Sanat Felsefesi","Din Felsefesi","Siyaset Felsefesi","Bilim Felsefesi",
        "Bilgi ve ??nan??","??slam ve ??badet","Ahlak ve De??erler","Allah ??nsan ??li??kisi","Hz. Muhammed (S.A.V.)","Vahiy ve Ak??l","??slam D??????ncesinde Yorumlar, Mezhepler",
        "Din, K??lt??r ve Medeniyet","??slam ve Bilim, Estetik, Bar????","Ya??ayan Dinler"
        ],
        "subject_state":"000000000000000000"
}




