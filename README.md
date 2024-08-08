# Traduzio

**Traduzio** è un modulo per [ZNC](https://znc.in/) che traduce automaticamente i messaggi utilizzando Google Translate API. Configura le lingue di origine e destinazione e abilita la traduzione su canali e nick specifici.

## Funzionalità

- Traduzione automatica dei messaggi in canali e query.
- Configurazione della lingua di origine e destinazione.
- Abilita/disabilita la traduzione su specifici canali o nick.
- Impostazione della chiave API di Google Translate direttamente da ZNC.

Esempio di Utilizzo

Imposta la chiave API di Google Translate:
/msg *traduzio setapi your_api_key_here

Imposta la lingua di origine (ad esempio, italiano):
/msg *traduzio from it

Imposta la lingua di destinazione (ad esempio, inglese):
/msg *traduzio to en

Abilita la traduzione:
/msg *traduzio enable

Aggiungi un canale per la traduzione (ad esempio, #example_channel):
/msg *traduzio addchan #example_channel

Aggiungi un nick per la traduzione in query (ad esempio, example_nick):
/msg *traduzio addnick example_nick

Codici Lingua
Puoi trovare l'elenco completo dei codici lingua supportati da Google Translate nella documentazione ufficiale.
https://cloud.google.com/translate/docs/languages
