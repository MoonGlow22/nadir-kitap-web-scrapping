# nadir-kitap-web-scrapping
Bu Python betiği, Selenium kullanarak **Nadir Kitap** web sitesinden belirli kitapların fiyatlarını ve satıcı bilgilerini çekmek için tasarlanmıştır. İşleyişi şu şekildedir:  

### **Özellikler:**  
- Kullanıcı tarafından sağlanan **kitap isimleri listesi** için web kazıma işlemi yapar.  
- **Fiyatları düşükten yükseğe sıralayarak** en ucuz seçenekleri listeler.  
- **İlk iki sayfadaki (toplam 50 kitap) verileri** toplar.  
- **Selenium WebDriver** kullanarak web sayfalarına erişir ve **XPATH ile verileri çeker**.  
- Her kitap için bulunan **satıcı ve fiyat bilgilerini bir DataFrame’e** kaydeder.  
- **Eksik veriye sahip satıcıları filtreleyerek** yalnızca yeterli sayıda kitabı listeleyenleri tutar.  
- Son olarak **verileri Excel dosyasına kaydeder** (`nadir_kitap.xlsx`).  

### **Kullanım:**  
1. **Eski bir Selenium sürümü** gereklidir. Yeni sürümlerde `find_element_by_xpath` yerine `find_element(By.XPATH, "...")` kullanılması gerekebilir.  
2. **Chromedriver yolunun doğru ayarlandığından** emin olunmalıdır.  
3. **Nadir Kitap’ın sayfa yapısı değişirse**, XPATH güncellenmelidir.  

Bu betik, **kitap fiyatlarını karşılaştırmak, satıcıları analiz etmek ve veri toplamak** isteyen kullanıcılar için uygundur.
