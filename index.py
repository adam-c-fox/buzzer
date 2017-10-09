import pygame
import web
from web import form

render = web.template.render('Templates/')

urls = ('/', 'Index',
		'/klaxon', 'klaxon')

app = web.application(urls, globals())

myform = form.Form(
	form.Dropdown('Name', ['Adam', 'Amy', 'Ben', 'Denis', 'Ellie', 'Julie', 'Michael', 'Nigel', 'Sarah', 'Simon', 'Wendy']),
	form.Button('BUZZ', id="button", class_="subButton"))
	
klaxonForm = form.Form(
	form.Button('klaxon', id='button', class_='klaxButton', value='true'))

pygame.init()
pygame.mixer.init()

class Index:
	def GET(self):
		form = myform()
    		return render.formtest(form)

	def POST(self):
		form = myform()
    		if not form.validates(web.input(Name=[])):
    			return render.formtest(form)
    		else:

    			if (form['Name'].value) == [u'Adam']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('adam.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    				
    			elif (form['Name'].value) == [u'Amy']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('amy.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Ben']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('ben.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Denis']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('denis.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Ellie']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('ellie.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Julie']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('julie.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Michael']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('michael.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Nigel']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('nigel.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Sarah']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('sarah.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Simon']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('simon.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    					
    			elif (form['Name'].value) == [u'Wendy']:
    				if pygame.mixer.music.get_busy() == True:
    					return render.failure()
    				else:
    					pygame.mixer.music.load('wendy.wav')
    					pygame.mixer.music.play()
    					return render.buzzed()
    				
    				    				
    			else:
    				return render.index(form['Name'].value)
    					
class klaxon:
	def GET(self):
		form = klaxonForm()
		return render.klaxon(form)
			
	def POST(self):
		form = klaxonForm()
		if not form.validates():
			return render.klaxon(form)
		else:
		
			if (form['klaxon'].value) == "true":
				pygame.mixer.music.load('klaxon.wav')
				pygame.mixer.music.play()
				return render.buzzed()
			else:
 				return (form['klaxon'].value)

if __name__=='__main__':
	web.internalerror = web.debugerror
	app.run()
