(require '[org.httpkit.client :as httpkit-client])
(require '[cheshire.core :as json])

(defn send-json-to-flask-server
  "Encodes a map as JSON and sends it in a HTTP POST request
  to the Flask server."
  [url request-options]
  (httpkit-client/post url request-options))  ; Transfer options (including header)