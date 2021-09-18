# naszemiasto
Pobieranie zdjęć z galerii w xyz.naszemiasto.pl w normalny sposób  
Sekwencyjne, aczkolwiek sprawne i 10 razy szybsze od przeklikiwania tamtej paskudnej strony  
Usuńcie f-stringi dla zmniejszenia wymaganej wersji Pythona  

### Wymagania:
**requests, bs4, re**

## Zastosowanie:

```bash
python3 naszemiasto.py <URL> # URL do pierwszego zdjęcia w otwartej galerii  
wget -i images.txt -U 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' # pobiera do obecnego folderu
```
