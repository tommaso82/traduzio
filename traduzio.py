import znc
import requests
import html

class traduzio(znc.Module):
    description = "Modulo utente: Traduci i messaggi utilizzando Google Translate API"

    def OnLoad(self, args, message):
        self.api_key = ""
        self.default_source_language = "it"
        self.default_target_language = "en"
        self.enabled = False
        self.channels = set()
        self.nicks = set()
        self.PutModule("Modulo caricato. Configura le opzioni di traduzione con i comandi.")
        self.PutModule("Realizzato con ❤️ da Tom :) e-mail: tom@tom.mk")
        return True

    def OnPrivMsg(self, nick, message):
        if self.enabled:
            translated_message = self.translate_message(message.s, self.default_target_language, self.default_source_language)
            message.s = translated_message
        return znc.CONTINUE

    def OnChanMsg(self, nick, channel, message):
        if self.enabled and channel.GetName() in self.channels:
            translated_message = self.translate_message(message.s, self.default_target_language, self.default_source_language)
            message.s = translated_message
        return znc.CONTINUE

    def OnUserMsg(self, target, message):
        if self.enabled and (str(target).lower() in self.channels or str(target).lower() in self.nicks):
            translated_message = self.translate_message(message.s, self.default_source_language, self.default_target_language)
            message.s = translated_message
        return znc.CONTINUE

    def translate_message(self, message, source_lang, target_lang):
        return self.translate_text(message, source_lang, target_lang)

    def translate_text(self, text, source_lang, target_lang):
        url = "https://translation.googleapis.com/language/translate/v2"
        params = {
            'q': text,
            'target': target_lang,
            'key': self.api_key
        }
        if source_lang:
            params['source'] = source_lang
        response = requests.get(url, params=params)
        response_json = response.json()
        if response.status_code == 200 and 'data' in response_json and 'translations' in response_json['data']:
            translated_text = response_json['data']['translations'][0]['translatedText']
            decoded_text = html.unescape(translated_text)
            return decoded_text
        else:
            self.PutModule(f"Errore nella risposta della traduzione: {response_json}")
            return text

    def cmd_setapi(self, api_key):
        self.api_key = api_key
        self.PutModule("API key impostata.")

    def cmd_from(self, lang):
        self.default_source_language = lang
        self.PutModule(f"Lingua di origine impostata su: {lang}")

    def cmd_to(self, lang):
        self.default_target_language = lang
        self.PutModule(f"Lingua di destinazione impostata su: {lang}")

    def cmd_enable_translation(self):
        self.enabled = True
        self.PutModule("Traduzione abilitata.")

    def cmd_disable_translation(self):
        self.enabled = False
        self.PutModule("Traduzione disabilitata.")

    def cmd_addchan(self, channel):
        if not channel.startswith('#'):
            channel = f'#{channel}'
        self.channels.add(channel.lower())
        self.PutModule(f"Canale aggiunto per la traduzione: {channel}")

    def cmd_delchan(self, channel):
        if not channel.startswith('#'):
            channel = f'#{channel}'
        self.channels.discard(channel.lower())
        self.PutModule(f"Canale rimosso dalla traduzione: {channel}")

    def cmd_listchans(self):
        chans = ', '.join(self.channels)
        self.PutModule(f"Canali attivi per la traduzione: {chans}")

    def cmd_addnick(self, nick):
        self.nicks.add(nick.lower())
        self.PutModule(f"Nick aggiunto per la traduzione: {nick}")

    def cmd_delnick(self, nick):
        self.nicks.discard(nick.lower())
        self.PutModule(f"Nick rimosso dalla traduzione: {nick}")

    def cmd_listnicks(self):
        nicks = ', '.join(self.nicks)
        self.PutModule(f"Nicks attivi per la traduzione: {nicks}")

    def OnModCommand(self, command):
        parts = command.split()
        if len(parts) < 1:
            return

        cmd = parts[0].lower()
        if cmd == "setapi" and len(parts) == 2:
            self.cmd_setapi(parts[1])
        elif cmd == "from" and len(parts) == 2:
            self.cmd_from(parts[1])
        elif cmd == "to" and len(parts) == 2:
            self.cmd_to(parts[1])
        elif cmd == "enable":
            self.cmd_enable_translation()
        elif cmd == "disable":
            self.cmd_disable_translation()
        elif cmd == "addchan" and len(parts) == 2:
            self.cmd_addchan(parts[1])
        elif cmd == "delchan" and len(parts) == 2:
            self.cmd_delchan(parts[1])
        elif cmd == "listchans":
            self.cmd_listchans()
        elif cmd == "addnick" and len(parts) == 2:
            self.cmd_addnick(parts[1])
        elif cmd == "delnick" and len(parts) == 2:
            self.cmd_delnick(parts[1])
        elif cmd == "listnicks":
            self.cmd_listnicks()
        elif cmd == "help":
            self.cmd_help()
        else:
            self.PutModule(f"Comando sconosciuto: '{cmd}' prova help")

    def cmd_help(self):
        self.PutModule("Comandi disponibili:")
        self.PutModule("  setapi <key> - Imposta la API key")
        self.PutModule("  from <lang> - Imposta la lingua di origine")
        self.PutModule("  to <lang> - Imposta la lingua di destinazione")
        self.PutModule("  enable - Abilita la traduzione")
        self.PutModule("  disable - Disabilita la traduzione")
        self.PutModule("  addchan <channel> - Aggiunge un canale per la traduzione")
        self.PutModule("  delchan <channel> - Rimuove un canale dalla traduzione")
        self.PutModule("  listchans - Mostra la lista dei canali per la traduzione")
        self.PutModule("  addnick <nick> - Aggiunge un nick per la traduzione")
        self.PutModule("  delnick <nick> - Rimuove un nick dalla traduzione")
        self.PutModule("  listnicks - Mostra la lista dei nicks per la traduzione")
        self.PutModule("  help - Mostra questo messaggio di aiuto")
