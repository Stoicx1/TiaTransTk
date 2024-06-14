import deepl

translator = deepl.Translator("52f5e3b1-bc16-4476-92bd-ed4ba45f9715:fx")

def GetTranslation(txtToTranslate, targetLanguage):
    txtTranslated = translator.translate_text(txtToTranslate, target_lang=targetLanguage)
    return txtTranslated