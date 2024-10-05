from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test1 = emotion_detector('I hate working long hours')
        self.assertEqual(test1['emotion'], 'anger')

        test2 = emotion_detector('I love it')
        self.assertEqual(test2['emotion'], 'joy')

        test3 = emotion_detector('I am glad this happened')
        self.assertEqual(test3['emotion'], 'joy')

        test4 = emotion_detector('I am really mad about this')
        self.assertEqual(test4['emotion'], 'anger')

        test5 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test5['emotion'], 'disgust')

        test6 = emotion_detector('I am so sad about this')
        self.assertEqual(test6['emotion'], 'sadness')

        test7 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test7['emotion'], 'fear')

unittest.main()