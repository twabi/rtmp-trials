# rtmp-trials

## Running Scipts
The scipts to run are mainSender.py and mainReceiver.py, run them simultaneously. 

## Changing params
You can change webcam params from VideoGet.py class e.g. fps or resolution. You can change the rtmp url in VideoSend.py when sending, and VideoRetrieve.py for when receiving. 

## Metric collection
I want to collect these metrics: 
- start_time (The initial time of the whole test for sender)
- start_time (The initial time of the whole test for receiver)
- end_time for sender
- end_time for receiver
- number of frames sent, 
- number of frames received, 
- frame_size (in bytes),
- total_bytes_sent
- total_bytes_received 
- sender_fps
- receiver_fps (if possible)
- * add any other metric you deem necessary thats fine

## time spans
Change the program execution time in the mainSender.py and mainReceiver.py while loops. You may run the collection on 100secs, 250sec, 500secs, 1000secs. This is sufficient

## Save format
Save final data as csv. Feel free to use whatever library you are comfortable with
