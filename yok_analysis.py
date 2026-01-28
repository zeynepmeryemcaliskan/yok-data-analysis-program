"""
YOK (Yükseköğretim Kurulu) Veri Analiz Programı
Colab üzerinde geliştirilip GitHub'a gönderiliyor.
"""

import pandas as pd
import numpy as np
from datetime import datetime

def yok_analysis_example():
    """YOK veri analizi örnek fonksiyonu"""
    print("YOK VERİ ANALİZ PROGRAMI")
    print("=" * 40)
    
    # Örnek veri oluştur (YOK istatistikleri gibi)
    data = {
        'Üniversite': ['İTÜ', 'ODTÜ', 'BOUN', 'Hacettepe', 'Ankara'],
        'Öğrenci_Sayısı': [25000, 23000, 18000, 42000, 35000],
        'Akademik_Personel': [1500, 1400, 1000, 2500, 2000],
        'Yayın_Sayısı': [5000, 4500, 3000, 7000, 6000]
    }
    
    df = pd.DataFrame(data)
    
    print("\n📊 Üniversite Verileri:")
    print(df.to_string(index=False))
    
    print("\n📈 Temel İstatistikler:")
    print(f"Toplam Öğrenci: {df['Öğrenci_Sayısı'].sum():,}")
    print(f"Ortalama Akademik Personel: {df['Akademik_Personel'].mean():.0f}")
    print(f"En Fazla Yayın: {df['Yayın_Sayısı'].max()} ({df.loc[df['Yayın_Sayısı'].idxmax(), 'Üniversite']})")
    
    # Öğrenci başına akademik personel oranı
    df['Oran'] = df['Akademik_Personel'] / df['Öğrenci_Sayısı'] * 100
    print("\n🎓 Öğrenci Başına Akademik Personel Oranı (%):")
    print(df[['Üniversite', 'Oran']].to_string(index=False))
    
    return df

def main():
    """Ana fonksiyon"""
    print(f"Program başlangıç zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    try:
        df = yok_analysis_example()
        print("\n✅ Analiz başarıyla tamamlandı!")
        print(f"\n📅 Program bitiş zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return df
    except Exception as e:
        print(f"\n❌ Hata oluştu: {e}")
        return None

if __name__ == "__main__":
    result = main()
