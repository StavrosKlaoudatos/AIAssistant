def Take_Video():
    import numpy as np
    import cv2
    import time as tm
    import speech_recognition as sr
    from Speak_Text import SpeakText

    time = str(tm.localtime().tm_mday) + '_' + str(tm.localtime().tm_hour)+'_'+str(tm.localtime().tm_min)+'.avi'
    r = sr.Recognizer()
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(time,fourcc, 20.0, (640,480))

    SpeakText('To prevent false trigger of a break function, in order to stop the program you need to press q in the keyboard!')

    while(cap.isOpened()):






        ret, frame = cap.read()
        if ret==True:



            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

