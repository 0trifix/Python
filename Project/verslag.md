# Verslag: Slimme Woning Simulatie

## Inleiding

Voor deze opdracht heb ik een slimme woning gesimuleerd in Python, volledig volgens het objectgeoriënteerd programmeren (OOP) paradigma. De simulatie bestaat uit verschillende kamers, apparaten en bewoners, gestuurd door een centrale SmartHub en voorzien van logging, met een live HTML-visualisatie. In dit verslag licht ik de ontwerpkeuzes toe, geef ik een overzicht van de structuur en reflecteer ik kort op het resultaat.

---

## Programmastructuur en OOP-toelichting

### Klassen en hun verantwoordelijkheden

De structuur is zoveel mogelijk modulair opgezet. Iedere belangrijke entiteit in de slimme woning is een aparte klasse. Hieronder volgt een kort overzicht:

- **Apparaat (basisklasse):** Algemene functionaliteit voor alle apparaten. Subklassen hiervan zijn:
  - **Lamp**
  - **Thermostaat**
  - **Deurslot**
  - **Rookmelder**
  - **Gordijn**
  - **Bewegingssensor**

- **Kamer:** Bevat een verzameling apparaten en bewoners. Is verantwoordelijk voor het beheren van deze objecten.

- **Woning:** Bevat een verzameling kamers en vormt zo de virtuele woning.

- **Bewoner:** Kan zich tussen kamers verplaatsen. Elke bewoner heeft een eigen naam en huidige kamer.

- **SmartHub:** Stuurt apparaten aan en reageert op triggers van bijvoorbeeld bewegingssensoren of tijd.

- **Logger:** Houdt alle belangrijke acties bij in een logbestand en maakt deze inzichtelijk.

- **HTML_Generator:** Maakt na elke tijdstap een live HTML-pagina aan met de status van het huis en het logboek.

### OOP-principes

- **Encapsulatie:** Elk object beheert zijn eigen data en gedrag. Bijv. een Lamp weet zijn helderheid en status.
- **Overerving:** Apparaat is de superklasse; specifieke apparaten erven hiervan.
- **Polymorfisme:** Apparaat-methodes kunnen door subklassen overschreven worden voor specifiek gedrag.
- **Samenwerking tussen objecten:** Kamers bevatten apparaten en bewoners. De woning bevat kamers. De SmartHub coördineert acties.

---

## Simulaties en automatisering

De simulatie start met twee bewoners (Jan en Sophie), elk met een eigen slaapkamer. Gedurende een dag bewegen ze volgens een vaste route door het huis. De SmartHub regelt automatisch:
- Lichten aan/uit bij beweging
- Gordijnen open/dicht op basis van tijd
- (Foutieve) pogingen bij het deurslot
- Brandalarm in de nacht

Alle acties en gebeurtenissen worden automatisch gelogd via de Logger. Na elke tijdstap wordt de status van het huis en de log live bijgewerkt in een HTML-pagina.

---

## Reflectie en keuzes

### Ontwerpkeuzes

- **Modulaire structuur:** Door elke klasse in een eigen bestand te plaatsen, blijft de code overzichtelijk en makkelijk uitbreidbaar.
- **Centrale Logger:** Door de logger als attribuut aan kamers en apparaten te koppelen, worden alle acties automatisch geregistreerd, wat zorgt voor een volledig logboek zonder veel duplicatie in de hoofdcode.
- **Live visualisatie:** Elke tijdstap wordt meteen zichtbaar gemaakt in de HTML, zodat het verloop van de simulatie goed te volgen is.

### Uitbreidbaarheid

Nieuwe apparaten, kamers, bewoners of automatiseringsregels zijn eenvoudig toe te voegen door een nieuwe klasse te schrijven en deze in het hoofdprogramma op te nemen. De bestaande structuur ondersteunt dit direct.

### Leerpunten

- **Samenwerking tussen objecten via OOP** zorgt dat de simulatie overzichtelijk blijft, ook bij uitbreiding.
- **Automatisch loggen** voorkomt vergeten acties te registreren.
- **Visualisatie** maakt het gedrag van het systeem inzichtelijk, ook voor niet-programmeurs.

---

## Conclusie

Met deze opdracht heb ik een gestructureerde, uitbreidbare simulatie van een slimme woning gerealiseerd, waarin OOP-principes volledig zijn toegepast en waarin alle gevraagde functionaliteit (meerdere bewoners, logging, automatisering, live visualisatie) aanwezig is. De code is overzichtelijk, goed gedocumenteerd en eenvoudig uit te breiden voor toekomstige functionaliteit.

