Download video content and subtitle from Nrk Tv-Radio-Super.  
Drag & Drop GUI made in Python(Wxpython).

---
Siste versjon  **14-1-2024** er **wx_nrk_2.7**  

---

- 2.7 Fikser ny media navn på eldere innhold

---

- 2.6 Fikser Nrk Radio,som nå har et to delt system med både .mp3 og stream .mkv nedlasting    
- 2.4 Virker forstatt fint viss bare bruker Nrk Tv

---

- 2.3 Fikser noen programmer som ikke virket på Nrk Radio  

---
- 2.2 legger til Radio og Super støtte   
- 2.2 Bedre titler på programmer  
Se en demo [her](https://www.dropbox.com/sh/wackcyek8nzziaf/wJ1hAkF49U)

---
###  Beskrivelse wx_nrk_2.7:

 - Dra fra url adresse eller video tumbnails(NRK-TV) til GUI vinduet.
 - Velg videokvalitet "high" er default.
 - Laster ned automatisk til video formatet(mkv),parser for undertekster(srt) lages.
 - video(mkv) og undertekster(srt) får samme navn som tittel NRK-TV.
 - Mulig og dra flere url adresser til GUI,"Threading" deling av bånbredde ved nedlasting.
 - Ingen ekstra installasjon er nødvedig,Python og ffmpeg er pakket i mappe wx_nrk_...
 - wx_nrk_32 for windows 32bit,wx_nrk_64 for windows 64bit.
 
![Valid XHTML](http://imageshack.com/a/img853/8555/pfwy.jpg).

---
### Hvordan Kjøre dette opplegget?


wx_nrk_2.7 ligger under **Downloads** i zip format.  
Pakk ut plassering er valgfritt,start **Nrk.exe**.    
wx_nrk_2.7 konverterer(fra ACC) til AC3-kodek på lyden ut. 

---
Litt info om oplegget NRK-TV kjører på etter at de gikk opp i _skyene_,  
og ingikk avtale med Akamai CDN(Cloud solution).

NRK-TV bruker Flash spiller,streaming av fragmenter(AdobeHDS) via Akamai CDN.  
Video kvalitet er _on-demand_ fra 0,2 kbps til 2,5 Mbps (inkl lyd)  
Video kvalitet er _live tv_ fra 0,2 Mbps til 3,7 Mbps (inkl lyd)  
Hver video blir kodet i 5 kvaliteter,kompressjon er MPEG4, H.264(lyd ACC kodek).   
Størrelse er fra 320×180 pixler til 1280×720 pixler.  
For undertekster bruker NRK ".str" format.
---