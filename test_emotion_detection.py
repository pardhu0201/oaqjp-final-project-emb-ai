from EmotionDetection import emotion_detector

def test_emotion(text, expected_emotion):
    response = emotion_detector(text)

    if response["dominant_emotion"] == expected_emotion:
        print(f"PASSED: {text}")
    else:
        print(f"FAILED: {text}")
        print(f"Expected: {expected_emotion}")
        print(f"Got: {response['dominant_emotion']}")

test_emotion("I am glad this happened", "joy")
test_emotion("I am really mad about this", "anger")
test_emotion("I feel disgusted just hearing about this", "disgust")
test_emotion("I am so sad about this", "sadness")
test_emotion("I am really afraid that this will happen", "fear")
