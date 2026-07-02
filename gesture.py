class GestureRecognizer:

    def finger_up(self, tip, pip, lm):
        return lm[tip].y < lm[pip].y

    def thumb_closed(self, lm, hand_label):
        # Different thumb direction for left and right hand
        if hand_label == "Right":
            return lm[4].x > lm[3].x
        else:
            return lm[4].x < lm[3].x

    def recognize(self, landmarks, hand_label):

        thumb_closed = self.thumb_closed(landmarks, hand_label)

        index = self.finger_up(8, 6, landmarks)
        middle = self.finger_up(12, 10, landmarks)
        ring = self.finger_up(16, 14, landmarks)
        pinky = self.finger_up(20, 18, landmarks)

        # Thumb must stay folded
        if not thumb_closed:
            return None

        # -----------------------------
        # Right Hand
        # -----------------------------
        if hand_label == "Right":

            if index and not middle and not ring and not pinky:
                return "RIGHT_ONE"

            if index and middle and not ring and not pinky:
                return "RIGHT_TWO"

            if index and middle and ring and not pinky:
                return "RIGHT_THREE"

            if index and middle and ring and pinky:
                return "RIGHT_FOUR"

        # -----------------------------
        # Left Hand
        # -----------------------------
        else:

            if index and not middle and not ring and not pinky:
                return "LEFT_ONE"

            if index and middle and not ring and not pinky:
                return "LEFT_TWO"

            if index and middle and ring and not pinky:
                return "LEFT_THREE"

            if index and middle and ring and pinky:
                return "LEFT_FOUR"

        return None