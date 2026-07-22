import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from deep_translator import GoogleTranslator

# تهيئة أداة jnius لربط البايثون بنظام جافا للأندرويد (تمنع إغلاق التطبيق)
try:
    from jnius import autoclass
    AndroidTTS = True
except:
    AndroidTTS = False

class AI_TranslatorApp(App):
    def build(self):
        # محرك الترجمة الذكي والمجاني من جوجل
        self.translator = GoogleTranslator(source='ar', target='en')
        
        # تصميم واجهة التطبيق الاحترافية بالألوان والأزرار
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        # العنوان الرئيسي للتطبيق
        title = Label(text="AI Translator Pro", font_size='26sp', color=(0.1, 0.6, 1, 1), bold=True, size_hint_y=0.1)
        layout.add(title)
        
        # صندوق إدخال النص العربي
        self.input_text = TextInput(hint_text="✍️ اكتب أو املأ النص العربي هنا...", font_size='20sp', size_hint_y=0.3, halign='right')
        layout.add(self.input_text)
        
        # شاشة عرض الترجمة الإنجليزية
        self.output_label = Label(text="الترجمة الإنجليزية ستظهر هنا", font_size='20sp', size_hint_y=0.3, color=(1, 1, 1, 1))
        layout.add(self.output_label)
        
        # زر الترجمة الفورية والنطق الصوتي
        btn = Button(text="🔊 ترجم وانطق فوراً", font_size='22sp', background_color=(0.1, 0.6, 1, 1), size_hint_y=0.2, bold=True)
        btn.bind(on_press=self.process_translation)
        layout.add(btn)
        
        # تحضير محرك الصوت الداخلي للأندرويد مسبقاً إذا كان التطبيق يعمل على الجوال
        if AndroidTTS:
            try:
                Locale = autoclass('java.util.Locale')
                TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                
                # ربط محرك النطق بواجهة أندرويد الحالية للنشاط
                self.tts = TextToSpeech(PythonActivity.mActivity, None)
                self.locale_en = Locale.US
            except:
                pass
        
        return layout

    def process_translation(self, instance):
        arabic_text = self.input_text.text.strip()
        if not arabic_text:
            self.output_label.text = "⚠️ يرجى إدخال نص أولاً!"
            return
            
        self.output_label.text = "جاري الترجمة الصوتية الفورية..."
        try:
            # 1. الترجمة الفورية عبر الذكاء الاصطناعي لجوجل
            english_text = self.translator.translate(arabic_text)
            self.output_label.text = f"🔹 Translation:\n{english_text}"
            
            # 2. تشغيل النطق الصوتي بالإنجليزية عبر النظام الداخلي الآمن للأندرويد
            if AndroidTTS:
                try:
                    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
                    self.tts.setLanguage(self.locale_en)
                    self.tts.speak(english_text, TextToSpeech.QUEUE_FLUSH, None, None)
                except:
                    self.output_label.text = f"🔹 Translation:\n{english_text}\n(عذراً، محرك الصوت بالجهاز غير مستعد)"
            else:
                # إذا كنت تجربه للاختبار على الكمبيوتر يطبع النص فقط بدون صوت لمنع الأخطاء
                print(f"صوت المترجم: {english_text}")
                
        except Exception as e:
            self.output_label.text = f"خطأ في الاتصال بالإنترنت"

if __name__ == "__main__":
    AI_TranslatorApp().run()
