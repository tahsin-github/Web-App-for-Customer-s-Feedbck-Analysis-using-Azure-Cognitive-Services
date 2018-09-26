from flask import render_template, url_for, flash, redirect
from azuretext import app, db
from azuretext.textinput import TextComment
from azuretext.models import comment, textanalysis
from azuretext.azureapi import *
from azuretext.azureapikey import *



@app.route("/", methods = ['GET', 'POST'])
def home():    
    text_form = TextComment()
    if text_form.validate_on_submit():        
        TEXT = comment(text = text_form.comment.data)
        db.session.add(TEXT)
        db.session.commit()
        
        documents = { 'documents': [
            { 'id': '2', 'text':  TEXT.text}
        ]}

        analysis = AzureText(host_lng, path_lng, subscription_key_lng,host_tr, path_tr, subscriptionKey_tr,  documents).result
        analysis['KeyPhrase'] = str(analysis['KeyPhrase'])

        
        analysis_result = textanalysis(text = TEXT.text, 
                                        detectedLanguage = analysis.get('detectedLanguage'),
                                        language_iso639Name = analysis.get('language_iso639Name'),
                                        sentiment = analysis.get('sentiment'),
                                        translation = analysis.get('translation'),
                                        KeyPhrase = analysis.get('KeyPhrase') 
                                        )
        db.session.add(analysis_result)
        db.session.commit()

        analysis['main_text'] = TEXT.text

        flash(f'The text analysis is done. See the results here !', 'success')
        return render_template('results.html', results = analysis)
    
    

    return render_template('home.html', form = text_form)

    

    




