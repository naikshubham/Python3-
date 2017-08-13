import cmu_sphinx4
#step2 read audio file
audio_url='http://download2.prokerala.com/downloads/ringtones/files/mp3/sound-clip-37-29552.mp3'
transcriber=cmu_sphinx4.Transcriber(audio_url)
#step 3 : print it out
for line in transcriber.transcript_stream():
	print(line)
