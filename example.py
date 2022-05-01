import s3prl.hub as hub

model = getattr(hub, 'wav2vec2')()  # build the Wav2Vec 2.0 model with pre-trained weights

print(model)