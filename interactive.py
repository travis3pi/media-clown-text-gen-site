from textgenrnn import textgenrnn

textgen = textgenrnn(weights_path='./des-train_weights.hdf5', vocab_path='./des-train_vocab.json',
                     config_path='./des-train_config.json')

textgen.generate(interactive=True, top_n=5)