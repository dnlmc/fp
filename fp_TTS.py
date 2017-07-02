import json
from watson_developer_cloud import AuthorizationV1
from watson_developer_cloud import TextToSpeechV1

# get credentials & authorize per https://www.ibm.com/watson/developercloud/doc/common/getting-started-credentials.html 
# & https://github.com/watson-developer-cloud/python-sdk/tree/master/examples
authorization = AuthorizationV1(
    username='my_username',
    password='my_password')

text_to_speech = TextToSpeechV1(
    username='my_username',
    password='my_password',
    x_watson_learning_opt_out=True)  
    
# loop thru list of cleaned posts  
counter = 0
for i in friend17clean:
    
    # skip blank entries
    if i != '':
        
        # assign post text to TextBlob object & retrieve polarity & subjectivity scores
        tempblob = tb(i)
        pol = tempblob.sentiment.polarity*100     # multiply by 100 to scale float to integer percentage 
        sub = tempblob.sentiment.subjectivity*100
        
        # various if else statements handle differing lengths of returned integer to truncate decimals
        if pol == 100:
            pitch = pol
        elif pol >= 0:
            pitch = str(pol)[0:2]
        elif pol == -100:
            pitch = str(pol)[0:4]
        else:
            pitch = str(pol)[0:3]
       
        if sub == 100:
            glot = sub
        else:
            glot = str(sub)[0:3]
        
        breath = float(pitch) * float(glot)
        rate = pol-sub
        
        if pol >= 77:
            timbre = 'Breeze'
        else: timbre = 'Sunrise'
        
        # Call Watson API, feed values from above into parameters, save as .wav file
        with open('friend17_'+str(counter)+'.wav','wb') as audio_file: 
            audio_file.write(text_to_speech.synthesize(
            '<voice-transformation type="Custom" breathiness="'+str(breath)[0:2]+'%" \
            pitch="'+str(pitch)+'%" pitch_range="-70%" rate="'+str(rate)[0:3]+'%" \
            glottal_tension="'+str(glot)+'%" timbre="'+timbre+'">'+ i +'</voice-transformation>', 
            accept='audio/wav', voice="en-US_MichaelVoice"))
            
        counter += 1