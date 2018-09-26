from socket import gaierror
import http.client, uuid, json, copy

# Text Analysis
class AzureTextAnalysis:
    
    def __init__(self, host, path, text_analysis, subscription_key, documents):
        
        doc = json.dumps(documents)
        headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
        
        self.resp_error = {}


        try:
            conn = http.client.HTTPSConnection(host)
            conn.request("POST", path + text_analysis , body = doc , headers = headers)
            self.resp = json.loads(conn.getresponse().read().decode("utf-8"))
        except gaierror:
            error = "Wrong Host Name."
            self.resp_error['error'] = error
        except JSONDecodeError:
            error = "Wrong Path Name or text_analysis Name"
            self.resp_error['error'] = error
        

        
# Translation
class AzureTranslation:
    
    def __init__(self, host_tr, path_tr, subscriptionKey_tr, documents):
        
        self.resp_error = {}        
        # document
        text = documents['documents'][0]['text']

        requestBody = [{
            'Text' : text,
        }]

        content = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')

        headers = {
            'Ocp-Apim-Subscription-Key': subscriptionKey_tr,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # Translate to English.
        params = "&to=en";


        try:

            conn = http.client.HTTPSConnection(host_tr)
            conn.request ("POST", path_tr + params, content, headers)
            self.resp = json.loads(conn.getresponse().read().decode("utf-8"))
        except gaierror:
            error = "Wrong Host Name."
            self.resp_error['error'] = error
        except JSONDecodeError:
            error = "Wrong Path Name or text_analysis Name"
            self.resp_error['error'] = error

            
# text analysis and translation
class AzureText:
    
    def __init__(self, host_lng, path_lng, subscription_key_lng,host_tr, path_tr, subscription_key_tr, documents):
        
        self.result = {}  # an empty dictionary to store the results.
        
        
        # Language Detection
        
        language_detection = AzureTextAnalysis(host_lng, path_lng, "languages" , subscription_key_lng, documents)
        
        self.result['detectedLanguage'] = language_detection.resp['documents'][0]['detectedLanguages'][0]['name']
        self.result['language_iso639Name'] = language_detection.resp['documents'][0]['detectedLanguages'][0]['iso6391Name'] 
        
        # Sentiment Analysis
        
        # add the detected language name into the document        
        documents['documents'][0]['language'] = language_detection.resp['documents'][0]['detectedLanguages'][0]['iso6391Name']       
        sentiment_analysis = AzureTextAnalysis(host_lng, path_lng, "sentiment" , subscription_key_lng, documents)  
        
        self.result['sentiment'] = sentiment_analysis.resp['documents'][0]['score']
        
        
        # Extract key phrases if the language is English, else translate and extract the key phrase.
        
        if language_detection.resp['documents'][0]['detectedLanguages'][0]['iso6391Name'] == 'en':
            key_phrase = AzureTextAnalysis(host_lng, path_lng, "keyPhrases" , subscription_key_lng, documents)
            self.result['KeyPhrase'] = key_phrase.resp['documents'][0]['keyPhrases']
            
        else:
            trans = AzureTranslation(host_tr, path_tr, subscription_key_tr, documents)
            self.result['translation'] = trans.resp[0].get('translations')[0].get('text')
            documents_tr = copy.deepcopy(documents)
            documents_tr['documents'][0]['text'] = self.result.get('translation')
            documents_tr['documents'][0]['language'] = 'en'
            key_phrase = AzureTextAnalysis(host_lng, path_lng, "keyPhrases" , subscription_key_lng, documents_tr)
            self.result['KeyPhrase'] = key_phrase.resp['documents'][0]['keyPhrases']
                                    
                        
