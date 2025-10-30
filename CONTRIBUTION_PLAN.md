# KATKI PLANI ŞABLONU
# YENİ BİR GÖREVE BAŞLAMADAN ÖNCE BU DOSYAYI KOPYALAYIN VE DOLDURUN.
# Örnek dosya adı: `plan/feature-user-auth.md`

intent: "Örnek: Kullanıcı servisine caching katmanı eklemek"
author: "@kullaniciadi veya @agent:CodeAgent"
context_version: "1.0"
constraints:
  - "docs/architecture.md dosyasındaki prensiplere uyulmalı"
  - "İlgili testler güncellenmeli"
  - "Redis client kütüphanesi kullanılmalı"
expected_output:
  - "src/services/cache_manager.py"
  - "tests/test_cache_manager.py"
  - "docs/architecture.md (yeni bağımlılık eklendi)"
