# Yılan Oyunu

## Kod Açıklaması

Bu Python programı, klasik bir yılan oyunu oluşturmak için Pygame kütüphanesini kullanır. Oyunun amacı, yılanı kontrol ederek ekrandaki yemleri yemesini sağlamak ve puan kazanmaktır. Yılan yem yedikçe büyür ve oyun hızı sabit kalır.

### Ana Bileşenler

- **YEM Sınıfı:** Yemin pozisyonunu ve rengini belirler. Rastgele bir pozisyon oluşturur ve yemi ekranda çizer.
- **YILAN Sınıfı:** Yılanın pozisyonunu, yönünü ve rengini belirler. Yılanın hareket etmesini, yön değiştirmesini ve ekranda çizilmesini sağlar. Ayrıca yılanın kendine çarpıp çarpmadığını kontrol eder.
- **kafesi_ciz:** Oyun ekranındaki kafesi (ızgarayı) çizer.
- **main:** Oyunun ana fonksiyonu. Pygame'i başlatır, ekranı oluşturur, yılanı ve yemi oluşturur. Kullanıcı girişlerini işler, yılanı hareket ettirir, yemi kontrol eder ve puanı günceller.

## Örnek Kullanım

Bu oyunu çalıştırmak için, Python ve Pygame kütüphanesinin yüklü olduğundan emin olun. Ardından, aşağıdaki kodu çalıştırarak oyunu başlatabilirsiniz:

```bash
python yilan_oyunu.py
```
## Notlar

- Yılanın kendine çarpması durumunda oyun sıfırlanır.
- Yem yedikçe yılan büyür ve puan artar.
- Oyun hızı `saat.tick(6)` satırı ile ayarlanmıştır. Bu değeri artırarak oyunu hızlandırabilir, azaltarak yavaşlatabilirsiniz.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

