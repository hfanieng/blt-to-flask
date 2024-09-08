# Status Update Trigger Expression

__Beschreibung__
Diese Funktion wird aufgerufen, wenn ein Status-Update-Paket vom Player empfangen wird, den die Trigger-Funktion verfolgt, nachdem die Filterausdruck-Erfassung (wenn vorhanden) bestimmt hat, ob der Trigger aktiviert ist, und nachdem der Aktivierungs- oder Deaktivierungsausdruck (soweit zutreffend) ausgeführt wurde.

Die Status-Update-Objekt eines beat-link ```CdjStatus``` wird als ```status``` zur Verfügung gestellt und kann über normalen Clojure-Java-Interop-Syntax auf seine Felder und Methoden zugegriffen werden. Es ist jedoch einfacher, die Convenience-Variablen zu verwenden, die unten beschrieben sind.

Wenn Sie nur Updates senden möchten, wenn der Trigger aktiviert ist (d.h. wenn er eingeschaltet ist und ein beobachteter Player läuft), sollten Sie Ihren Code innerhalb einer when-Ausdruck konditionieren, der auf den Convenience-Variablen trigger-active? abzielt.

Die Variablen ```locals``` und ```globals``` sind für alle Ausdrücke auf diesem Trigger verfügbar. Während locals spezifisch für diesen Trigger ist, wird globals über alle Ausdrücke in jedem Trigger geteilt

---

## Device Informationen

### address

- Die Adresse des Geräts, von dem dieses Update empfangen wurde.

---

## Musikstatus

### at-end?

Ist der Player am Ende einer Strecke angehalten?

### bar-meaningful?

Gibt es eine bedeutende Barinformation für das verwendete Gerät?

### bar-number

Identifiziert die Bar, in der der letzte Schlag fällt. Die Zählung beginnt bei 1 und erhöht sich mit jedem Downbeat.

### beat-number

Identifiziert den Beat im aktuellen Track, der gerade gespielt wird. Die Zählung beginnt bei 1 und erhöht sich mit jedem Beat.

### beat-within-bar

Gibt an, an welcher Stelle innerhalb eines Musikmaßes der letzte Beat fällt (Wert von 1 bis 4, wobei 1 den Downbeats darstellt).

### beat?

Wird True geliefert, wenn das Update einen neuen Beat ankündigt.

---

## Player-Status

### busy?

Gibt an, ob der Player aktiv ist.

### cdj?

Wird True geliefert, wenn das Update den Status eines CDJ-Geräts meldet.

### cued?

Gibt an, ob der Player an einer Cue-Position angehalten wurde.

---

## Cue-Informationen

### cue-countdown

Gibt die Anzahl der Beats ab, bis ein Cue-Punkt erreicht wird. Wenn es keinen Cue-Punkt gibt oder dieser mehr als 64 Bars entfernt ist, wird der Wert 511 zurückgegeben.

### cue-countdown-text

Enthält die Informationen von cue-countdown im Format, wie sie auf dem Player angezeigt werden.

---

## Zeit- und Tempo-Informationen

### effective-tempo

Gibt den effektiven Spieltempo an, der sowohl aus der Track-BPM als auch aus der Pitch-Einstellung berechnet wird.

### on-air?

Gibt an, ob der CDJ aktuell auf Sendung ist (d.h. wenn er mit einem Mixer-Channel verbunden ist, das nicht abgedunkelt ist).

### paused?

Gibt an, ob der Player angehalten wurde.

### playing?

Gibt an, ob der Player ein Track spielt.

### pitch-multiplier

Enthält den aktuellen Geräte-Pitch-Einstellung als Multiplikator von 0,0 bis 2,0, wobei 1,0 die normale Spielgeschwindigkeit darstellt und 0,0 bedeutet, dass der Player angehalten wurde.

### pitch-percent

Enthält den aktuellen Geräte-Pitch-Einstellung als Prozentsatz von -100% bis +100%, wobei 0% die normale Spielgeschwindigkeit darstellt.

---

## Track-Informationen

### track-album

Gibt den Albumnamen des gerade gespielten Tracks an.

### track-artist

Gibt den Künstler des gerade gespielten Tracks an.

### track-bpm

Gibt den aktuellen BPM-Wert des gerade gespielten Tracks an.

### track-comment

Enthält die Kommentare des gerade gespielten Tracks.

### track-genre

Gibt den Musikgenre des gerade gespielten Tracks an.

### track-key

Gibt die Tonart des gerade gespielten Tracks an.

### track-label

Gibt das Label des gerade gespielten Tracks an.

### track-length

Gibt die Länge des gerade gespielten Tracks in Sekunden an.

### track-metadata

Enthält alle verfügbaren Metadaten zum gerade gespielten Track.

### track-number

Identifiziert die Stellennummer des gerade gespielten Tracks innerhalb einer Playlist oder ähnlicher Liste auf dem CDJ-Browser-Interface.

### track-source-player

Gibt den Player an, von dem der gerade gespielte Track geladen wurde (falls zutreffend).

### track-source-slot

Gibt das Slot an, aus dem der gerade gespielte Track geladen wurde.

### track-time-reached

Enthält die Zeit, bis wann des gerade gespielten Tracks erreicht wurde (falls zutreffend).

### track-title

Gibt den Titel des gerade gespielten Tracks an.

### track-type

Identifiziert den Typ des gerade gespielten Tracks.

---

## Trigger-Eigenschaften

### trigger-active?

Wird True geliefert, wenn der Trigger aktiv ist und mindestens ein beobachter Player läuft.

### trigger-channel

Gibt den MIDI-Kanal an, auf dem der Trigger konfiguriert ist, eine MIDI-Nachricht zu senden.

### trigger-comment

Enthält einen beschreibenden Kommentar zum Trigger.

### trigger-enabled

Gibt an, unter welchen Bedingungen der Trigger aktiviert wird (z.B. immer, nur wenn ein bestimmter Player läuft, etc.).

### trigger-message

Gibt den Typ der MIDI-Nachricht an, die der Trigger senden soll (z.B. Note, CC, Clock, Link oder Custom).

### trigger-note

Gibt den MIDI-Note-Wert oder CC-Nummer an, den der Trigger senden soll.

### trigger-output

Enthält das gewählte MIDI-Ausgabegerät für diesen Trigger.


