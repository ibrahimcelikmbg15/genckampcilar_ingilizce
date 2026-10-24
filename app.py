import streamlit as st
import pandas as pd
import os
from datetime import datetime
from sorular import sorular 

st.set_page_config(page_title="Genç Kapcılar İngilizce Eğitim Platformu", page_icon="🚀")
DOSYA_ADI = "test_sonuclari.csv"

st.sidebar.title("Genç Kapcılar 🚀")
menu = st.sidebar.selectbox("Giriş Yap", ["Testi Çöz", "Öğretmen Paneli"])

if menu == "Testi Çöz":
    st.title("🚀 Genç Kapcılar İngilizce Eğitim Platformu")
    st.markdown("Hoş geldin! Aşağıya adını yaz ve İngilizce görevlerine başla.")
    
    ogrenci_adi = st.text_input("Adını Yaz ve Başla:")
    
    if ogrenci_adi:
        if 'soru_index' not in st.session_state:
            st.session_state.soru_index = 0
            st.session_state.puan = 0
            st.session_state.test_bitti = False

        if not st.session_state.test_bitti:
            mevcut_soru = sorular[st.session_state.soru_index]
            st.subheader(f"Soru {st.session_state.soru_index + 1} / {len(sorular)}")
            st.write(mevcut_soru["soru"])
            
            secim = st.radio("Cevabını seç:", mevcut_soru["secenekler"], key=f"soru_{st.session_state.soru_index}")
            
            if st.button("Cevapla ve İlerle"):
                # Sadece arka planda puanı hesaplıyoruz, çocuğa mesaj göstermiyoruz
                if secim == mevcut_soru["cevap"]:
                    st.session_state.puan += 10
                
                if st.session_state.soru_index < len(sorular) - 1:
                    st.session_state.soru_index += 1
                else:
                    st.session_state.test_bitti = True
                    
                    yeni_veri = pd.DataFrame([{
                        "Tarih": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "İsim": ogrenci_adi,
                        "Puan": st.session_state.puan
                    }])
                    
                    if not os.path.isfile(DOSYA_ADI):
                        yeni_veri.to_csv(DOSYA_ADI, index=False)
                    else:
                        yeni_veri.to_csv(DOSYA_ADI, mode='a', header=False, index=False)
                        
                st.rerun()
                
        else:
            st.balloons()
            st.success("Test Bitti! Görev tamamlandı.")
            st.write("Harikasın! Sonuçların öğretmene gizlice iletildi. Çıkış yapabilirsin. 😎")
            
            if st.button("Yeniden Çöz"):
                st.session_state.soru_index = 0
                st.session_state.puan = 0
                st.session_state.test_bitti = False
                st.rerun()

elif menu == "Öğretmen Paneli":
    st.title("📊 Öğretmen Paneli: Test Sonuçları")
    sifre = st.text_input("Şifre Girin:", type="password")
    
    if sifre == "1234":
        if os.path.isfile(DOSYA_ADI):
            df = pd.read_csv(DOSYA_ADI)
            st.dataframe(df.style.highlight_max(subset=['Puan'], color='lightgreen'))
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Sonuçları Excel (CSV) Olarak İndir",
                data=csv,
                file_name='genc_kapcilar_sonuclar.csv',
                mime='text/csv',
            )
        else:
            st.info("Henüz kimse testi çözmemiş. Genç Kapcılar'ı bekliyoruz!")
