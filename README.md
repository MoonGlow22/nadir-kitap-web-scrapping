# nadir-kitap-web-scrapping
Bu Python betiği, Nadir Kitap web sitesinden belirli kitapların fiyatlarını, satıcı bilgilerini toplar ve kargo ücretinden tasarruf etmek amacıyla aynı satıcıdan birden fazla kitap almayı kolaylaştırır.

### **Özellikler:**  
- Kullanıcı tarafından sağlanan **kitap isimleri listesi** için web kazıma işlemi yapar.   
- **İlk iki sayfadaki (toplam 50 kitap) verileri** toplar.  
- **Selenium WebDriver** kullanarak web sayfalarına erişir ve **XPATH ile verileri çeker**.  
- Her kitap için bulunan **satıcı ve fiyat bilgilerini bir DataFrame’e** kaydeder.  
- **Eksik veriye sahip satıcıları filtreleyerek** yalnızca yeterli sayıda kitabı listeleyenleri tutar.  
- Son olarak **verileri Excel dosyasına kaydeder** (`nadir_kitap.xlsx`).  

### **Kullanım:**  
1. **Selenium 2.37.1 sürümü** gereklidir. Yeni sürümlerde `find_element_by_xpath` yerine `find_element(By.XPATH, "...")` kullanılması gerekebilir.  
2. **Chromedriver yolunun doğru ayarlandığından** emin olunmalıdır.  
3. **Nadir Kitap’ın sayfa yapısı değişirse**, XPATH güncellenmelidir.  

Bu betik, **kitap fiyatlarını karşılaştırmak, satıcıları analiz etmek ve veri toplamak** isteyen kullanıcılar için uygundur.
