from django.shortcuts import render
import pafy
from django.http import HttpResponse
from django.template.defaultfilters import filesizeformat

# Create your views here.



def Downloader(request):
	if request.method=='POST':
		video_url= request.POST.get('title')
		if 'm.' in video_url:
			video_url = video_url.replace(u'm.', u'')

		elif 'youtu.be' in video_url:
			video_id = video_url.split('/')[-1]
			video_url = 'https://www.youtube.com/watch?v=' + video_id

		if len(video_url.split("=")[-1]) != 11:
			return HttpResponse('Enter correct url.')

		video = pafy.new(video_url)
		stream = video.streams
		video_audio_streams = []
		for s in stream:
			video_audio_streams.append({
				'resolution': s.resolution,
				'extension': s.extension,
				'file_size': filesizeformat(s.get_filesize()),
				'video_url': s.url + "&title=" + video.title
			})

		

		stream_audio = video.audiostreams
		audio_streams = []
		for s in stream_audio:
			audio_streams.append({
				'resolution': s.resolution,
				'extension': s.extension,
				'file_size': filesizeformat(s.get_filesize()),
				'video_url': s.url + "&title=" + video.title
			})

		


		context = {
			
			
			
			
			
			'title': video.title,'streams': video_audio_streams,
			'stream_audio': audio_streams,
			
			
		}
		# context = {
			
		# 	'title': video.title, 'streams': video_audio_streams,
		# 	'description': video.description, 'likes': video.likes,
		# 	'dislikes': video.dislikes, 'thumb': video.bigthumbhd,
		# 	'duration': video.duration, 'views': video.viewcount,
		# 	'stream_video': video_streams, 'stream_audio': audio_streams
		# }
		return render(request,'home.html',context)
		# 'stream_video': video_streams

	return render(request,'home.html')