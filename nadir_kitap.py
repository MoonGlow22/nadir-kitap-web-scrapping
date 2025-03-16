from selenium import webdriver # 2.37.1 sürüm gereklidir
import pandas as pd


def scrape_nadir_kitap(book_names):
    base_url = "https://www.nadirkitap.com"
    df = pd.DataFrame()

    for book_name in book_names:
        for each in range(1,3):
            print(book_name, each)
            try:
                driver = webdriver.Chrome("D:\yazılım\python\kisisel projeler\chromedriver-win64\chromedriver.exe")
                
                search_url = f"{base_url}/kitapara_sonuc.php?kelime={book_name.replace(' ', '%20')}&siralama=fiyatartan&bks=30&page={each}"
                driver.get(search_url)
        

                for each in range(1,26): # her sayfada 25 kitap var
                    try:
                        seller = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/ul/li[{}]/div[2]/div/div[1]/ul/li[1]/span/a'.format(each))
                        price = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/ul/li[{}]/div[2]/div/div[2]/div[3]'.format(each))
                        
                        amount_str = price[0].text.replace(" TL", "")
                        amount_str = amount_str.replace(",", ".")
                        amount_float = float(amount_str)
                        df.loc[book_name,seller.text] =  amount_float
                    except:
                        break
                driver.quit()
            except:
                driver.quit()
                break
        
        
        columns_to_drop = []
        for column in df.columns:
            column_sum = df[column].notna().sum()
            if column_sum < min_book_found:
                columns_to_drop.append(column)
        df = df.drop(columns=columns_to_drop)
        
    return df

#%%


# Kitap isimlerini içeren bir liste oluşturun
# Yazar isimlerini eklemek doğru kitapların bulunmasına yardımcı olabilir 
# Ş Ç Ğ kullanmayın
book_names = ['Kırmızı kitap carl jung',
              'İnsan Ruhuna Yönelis carl jung',
              'Anılar, Düsler, Düsünceler carl jung',
              'olaganüstü bir gece zweig',
              'ölüm manifestosu tolstoy',
              'Sen bilim nietzsche',
              'sınırlar henry',
              'hayati yalanlar, basit gercekler goleman',
              'yeni liderler goleman']


# Satıcının excel dosyasına eklenebilmesi için gerekli minimum kitap sayısı
min_book_found=2


# Nadir Kitap sitesinden verileri çek
df = scrape_nadir_kitap(book_names)


# Doluluk oranlarına göre sütunları sırala
fill_rates = df.count() / len(df)
sorted_columns = fill_rates.sort_values(ascending=False)
new_order = sorted_columns.index
df = df.reindex(columns=new_order)


# Sonuçları Excel dosyasına kaydet
df.to_excel('nadir_kitap.xlsx', index=True)