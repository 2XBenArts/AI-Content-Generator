import google.generativeai as genai
import config
genai.configure( 'AIzaSyA0-37asyzLgCKp4BbOxJke9M3w8S2UEGo' ) #AlzaSyA0-37asyzLgCKp4BbOxJke9M3w8S2UEGo)

def openAIQuery(query):
    response = genai.Completion.create(
      prompt= query,
      temperature=0.8,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)

    print(response) 


    if 'choices' in response:
      if len(response['choices']) > 0:
        answer = response['choices'][0]['text']
      else:
        answer = 'Opps sorry, you beat the AI this time'
    else:
      answer = 'Opps sorry, you beat the AI this time'
    return answer
