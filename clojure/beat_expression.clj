(let [payload {"Message"				"Track"
			"beat-number"			beat-number
			"device_name"			device-name
               "device_number"		device-number
			"track_album"  		track-album
               "track_artist" 		track-artist
               "track_bpm"			track-bpm
			"track_genre"			track-genre
			"track_label"			track-label
			"track_lengths"		track-length
			"track_title"  		track-title
               }
     json-payload (cheshire.core/encode payload)     ; JSON kodieren
     headers {"Content-Type" "application/json"}     ; Header setzen
     request-options {:body json-payload             ; Payload anlegen
                    :headers headers}]             ; Header in die Optionen einfügen
(timbre/info "Sending JSON payload:" request-options)  ; JSON und Optionen ausgeben
(my-ns/send-json-to-flask-server "http://127.0.0.1:5000/api/receive_data" request-options))