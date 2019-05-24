
#mysql library
import mysql.connector


#python library
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError




db = mysql.connector.connect(
                              host="27.254.90.149",
                              user="kittipob",
                              passwd="Kg+Q9}Aa2uKq'rG#",
                              database="csloxinfo"
                            );

cursor = db.cursor();



sqlAlarms = "SELECT A.AlarmID, FROM_UNIXTIME(A.StartTime,'%d/%m/%y %H:%i') , A.LCUID , B.ParentID AS RoomID, B.NodeName , C.user_id , D.lineId, E.AlarmName FROM `alarmhistory` AS A LEFT OUTER JOIN `treeview` AS B ON A.LCUID = B.LCUID LEFT OUTER JOIN `user_tree` AS C ON B.ParentID = C.tree_id LEFT OUTER JOIN `users` AS D ON D.id = C.user_id LEFT OUTER JOIN `alarmlist` AS E ON A.AlarmID = E.AlarmID WHERE A.EndTime is null";

cursor.execute(sqlAlarms);
alarms = cursor.fetchall();

for alarm in alarms :
     startTime = alarm[1];
     lcuName   = alarm[4];
     lineId    = alarm[6];
     alarmName = alarm[7];
     print(alarm);
     try:
        # ini a connector
        line_bot_api = LineBotApi('onJyoGU83OkwXmoDXPFKaT1RvLC5WGpZlzpTpzTiHbMzWfnheB7shTyz8FVXckxME+xPbMVBHUbRU+TKBJlHN82MNCit2Jz7rZAzaF3HwV20X4m6FPBbSiR4pMriPgTtN0+wwaW6hZWLCfRzi0qYIQdB04t89/1O/w1cDnyilFU=');

        print("send to" + str(lineId));
        alarmMsg = "ระบบ :" + lcuName + "\nชื่อ :" + alarmName + "\nเวลาเกิด:" + str(startTime);
        line_bot_api.push_message(lineId, TextSendMessage(text=alarmMsg));

     except LineBotApiError as e:
        print("error" + str(e));
