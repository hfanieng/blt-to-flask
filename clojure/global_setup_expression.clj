(defn init-globals []
  (let [url "http://127.0.0.1:5000/api/receive_data"]
    (swap! globals assoc-in [:flask-server-url] url)))

(init-globals)