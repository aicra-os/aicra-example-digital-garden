# 🏛️ Mimari Bakış

## 1. Yüksek Seviye Tasarım

*Bu bölüme projenizin genel mimarisini açıklayan bir metin veya diyagram ekleyin.*

**Örnek:** Bu proje, bir REST API ağ geçidi arkasında çalışan mikroservis mimarisini takip etmektedir. Servisler arası iletişim için RabbitMQ kullanılmaktadır.

## 2. Ana Bileşenler

*   **Kullanıcı Servisi:** Kimlik doğrulama ve kullanıcı yönetimi sorumluluklarını üstlenir.
*   **Ürün Servisi:** Ürün bilgilerini ve envanteri yönetir.
*   **API Gateway:** Gelen istekleri ilgili servislere yönlendirir ve güvenlik kontrollerini sağlar.

## 3. Teknoloji Yığını

*   **Backend:** Python (FastAPI)
*   **Veritabanı:** PostgreSQL
*   **Önbellek:** Redis

## 4. Tasarım Prensipleri

*   **Modülerlik:** Bileşenler arasında gevşek bağlılık (loose coupling) hedeflenir.
*   **Ölçeklenebilirlik:** Yatay ölçeklenmeye uygun tasarım yapılır.
*   **Güvenlik:** OWASP Top 10 prensiplerine uyulur.
