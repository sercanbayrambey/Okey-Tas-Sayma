# Okey Taş Sayma (Okey Tile Counter)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Görüntü işleme teknikleri kullanılarak Okey oyununda atılan tüm taşları gerçek zamanlı olarak takip eden ve görüntüleyen Python uygulaması.

![Demo](https://user-images.githubusercontent.com/45638332/90337473-626f6e80-dfeb-11ea-8425-ee9364843a4c.png)

## 🎯 Özellikler

- **Gerçek Zamanlı Takip**: Okey masasındaki taş değişikliklerini anlık olarak algılar
- **Görsel Arayüz**: Atılan taşları düzenli bir şekilde görüntüler
- **Otomatik Algılama**: Dört farklı pozisyondaki taş değişikliklerini otomatik tespit eder
- **Keyboard Kontrolleri**: F1, F2, F3 tuşları ile uygulama kontrolü

## 🛠️ Teknolojiler

- **Python 3.x**: Ana programlama dili
- **OpenCV (cv2)**: Görüntü işleme ve bilgisayarlı görü
- **NumPy**: Sayısal hesaplamalar ve array işlemleri
- **PIL (Pillow)**: Ekran görüntüsü alma
- **Threading**: Çoklu iş parçacığı desteği
- **Keyboard**: Klavye girişlerini yakalama

## 📋 Gereksinimler

```bash
pip install opencv-python
pip install numpy
pip install pillow
pip install keyboard
```

## 🚀 Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/sercanbayrambey/Okey-Tas-Sayma.git
cd Okey-Tas-Sayma
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştırın:
```bash
python 101.py
```

## 🎮 Kullanım

### Kontroller
- **F1**: Taş takibini başlat
- **F2**: Taş takibini durdur  
- **F3**: Uygulamayı sıfırla
- **Q**: Uygulamadan çık

### Nasıl Çalışır
1. Uygulama başlatıldığında ekranınızı tarar
2. F1 tuşuna basarak taş takibini başlatın
3. Okey oyununu oynarken, atılan taşlar otomatik olarak "Taslar" penceresinde görüntülenir
4. Her yeni taş, önceki taşların yanına sıralı olarak eklenir

## 📐 Teknik Detaylar

- **Ekran Bölgesi**: Belirli koordinatlarda taş pozisyonlarını izler
- **Görüntü Karşılaştırma**: NumPy array karşılaştırması ile değişiklikleri tespit eder
- **Threading**: Klavye dinleme ve görüntü işleme paralel çalışır
- **Real-time Processing**: Sürekli ekran tarama ile anlık güncelleme



