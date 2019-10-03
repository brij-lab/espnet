# script to make old LM model compatible with new espnet, since some keys are renamed

import torch

path = 'exp/train_rnnlm_pytorch_1layer_unit1024_sgd_bs1024_unigram5000/rnnlm.model.best'
new_path = 'exp/train_rnnlm_pytorch_1layer_unit1024_sgd_bs1024_unigram5000/rnnlm.model.bestmod'

snapshot = torch.load(path, map_location=lambda storage, loc: storage)

snapshot['predictor.rnn.0.weight_ih'] = snapshot.pop('predictor.lstm.0.weight_ih')
snapshot['predictor.rnn.0.weight_hh'] = snapshot.pop('predictor.lstm.0.weight_hh')
snapshot['predictor.rnn.0.bias_ih'] = snapshot.pop('predictor.lstm.0.bias_ih')
snapshot['predictor.rnn.0.bias_hh'] = snapshot.pop('predictor.lstm.0.bias_hh')

torch.save(snapshot, new_path)
