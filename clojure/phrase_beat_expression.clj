(let [payload {"Message"				"phrase"
			"beat-number"			beat-number
			"bpm"					effective-tempo
			"device_name"			device-name
			"device_number"			device-number
			"fill"               	(= section :fill)
			"phrase_type"			phrase-type
			"section"				section
			"track_album"  			track-album
			"track_bank"			track-bank
            "track_artist" 			track-artist
            "track_bpm"				track-bpm
			"track_genre"			track-genre
			"track_key"				track-key
			"track_label"			track-label
			"track_length"			track-length
			"track_time_reached"	track-time-reached
			"track_title"  			track-title}
json-payload (cheshire.core/encode payload)     	; JSON encode
    headers {"Content-Type" "application/json"}     ; Set header
    request-options {:body json-payload             ; Create payload
                    :headers headers}]             	; Insert header in the options
(timbre/info "Sending JSON payload:" request-options)  ; Output JSON and options
(send-json-to-flask-server "http://127.0.0.1:5000/api/receive_data" request-options))