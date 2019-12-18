; loads and runs a specific problem in the repl
(defn run [problem-number]
  (let [name (str "problem" problem-number)
        file (str "src/" name ".clj")]
    (load-file file)
    ((resolve (symbol name)))))