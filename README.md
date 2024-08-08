# Traduzio

**Traduzio** è un modulo scritto in python per [ZNC](https://znc.in/) che traduce automaticamente i messaggi utilizzando le API di Google Translate. Deve essere utilizzato con `modpython`.

## Funzionalità

- Traduzione automatica dei messaggi in canali e query.
- Configurazione della lingua di origine e destinazione.
- Abilita/disabilita la traduzione su specifici canali o nick.
- Impostazione della chiave API di Google Translate direttamente da ZNC.

### Esempio di Utilizzo

Imposta la chiave API di Google Translate:<br>
` /msg *traduzio setapi your_api_key_here` 

Imposta la lingua di origine (la tua lingua, italiano):<br>
` /msg *traduzio from it` 

Imposta la lingua di destinazione (ad esempio, inglese):<br>
` /msg *traduzio to en` 

Abilita la traduzione:<br>
` /msg *traduzio enable` 

Aggiungi un canale per la traduzione (ad esempio, #example_channel):<br>
` /msg *traduzio addchan #example_channel` 

Aggiungi un nick per la traduzione in query (ad esempio, example_nick):<br>
` /msg *traduzio addnick example_nick` 

Puoi trovare l'elenco completo dei codici lingua supportati da Google Translate nella documentazione ufficiale.<br>
` https://cloud.google.com/translate/docs/languages` 
