# Yapay Zeka Etik ve Güvenlik Politikası

Yapay zeka ajanlarının kullanımı, projeye büyük faydalar sağlarken aynı zamanda sorumluluklar da getirir.

1.  **İnsan Sorumluluğu:** Ana branch'e birleştirilen her kod satırından, kodu kimin (insan veya AI) yazdığına bakılmaksızın, nihai olarak bir **insan orkestratör** sorumludur.
2.  **Şeffaflık:** Yapay zeka tarafından üretilen veya büyük ölçüde değiştirilen commit'ler, bu durumu açıkça belirtmelidir (örneğin, commit mesajında "Co-authored-by: CodeAgent" gibi bir not ile).
3.  **Veri Gizliliği:** Yapay zeka ajanları, depodaki hassas verilere (şifreler, API anahtarları, kişisel bilgiler) erişmemeli veya bu verilerle eğitilmemelidir.
4.  **Önyargı Denetimi:** Yapay zeka tarafından üretilen kod, algoritmik önyargılar açısından gözden geçirilmelidir. Proje, adil ve ayrımcı olmayan çıktılar üretmeyi hedeflemelidir.
