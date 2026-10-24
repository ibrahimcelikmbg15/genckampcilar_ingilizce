import streamlit as st

# 1. Sorular Listesi (Veri Tabanı)
sorular = [
    {"soru": "I ________ a student at a middle school.", "secenekler": ["am", "is", "are", "be"], "cevap": "am", "aciklama": "'I' öznesi her zaman 'am' alır."},
    {"soru": "She ________ my best friend.", "secenekler": ["am", "is", "are", "be"], "cevap": "is", "aciklama": "'She' tekil bir özne olduğu için 'is' kullanılır."},
    {"soru": "They ________ from Turkey.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "'They' çoğul bir özne olduğu için 'are' gelir."},
    {"soru": "We ________ very happy today.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "'We' (Biz) çoğuldur, 'are' kullanılır."},
    {"soru": "He ________ ten years old.", "secenekler": ["am", "is", "are", "be"], "cevap": "is", "aciklama": "Yaş söylerken 'to be' (am/is/are) kullanılır. 'He' tekil olduğu için 'is' alır."},
    {"soru": "You ________ a great football player.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "'You' (Sen/Siz) her zaman 'are' alır."},
    {"soru": "It ________ a sunny day.", "secenekler": ["am", "is", "are", "be"], "cevap": "is", "aciklama": "Hava durumundan bahsederken 'It' öznesi 'is' alır."},
    {"soru": "I ________ not a doctor.", "secenekler": ["am", "is", "are", "be"], "cevap": "am", "aciklama": "'I' öznesi olumsuz cümlede de 'am' alır (am not)."},
    {"soru": "________ they your brothers?", "secenekler": ["Am", "Is", "Are", "Do"], "cevap": "Are", "aciklama": "Soru cümlesinde 'they' öznesinin başına 'Are' gelir."},
    {"soru": "________ she your new English teacher?", "secenekler": ["Am", "Is", "Are", "Does"], "cevap": "Is", "aciklama": "'She' öznesi soru cümlesinde başa 'Is' alır."},
    {"soru": "My parents ________ at home.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "'My parents' (Annem ve babam) çoğuldur yani 'They'. Bu yüzden 'are' alır."},
    {"soru": "My best friend and I ________ in the same class.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "'My friend and I' (Arkadaşım ve ben) 'Biz' (We) demektir. 'I' var diye am seçme, çoğul olduğu için 'are' gelir!"},
    {"soru": "Ali and Ahmet ________ brothers.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "İki kişi oldukları için 'Onlar' (They) olurlar, 'are' kullanılır."},
    {"soru": "The cat ________ sleeping on the sofa.", "secenekler": ["am", "is", "are", "be"], "cevap": "is", "aciklama": "'The cat' tekil bir hayvandır (It). Bu yüzden 'is' alır."},
    {"soru": "The cats ________ sleeping on the sofa.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "'The cats' kelimesinin sonundaki -s takısı onu çoğul (Onlar/They) yapar, 'are' kullanılır."},
    {"soru": "My brother's name ________ Can.", "secenekler": ["am", "is", "are", "be"], "cevap": "is", "aciklama": "Burada özne Can'ın kendisi değil, 'adı' (isim). İsim tekil olduğu için 'is' alır."},
    {"soru": "My mother and father ________ teachers.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "Anne ve baba iki kişi oldukları için çoğuldur, 'are' kullanılır."},
    {"soru": "Our school ________ very big.", "secenekler": ["am", "is", "are", "be"], "cevap": "is", "aciklama": "'Our school' (Okulumuz) tekil bir kurumdur (It), bu yüzden 'is' alır."},
    {"soru": "His dogs ________ running in the park.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "Köpekler (dogs) çoğul olduğu için 'are' alır."},
    {"soru": "My uncle and I ________ playing chess.", "secenekler": ["am", "is", "are", "be"], "cevap": "are", "aciklama": "'Amcam ve ben' (Biz) demek olduğu için 'are' alır."},
    {"soru": "I ________ milk every morning.", "secenekler": ["drink", "drinks", "drinking", "is drink"], "cevap": "drink", "aciklama": "Geniş zamanda 'I, You, We, They' özneleri fiile hiçbir ek (s takısı) almaz."},
    {"soru": "He ________ football every weekend.", "secenekler": ["play", "plays", "playing", "is play"], "cevap": "plays", "aciklama": "Geniş zamanda 'He, She, It' özneleri fiile -s takısı alır."},
    {"soru": "They ________ to the cinema on Sundays.", "secenekler": ["go", "goes", "going", "are go"], "cevap": "go", "aciklama": "'They' çoğul olduğu için fiil ek (es) almaz."},
    {"soru": "She ________ a book every night.", "secenekler": ["read", "reads", "reading", "is read"], "cevap": "reads", "aciklama": "'She' tekil olduğu için fiile -s takısı gelir (reads)."},
    {"soru": "We ________ our homework after school.", "secenekler": ["do", "does", "doing", "are do"], "cevap": "do", "aciklama": "'We' (Biz) çoğuldur, fiil yalın halde kalır (do)."},
    {"soru": "It ________ a lot in winter.", "secenekler": ["snow", "snows", "snowing", "is snow"], "cevap": "snows", "aciklama": "'It' tekil öznesi fiile -s takısı aldırır (snows)."},
    {"soru": "You ________ very fast.", "secenekler": ["run", "runs", "running", "are run"], "cevap": "run", "aciklama": "'You' öznesi fiile ek almaz."},
    {"soru": "I ________ my teeth every day.", "secenekler": ["brush", "brushes", "brushing", "am brush"], "cevap": "brush", "aciklama": "'I' öznesi olduğu için fiil ek almaz."},
    {"soru": "He ________ TV in the evenings.", "secenekler": ["watch", "watches", "watching", "is watch"], "cevap": "watches", "aciklama": "Sonu 'ch' ile biten fiiller He/She/It ile '-es' takısı alır (watches)."},
    {"soru": "They ________ English at school.", "secenekler": ["learn", "learns", "learning", "are learn"], "cevap": "learn", "aciklama": "'They' çoğul olduğu için fiil yalın kalır (learn)."},
    {"soru": "My parents ________ up early.", "secenekler": ["wake", "wakes", "waking", "are wake"], "cevap": "wake", "aciklama": "'My parents' (Onlar) çoğuldur, çoğullar fiile -s takısı almaz."},
    {"soru": "My brother ________ milk.", "secenekler": ["like", "likes", "liking", "is like"], "cevap": "likes", "aciklama": "'My brother' tekil bir erkek (He), bu yüzden fiile -s takısı gelir."},
    {"soru": "Ahmet and I ________ to school together.", "secenekler": ["walk", "walks", "walking", "are walk"], "cevap": "walk", "aciklama": "'Ahmet and I' (Ahmet ve ben = Biz/We). Çoğul olduğu için fiil yalın kalır."},
    {"soru": "My dog ________ meat.", "secenekler": ["eat", "eats", "eating", "is eat"], "cevap": "eats", "aciklama": "'My dog' tekil bir hayvandır (It). Fiile -s takısı gelir."},
    {"soru": "The students ________ to the teacher.", "secenekler": ["listen", "listens", "listening", "are listen"], "cevap": "listen", "aciklama": "'Students' kelimesindeki -s onu çoğul (Onlar) yapar. Fiil yalın kalır."},
    {"soru": "My sister ________ hard for exams.", "secenekler": ["study", "studies", "studying", "is study"], "cevap": "studies", "aciklama": "'My sister' tekildir (She). 'y' harfi ile biten fiillerde y düşer ve -ies gelir (studies)."},
    {"soru": "My mother ________ delicious cakes.", "secenekler": ["make", "makes", "making", "is make"], "cevap": "makes", "aciklama": "'My mother' tekildir (She), fiile -s takısı gelir."},
    {"soru": "Can and Ali ________ basketball.", "secenekler": ["play", "plays", "playing", "are play"], "cevap": "play", "aciklama": "İki kişi oldukları için (They) çoğuldurlar, fiil ek almaz."},
    {"soru": "My father and I ________ football matches.", "secenekler": ["watch", "watches", "watching", "are watch"], "cevap": "watch", "aciklama": "'Babam ve ben' (Biz/We) demektir. Fiil ek almaz."},
    {"soru": "The baby ________ when he is hungry.", "secenekler": ["cry", "cries", "crying", "is cry"], "cevap": "cries", "aciklama": "'The baby' tekildir (He/She). 'y' harfi düşer ve '-ies' eklenir (cries)."},
    {"soru": "I ________ like broccoli.", "secenekler": ["don't", "doesn't", "isn't", "aren't"], "cevap": "don't", "aciklama": "'I' öznesi geniş zamanda olumsuz yapılırken 'don't' kullanılır."},
    {"soru": "She ________ play the guitar.", "secenekler": ["don't", "doesn't", "isn't", "aren't"], "cevap": "doesn't", "aciklama": "'He, She, It' özneleri geniş zamanda olumsuz yapılırken 'doesn't' kullanılır. Fiildeki -s takısı düşer."},
    {"soru": "My parents ________ watch TV in the morning.", "secenekler": ["don't", "doesn't", "isn't", "aren't"], "cevap": "don't", "aciklama": "'My parents' çoğuldur (They), bu yüzden 'don't' kullanılır."},
    {"soru": "My friend and I ________ go to bed late.", "secenekler": ["don't", "doesn't", "isn't", "aren't"], "cevap": "don't", "aciklama": "'Biz' (We) olduğumuz için 'don't' gelir."},
    {"soru": "The cat ________ like water.", "secenekler": ["don't", "doesn't", "isn't", "aren't"], "cevap": "doesn't", "aciklama": "Kedi tekildir (It), olumsuzda 'doesn't' kullanılır."},
    {"soru": "________ you like playing tennis?", "secenekler": ["Do", "Does", "Are", "Is"], "cevap": "Do", "aciklama": "Geniş zaman soru cümlesinde 'You' öznesi için başa 'Do' gelir."},
    {"soru": "________ your mother work in a hospital?", "secenekler": ["Do", "Does", "Is", "Are"], "cevap": "Does", "aciklama": "'Your mother' (Annen) tekil kişidir (She). Soru kelimesi 'Does' olmalıdır."},
    {"soru": "________ they speak English?", "secenekler": ["Do", "Does", "Are", "Is"], "cevap": "Do", "aciklama": "'They' çoğul öznesinin başına 'Do' gelir."},
    {"soru": "________ Ahmet and Ayşe live in İstanbul?", "secenekler": ["Do", "Does", "Are", "Is"], "cevap": "Do", "aciklama": "İki kişi oldukları için (Onlar), soruya 'Do' ile başlanır. 'Does' sadece tekil kişiler için kullanılır."},
    {"soru": "I am a student, but I ________ study every day.", "secenekler": ["don't", "doesn't", "am not", "aren't"], "cevap": "don't", "aciklama": "'study' bir fiildir, fiil olan cümleyi olumsuz yapmak için 'don't' kullanılır. 'I am not study' denmez."}
]

# 2. Arayüz ve Uygulama Mantığı
st.title("İngilizce Dilbilgisi Testi 🚀")

# Test durumunu hafızada tutmak için Session State ayarları
if 'soru_index' not in st.session_state:
    st.session_state.soru_index = 0
if 'skor' not in st.session_state:
    st.session_state.skor = 0
if 'cevaplandi_mi' not in st.session_state:
    st.session_state.cevaplandi_mi = False
if 'secilen_cevap' not in st.session_state:
    st.session_state.secilen_cevap = None

# Test bitiş kontrolü
if st.session_state.soru_index >= len(sorular):
    st.success(f"🎉 Test Bitti! Toplam Skorunuz: {st.session_state.skor} / {len(sorular)}")
    if st.button("Yeniden Başla"):
        st.session_state.soru_index = 0
        st.session_state.skor = 0
        st.session_state.cevaplandi_mi = False
        st.session_state.secilen_cevap = None
        st.rerun()
else:
    # Mevcut soruyu çekme
    mevcut_soru = sorular[st.session_state.soru_index]
    
    st.subheader(f"Soru {st.session_state.soru_index + 1} / {len(sorular)}")
    st.write(f"**{mevcut_soru['soru']}**")
    
    # Cevaplama aşaması
    if not st.session_state.cevaplandi_mi:
        secim = st.radio("Cevabınızı seçin:", mevcut_soru["secenekler"], index=None, key=f"radio_{st.session_state.soru_index}")
        
        if st.button("Cevapla") and secim is not None:
            st.session_state.secilen_cevap = secim
            st.session_state.cevaplandi_mi = True
            
            if secim == mevcut_soru["cevap"]:
                st.session_state.skor += 1
                
            st.rerun()
            
    # Sonuç gösterme aşaması
    else:
        secim = st.session_state.secilen_cevap
        # Radio butonunu devre dışı bırakarak tekrar gösteriyoruz (görsellik için)
        st.radio("Cevabınızı seçin:", mevcut_soru["secenekler"], index=mevcut_soru["secenekler"].index(secim), disabled=True)
        
        if secim == mevcut_soru["cevap"]:
            st.success("✅ Doğru!")
        else:
            st.error(f"❌ Yanlış! Doğru Cevap: **{mevcut_soru['cevap']}**")
        
        # Açıklamayı gösterme
        st.info(f"💡 **Açıklama:** {mevcut_soru['aciklama']}")
        
        # Sonraki soruya geçiş
        if st.button("Sonraki Soruya Geç"):
            st.session_state.soru_index += 1
            st.session_state.cevaplandi_mi = False
            st.session_state.secilen_cevap = None
            st.rerun()
