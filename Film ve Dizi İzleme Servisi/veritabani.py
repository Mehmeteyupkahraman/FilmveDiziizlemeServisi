import sqlite3

class Veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='filmler'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kullanicilar (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciadi TEXT, sifre TEXT, ad TEXT, soyad TEXT, telefon TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS filmler (ID INTEGER PRIMARY KEY AUTOINCREMENT, ad TEXT, yonetmen TEXT, tur TEXT, yapim_yili INTEGER, sure INTEGER, yapim_yeri TEXT, fotograf TEXT, aciklama TEXT, fragman TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS filmlistem (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciid INTEGER, filmid INTEGER)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS yorumlar (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciid INTEGER, filmid INTEGER, yorum TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS filmicerik (ID INTEGER PRIMARY KEY AUTOINCREMENT, filmid INTEGER, sahne INTEGER, icerik TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS izleme_gecmisi (ID INTEGER PRIMARY KEY AUTOINCREMENT, filmid INTEGER, kullaniciid INTEGER, izleme_tarihi TIMESTAMP)')

            filmler_tuple = [
                ("Matrix", "Lana Wachowski, Lilly Wachowski", "Bilim Kurgu", 1999, 136, "ABD", "matrix.jpg", "Neo, normal bir hayat süren bir yazılım mühendisidir. Ancak hayatı,gizemli bir şekilde Morpheus adında bir adamla tanışmasıyla tamamen değişir. Morpheus , Neo'ya gerçek dünyanın aslında insanların yaşadığı dünyadan çok farklı olduğunu,insanlığın gerçekliğinin Matrix adı verilen bir bilgisayar simülasyonunda olduğunu açıklar.Morpheus,Neo'nun bu simülasyondan kurtulabilmesi için bir seçeneği olduğunu ve Neo'nun Uyaniş adı verilen bu süreci yaşaması gerektiğini söyler. Neo, Morpheus'un rehberliğinde Matrix ten kaçmaya ve gerçekleri arar.", "m8e-FF8MsqU"),
                ("Baba", "Francis Ford Coppola", "Drama", 1972, 175, "ABD", "baba.jpg", "Film, New York'un suç dünyasında yükselen ve ailesi için güçlü bir gelecek kurmaya çalışan İtalyan asıllı Amerikalı mafya lideri Don Vito Corleone'nin hikayesini anlatır. Corleone ailesi, sadakat, güç ve aile bağları üzerine kurulmuş bir suç imparatorluğunun başında bulunmaktadır.Hikaye, Don Vito'nun oğlu Michael Corleone'nin, aile işlerine karışmak istemeyen bir asker olarak başlayıp, acımasız bir lider haline dönüşümünü takip eder. Don Vito'nun düşmanları tarafından suikasta uğramasıyla, Michael ailenin liderliğini devralmak zorundadır.", "UaVTIH8mujA"),
                ("Yeşil Yol", "Frank Darabont", "Drama", 1999, 189, "ABD", "yesil.jpg", "Yeşil Yol, Louisiana da bulunan Cold Mountain Hapishanesinde çalışan gardiyan Paul Edgecombun hikayesini anlatır. Paul, devasa yapılı ama ruhsal olarak saf ve masum olduğuna inandığı mahkum John Coffeyin idamını beklemektedir. Johnun olağanüstü yetenekleri ve masumiyeti, Paulun ve diğer gardiyanların onu sorgulamalarına neden olur. Film, Johnun masumiyeti ve insan doğasının karmaşıklığını işlerken, umut, iyilik ve adalet temalarını derinlemesine inceler.", "hfa5F-kRTq4"),
                ("Kara Şövalye", "Christopher Nolan", "Aksiyon", 2008, 152, "ABD", "kara.jpg", "Batman, Teğmen Jim Gordon ve Bölge Savcısı Harvey Dent’in yardımlarıyla, şehir sokaklarını sarmış olan suç örgütlerinden geriye kalanları temizlemeye girişir. Bu ortaklığın etkili olduğu açıktır, ama ekip kısa süre sonra kendilerini, Joker olarak bilinen ve Gotham şehri sakinlerini daha önce de dehşete boğmuş olan suç dehasının yarattığı karmaşanın ortasında bulurlar.Batman, Joker'in yarattığı karmaşık olaylarla başa çıkmak zorundadır. Bu süreçte, Gotham'ın Savcısı Harvey Dent (Aaron Eckhart) ile birlikte çalışarak suçla mücadele etmeye çalışır.", "EXeTwQWrcwY"),
                ("Başlangıç", "Christopher Nolan", "Bilim Kurgu", 2010, 148, "ABD", "baslangic.jpg", "Leonardo DiCaprio bu yapımda, çok yetenekli bir hırsız olan Dom Cobb ile karşımızda. Uzmanlık alanı, zihnin en karanlık ve savunmasız olduğu rüya anında, bilinçaltının derinliklerindeki değerli sırları çekip çıkarmak ve onları çalmaktır. Cobb'un insanlarda nadiren görülebilecek bu yeteneği onu kurumsal casusluğun tehlikeli yeni dünyasında aranan bir oyuncu yapmıştır. Aynı zamanda bu durum onu uluslararası bir kaçak yapmış ve sevdiği her şeye malolmuştur. Cobb'a içinde bulunduğu durumdan kurtulmasını sağlayacak bir fırsat sunulur.", "YoHD9XEInc0"),
                ("Dövüş Kulübü", "David Fincher", "Drama", 1999, 139, "ABD", "dovus.jpg", "Dövüş kulübünün ilk kuralı, dövüş kulübü hakkında konuşmamaktır. Dövüş kulübünün ikinci kuralı da, kulüp hakkında konuşmamaktır... Filmin baş kişisi, sıradan hayatının girdaplarında bunalımlar geçiren bir sigorta müfettişi olan Jack, Kanserli olmadığı halde, uykusuzluğunu yenmek ve hayatına anlam katmak adına, kanserlilere moral destek sağlayan terapi gruplarına katılır. Orada, Marla Singer adlı bir kızla garip bir yakınlık kurar. Bir iş gezisi dönüşü ise, Tyler Durden adlı egzantrik karakterle tanışır. Durden, Jack'in olmak isteyip de olamadığı adamdır", "SHH9UZlKid0"),
                ("Uzay Yolcuları", "Morten Tyldum", "Bilim Kurgu", 2016, 116, "ABD", "uzay.jpg", "Starship Avalon adlı uzay gemisi, Homestead II adında çok uzak bir koloniye 5000'den fazla kişiyi götürmek üzere, 120 yıl sürecek bir yolculuk yapmaktadır. Giden kişiler bu yolculuk sonunda sağlıklı bir şekilde hayatlarına devam edebilmek için özel tasarlanmış uyku kapsüllerinde uyutulmaktadırlar. Ancak yaşanan teknik bir sorun nedeniyle iki kapsül vaktinden önce açılır, birinde makine mühendisi Jim Preston (Chris Pratt), diğerinde ise yazar Aurora Lane (Jennifer Lawrence) bulunmaktadır. Gemide bir başlarına kalan ikilinin önünde, hala 90 yıllık bir yol var.", "8GKyQ1S5594"),
                ("Forrest Gump", "Robert Zemeckis", "Drama", 1994, 142, "ABD", "forrest.jpg", "Forrest Gump , zeka seviyesi düşük ama kalbi saf ve iyilik dolu olan Forrest Gump'un hayatını anlatır. Alabama'da büyüyen Forrest, hayatı boyunca birçok maceraya atılır: kolej futbolcusu olur, Vietnam Savaşı'nda savaşır, meşhur bir Amerikan futbolcusu ve Ping Pong şampiyonu olur, girişimci bir iş adamı olur ve sonunda bir çocuk babası olur. Forrest'in hayatı, Amerikan tarihindeki önemli olaylarla da iç içe geçmiştir. Film, sıcak bir hikaye anlatımı, duygusal derinlik ve mizahi dokunuşlarla doludur.", "bLvqoHBptjg"),
                ("Yüzüklerin Efendisi", "Peter Jackson", "Fantastik", 2001, 178, "ABD", "yuzuk.jpg", "İyiyle kötü arasındaki mücadelenin epik bir anlatımı olan bu filmde, dünyanın kaderini değişterecek olan bir yüzükten kurtulmak için verilen mücadele anlatılıyor. Yıllar önce üretilen ve Orta Dünya topraklarına kandan başka hiçbir şey getirmeyen yüzüklerin sonuncusu, üretiminden yüz yıllar sonra ortaya çıkar. Amcasının kendisine emanet ettiği yüzüğün nelere kadir olduğundan habersiz olan Frodo, büyücü Gandalf'ın anlattıkları sonrasında dehşete kapılır. Bu yüzükten ve savaşlardan kurtulmaktır.", "ZQv4ah0N6mI"),
                ("Yıldız Savaşları", "George Lucas", "Bilim Kurgu", 1977, 121, "ABD", "yildiz.jpg", "Star Wars: Bölüm 1 - Gizli Tehlike'nin destansı aksiyonu ve unutulmaz maceralarını ilk defa dijital ortamda izleyin. Anakin Skywalker'ın yolculuğundaki ilk önemli adımlarına eşlik edin. Kraliçe Amidala'yı Naboo gezegeninin işgalinden kurtardıktan sonra çöl gezegen Tatooine'e inen, Jedi Ustası Qui-Gon Jinn ve öğrencisi Jedi Obi-Wan Kenobi, Güç yönünden olağanüstü yeteneğe sahip sahip 9 yaşındaki genç köle Anakin Skywalker'ı keşfeder. Anakin heyecanlı bir mücadelenin ardından Pod Yarışı'nı kazanır ve ödül olarak özgürlüğünü alır.", "AEx1fdRZD70"),
            ]

            icerikler_tuple = [
                (1, 1, "Neo ve Trinity Matrix'e giriyorlar."),
                (1, 2, "Agent Smith Neo'yu kovalıyor."),
                (1, 3, "Morpheus, Neo'yu eğitiyor."),
                (2, 1, "Michael Corleone, babasının işlerini devralmaya karar verir."),
                (2, 2, "Michael, ailesini korumak için acımasız kararlar alır."),
                (2, 3, "Ailesinin düşmanlarına karşı intikam almak için harekete geçer."),
                (3, 1, "Andy Dufresne hapishanede Red ile dost olur."),
                (3, 2, "Andy, hapishanede çeşitli işlerde para kazanmaya başlar."),
                (3, 3, "Andy, hapishaneden kaçmayı planlar ve yıllar süren bir kaçış planı kurar."),
                (4, 1, "Batman, Gotham Şehri'ni Joker'in kaosundan korumaya çalışıyor."),
                (4, 2, "Joker, Gotham Şehri'ni terörize etmek için çılgın planlar yapar."),
                (4, 3, "Batman ve Joker arasında epik bir final çatışması yaşanır."),
                (5, 1, "Dom Cobb, rüyalar arasında gezinerek bilgi çalıyor."),
                (5, 2, "Dom, tehlikeli bir soygun görevine liderlik eder ve ekip üyelerinin kişisel hayatları tehlikeye girer."),
                (5, 3, "Dom'un geçmişiyle ilgili sırlar açığa çıkar ve gerçeklikle rüya arasındaki çizgi belirsizleşir."),
                (6, 1, "Tyler Durden, Fight Club'ı kuruyor ve anarşik bir grup oluşturuyor."),
                (6, 2, "Fight Club, erkeklik, tüketim toplumu ve modern yaşamın anlamsızlığı hakkında derin bir yorum sunar."),
                (6, 3, "Narrator, gerçekliği sorgulamaya ve Tyler'ın varlığı hakkında karanlık sırları keşfetmeye başlar."),
                (7, 1, "Vincent Vega ve Jules Winnfield, bir uyuşturucu işini devralırken maceralar yaşıyor."),
                (7, 2, "Vincent ve Jules, bir dizi komik ve tehlikeli olayla karşılaşır."),
                (7, 3, "Uyuşturucu işi kötüye gider ve Vincent ve Jules hayatta kalmaya çalışır."),
                (8, 1, "Cooper ve ekibi, uzayda yeni bir gezegen aramak için görevlendirilir."),
                (8, 2, "Uzay gemisi, bilinmeyen bir gezegene iner ve garip fenomenlerle karşılaşır."),
                (8, 3, "Ekibin hayatta kalma mücadelesi ve bilinmeyen bir dünyayı keşfetme çabaları."),
                (9, 1, "Forrest Gump, hayatında birçok önemli figürle karşılaşır ve tarihî olaylarda rol alır."),
                (9, 2, "Forrest, Amerikan tarihinde önemli bir rol oynar ve bir dizi komik ve dokunaklı macera yaşar."),
                (9, 3, "Forrest'ın hikayesi, Amerikan rüyasını, dostluğu ve aşkı anlatıyor."),
                (10, 1, "Frodo ve Sam, Yüzük'ü yok etmek için Mordor'a yolculuk ediyor."),
                (10, 2, "Yolda, birçok tehlike ve engelle karşılaşırlar."),
                (10, 3, "Frodo ve Sam, Yüzük'ü yok etmek için son bir mücadeleye girerler ve Orta Dünya'yı kurtarırlar."),
            ]

            self.cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES ('eyüp', '123', 'eyüp', 'yılmaz', '5323184256')")
            self.cursor.executemany("INSERT INTO filmler (ad, yonetmen, tur, yapim_yili, sure, yapim_yeri, fotograf, aciklama, fragman) VALUES (?,?,?,?,?,?,?,?, ?)", filmler_tuple)
            self.cursor.executemany("INSERT INTO filmicerik (filmid, sahne, icerik) VALUES (?,?,?)", icerikler_tuple)
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
veritabani = Veritabani('film_veritabani.db')
