# 🛠️ Geliştirme Rehberi

Bu rehber, hem insan hem de yapay zeka geliştiriciler için hazırlanmıştır.

---

### 🚀 Projenize Başlarken (Önerilen İlk Adımlar)

Bu şablonu kullanarak yeni bir proje oluşturduktan sonra, geliştirme sürecine başlamadan önce aşağıdaki adımları tamamlamanız şiddetle tavsiye edilir. Bu adımlar, projenizin "neden" var olduğunu ve ilk "ne"leri yapacağını netleştirir.

1.  **Vizyonu Tanımlayın:** `docs/` klasörü içinde, projenizin amacını, çözdüğü problemi ve hedef kitlesini anlatan bir `PROJECT_VISION.md` dosyası oluşturun.
2.  **Kapsamı Belirleyin:** Yine `docs/` klasöründe, projenizin ilk kullanılabilir sürümünde (v1.0) hangi özelliklerin olacağını ve nelerin olmayacağını listeleyen bir `FEATURES.md` dosyası oluşturun.
3.  **Etiketleri Kurun (Önemli):** GitHub, şablondaki özel etiketleri (labels) otomatik olarak kopyalamaz. Lütfen projenizin "Issues" -> "Labels" bölümüne gidin ve `aicra-repo-template` deposunda tanımlanan standart etiket setini manuel olarak oluşturun. Bu, görev takibinin doğru çalışması için kritik öneme sahiptir.

---

### 🔄 Süreç

1.  **Bağlamı Anla:** Kod yazmaya başlamadan önce `docs/ai-context.yaml`, `docs/architecture.md` ve özellikle yeni oluşturduğunuz vizyon/kapsam belgelerini dikkatlice oku.
2.  **"Issue" Aç:** Her yeni görev (özellik, hata vb.) için bir "Issue" aç. Bu, işin takip edilebilir olmasını sağlar.
3.  **Niyetini Beyan Et:** Açtığın "Issue" ile ilişkili olarak, projenin kök dizinindeki `CONTRIBUTION_PLAN.md` dosyasını kopyalayarak yeni bir görev için planını oluştur. Bu planı `plan/` klasörü altına kaydet ve commitle.
4.  **Onay Al:** Planının linkini ilgili "Issue"ya yorum olarak ekle ve durumu `status: 2-awaiting-approval` olarak değiştir. Bir Orkestratör planı gözden geçirecektir.
5.  **Uygula:** Planın onaylandıktan (`status: 3-ready-for-dev`) sonra, yeni bir branch açarak kodu üret veya düzenle.
6.  **Test Et:** `/tests` klasörüne gerekli testleri ekle veya mevcutları güncelle.
7.  **Gönder (Pull Request):** Değişikliklerini bir Pull Request ile gönder. Açıklama kısmında ilgili `CONTRIBUTION_PLAN.md` dosyasına ve "Closes #IssueNumarası" formatında ilgili "Issue"ya referans ver. Bir Orkestratör, kodu gözden geçirip birleştirecektir.
