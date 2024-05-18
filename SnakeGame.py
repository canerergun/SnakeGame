import pygame, sys, random

# Ekran boyutları
ekran_genisligi = 600
ekran_yuksekligi = 600

# Kafes boyutu
kafes_boyutu = 20
kafes_genisligi = ekran_genisligi // kafes_boyutu
kafes_yuksekligi = ekran_yuksekligi // kafes_boyutu

# Renkler
acik_yesil = (0, 170, 140)
koyu_yesil = (0, 140, 120)
yem_rengi = (250, 200, 0)
yilan_rengi = (34, 34, 34)

# Yönler
yukari = (0, -1)
asagi = (0, 1)
sag = (1, 0)
sol = (-1, 0)

# Yem sınıfı
class YEM:
    def __init__(self):
        # Yemin başlangıç pozisyonunu ve rengini belirle
        self.pozisyon = (0, 0)
        self.renk = yem_rengi
        self.rastgele_pozisyon()  # Rastgele bir pozisyon belirle

    def rastgele_pozisyon(self):
        # Yemin pozisyonunu rastgele belirle
        self.pozisyon = (random.randint(0, kafes_genisligi - 1) * kafes_boyutu, 
                         random.randint(0, kafes_yuksekligi - 1) * kafes_boyutu)

    def ciz(self, yuzey):
        # Yem dikdörtgenini çiz
        dikdortgen = pygame.Rect(self.pozisyon, (kafes_boyutu, kafes_boyutu))
        pygame.draw.rect(yuzey, self.renk, dikdortgen)

# Yılan sınıfı
class YILAN:
    def __init__(self):
        # Yılanın başlangıç pozisyonunu, yönünü ve rengini belirle
        self.pozisyonlar = [(ekran_genisligi // 2, ekran_yuksekligi // 2)]
        self.yon = random.choice([yukari, asagi, sol, sag])
        self.renk = yilan_rengi
        self.buyume = False  # Yılanın büyüme durumu

    def bas_pozisyonu(self):
        # Yılanın baş pozisyonunu döndür
        return self.pozisyonlar[0]

    def yon_degistir(self, nokta):
        # Yılanın yönünü değiştir (ters yön olmaması şartıyla)
        if (nokta[0] * -1, nokta[1] * -1) == self.yon:
            return
        else:
            self.yon = nokta

    def hareket_et(self):
        # Yılanın hareketini gerçekleştir
        suanki = self.bas_pozisyonu()
        x, y = self.yon
        yeni = ((suanki[0] + (x * kafes_boyutu)) % ekran_genisligi, 
                (suanki[1] + (y * kafes_boyutu)) % ekran_yuksekligi)

        # Yılanın kendine çarpıp çarpmadığını kontrol et
        if len(self.pozisyonlar) > 2 and yeni in self.pozisyonlar[2:]:
            self.sifirla()  # Çarptıysa yılanı sıfırla
        else:
            self.pozisyonlar.insert(0, yeni)  # Yeni baş pozisyonunu ekle
            if not self.buyume:
                self.pozisyonlar.pop()  # Büyüme yoksa son elemanı çıkar
            else:
                self.buyume = False  # Büyüme varsa büyümeyi iptal et

    def sifirla(self):
        # Yılanı başlangıç durumuna getir
        self.pozisyonlar = [(ekran_genisligi // 2, ekran_yuksekligi // 2)]
        self.yon = random.choice([yukari, asagi, sol, sag])
        self.buyume = False

    def ciz(self, yuzey):
        # Yılanı çiz
        for p in self.pozisyonlar:
            dikdortgen = pygame.Rect(p, (kafes_boyutu, kafes_boyutu))
            pygame.draw.rect(yuzey, self.renk, dikdortgen)

    def tuslari_isle(self):
        # Kullanıcıdan gelen tuşları işle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.yon_degistir(yukari)
                elif event.key == pygame.K_DOWN:
                    self.yon_degistir(asagi)
                elif event.key == pygame.K_LEFT:
                    self.yon_degistir(sol)
                elif event.key == pygame.K_RIGHT:
                    self.yon_degistir(sag)

# Kafes çizme fonksiyonu
def kafesi_ciz(yuzey):
    # Ekrandaki kafesi çiz
    for y in range(0, int(kafes_yuksekligi)):
        for x in range(0, int(kafes_genisligi)):
            if (x + y) % 2 == 0:
                acik = pygame.Rect((x * kafes_boyutu, y * kafes_boyutu), (kafes_boyutu, kafes_boyutu))
                pygame.draw.rect(yuzey, acik_yesil, acik)
            else:
                koyu = pygame.Rect((x * kafes_boyutu, y * kafes_boyutu), (kafes_boyutu, kafes_boyutu))
                pygame.draw.rect(yuzey, koyu_yesil, koyu)

# Ana fonksiyon
def main():
    pygame.init()  # Pygame'i başlat
    ekran = pygame.display.set_mode((ekran_genisligi, ekran_yuksekligi))  # Ekranı oluştur
    saat = pygame.time.Clock()  # Saat objesi oluştur
    yuzey = pygame.Surface(ekran.get_size())
    yuzey = yuzey.convert()  # Yüzeyi oluştur ve dönüştür
    yilan = YILAN()  # Yılanı oluştur
    yem = YEM()  # Yemi oluştur
    puan = 0  # Başlangıç puanı
    font = pygame.font.SysFont('arial', 25)  # Puan yazı tipi

    while True:
        yilan.tuslari_isle()  # Kullanıcı girişlerini işle
        yilan.hareket_et()  # Yılanı hareket ettir
        if yilan.bas_pozisyonu() == yem.pozisyon:
            yilan.buyume = True  # Yılan yemi yediğinde büyü
            yem.rastgele_pozisyon()  # Yeni yem pozisyonu oluştur
            puan += 1  # Puanı artır

        kafesi_ciz(yuzey)  # Kafesi çiz
        yilan.ciz(yuzey)  # Yılanı çiz
        yem.ciz(yuzey)  # Yemi çiz

        # Puanı ekrana yaz
        puan_yazi = font.render(f'Puan: {puan}', True, (255, 255, 255))
        ekran.blit(yuzey, (0, 0))  # Yüzeyi ekrana çiz
        ekran.blit(puan_yazi, (10, 10))  # Puanı ekrana çiz

        pygame.display.update()  # Ekranı güncelle
        saat.tick(6)  # Oyunun hızını ayarla (6 FPS)

main()  # Ana fonksiyonu çalıştır
