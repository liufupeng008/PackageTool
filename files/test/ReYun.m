#import "XFNotificationController.h"
#if defined(__IPHONE_10_0) && (__IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_10_0)
#import <UserNotifications/UserNotifications.h>
#endif
@implementation XFNotificationController
static dispatch_once_t onceToken;
static XFNotificationController *sharedInstance;
+(XFNotificationController *)sharedInstance{
    dispatch_once(&onceToken, ^{
        sharedInstance = [[XFNotificationController alloc] init];
    });
    return sharedInstance;
}
-(instancetype)init{
    self = [super init];
    if (self) {
    }
    return self;
}
-(void)NotificationInitWithParams:(NSDictionary *)dict{
#if defined(__IPHONE_10_0) && (__IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_10_0)
            UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
            UNMutableNotificationContent *content_1 = [[UNMutableNotificationContent alloc]init];
            content_1.title = [NSString localizedUserNotificationStringForKey:[dict valueForKey:@"title"] arguments:nil];
            content_1.badge = [NSNumber numberWithInteger:1];
            content_1.body = [NSString localizedUserNotificationStringForKey:[dict valueForKey:@"content"] arguments:nil];
            content_1.sound = [UNNotificationSound defaultSound];
            content_1.userInfo = dict;
            content_1.badge = [NSNumber numberWithInteger:1];
            NSDateComponents *components = [[NSDateComponents alloc]init];
            NSArray *timeArr1 = [self timeToTimestamp1:dict[@"time"]];
            components.year = [timeArr1[0] integerValue];
            components.month = [timeArr1[1] integerValue];
            components.day = [timeArr1[2] integerValue];
            components.hour = [timeArr1[3] integerValue];
            components.minute = [timeArr1[4] integerValue];
            components.second = [timeArr1[5] integerValue];
            UNCalendarNotificationTrigger *trigger_1 = [UNCalendarNotificationTrigger triggerWithDateMatchingComponents:components repeats:NO];
            UNNotificationRequest *request_1 = [UNNotificationRequest requestWithIdentifier:dict[@"nid"] content:content_1 trigger:trigger_1];
            [center addNotificationRequest:request_1 withCompletionHandler:^(NSError * _Nullable error) {
                NSLog(@"error :%@",error);
            }];
#else
            UILocalNotification *localNotifi = [[UILocalNotification alloc] init];
            localNotifi.fireDate = [self timeToTimestamp:[dict valueForKey:@"time"]];
            localNotifi.alertBody = [dict valueForKey:@"content"];
            localNotifi.alertTitle = [dict valueForKey:@"title"];
            localNotifi.applicationIconBadgeNumber =1;
            localNotifi.userInfo = dict;
            localNotifi.timeZone = [NSTimeZone defaultTimeZone];
            UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge | UIUserNotificationTypeSound | UIUserNotificationTypeAlert categories:nil];
            [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
            [[UIApplication sharedApplication] scheduleLocalNotification:localNotifi];
#endif
}
-(void)removeAllNotification{
    [[UIApplication sharedApplication] cancelAllLocalNotifications];
}
-(void)removeNotificationWithParams:(NSDictionary *)dict{
    NSString *nid = [NSString stringWithFormat:@"%@",[dict valueForKey:@"nid"]];
#if defined(__IPHONE_10_0) && (__IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_10_0)
        UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
        [center     getPendingNotificationRequestsWithCompletionHandler:^(NSArray<UNNotificationRequest *> * _Nonnull requests) {
            for (UNNotificationRequest *localNoti in requests) {
                if ([[NSString stringWithFormat:@"%@",[localNoti.content.userInfo valueForKey:@"nid"]] isEqualToString:nid]) {
                    [center removeAllPendingNotificationRequests];
                }
            }
        }];
#else
        NSArray *notifiArray = [[UIApplication sharedApplication] scheduledLocalNotifications];
        for (UILocalNotification *localNoti in notifiArray) {
            if ([[NSString stringWithFormat:@"%@",[localNoti.userInfo valueForKey:@"nid"]] isEqualToString:nid]) {
                [[UIApplication sharedApplication] cancelLocalNotification:localNoti];
            }
        }
#endif
}
-(void)editNotificationWithParams:(NSDictionary *)dict{
    NSArray *notifiArray = [[UIApplication sharedApplication] scheduledLocalNotifications];
    NSString *nid = [NSString stringWithFormat:@"%@",[dict valueForKey:@"nid"]];
    for (UILocalNotification *localNoti in notifiArray) {
        if ([[NSString stringWithFormat:@"%@",[localNoti.userInfo valueForKey:@"nid"]] isEqualToString:nid] ) {
            localNoti.alertBody = [dict valueForKey:@"content"];
            localNoti.alertTitle = [dict valueForKey:@"title"];
            localNoti.fireDate = [self timeToTimestamp:[dict valueForKey:@"time"]];
            localNoti.userInfo = dict;
        }
    }
}
-(BOOL)hasNotificationWithParams:(NSDictionary *)dict{
    NSArray *notifiArray = [[UIApplication sharedApplication] scheduledLocalNotifications];
    NSString *nid = [NSString stringWithFormat:@"%@",[dict valueForKey:@"nid"]];
    for (UILocalNotification *localNoti in notifiArray) {
        if ([[NSString stringWithFormat:@"%@",[localNoti.userInfo valueForKey:@"nid"]] isEqualToString:nid] ) {
                return YES;
        }
    }
    return NO;
}
-(NSDate *)timeToTimestamp:(NSString *)timestamp{
    if (!timestamp) {
        return nil;
    }
    NSDateFormatter *dateFormatter=[[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"yyyy-MM-dd HH:mm"];
    NSDate *aTime = [NSDate dateWithTimeIntervalSince1970:[timestamp integerValue]];
    NSString *str=[dateFormatter stringFromDate:aTime];
    NSDate *date = [dateFormatter dateFromString:str];
    return date;
}
- (NSArray *)timeToTimestamp1:(NSString *)timestamp{
    if (!timestamp) {
        return nil;
    }
    NSDateFormatter *dateFormatter=[[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"yyyy-MM-dd HH:mm:ss"];
    NSDate *aTime = [NSDate dateWithTimeIntervalSince1970:[timestamp integerValue]];
    NSString *str=[dateFormatter stringFromDate:aTime];
    NSMutableArray *timesArr = [NSMutableArray array];
    NSRange yearRange = NSMakeRange(0, 4);
    NSInteger year = [[str substringWithRange:yearRange] integerValue];
    NSRange monthRange = NSMakeRange(5, 2);
    NSInteger month = [[str substringWithRange:monthRange] integerValue];
    NSRange dayRange = NSMakeRange(8, 2);
    NSInteger day = [[str substringWithRange:dayRange] integerValue];
    NSRange hourRange = NSMakeRange(11, 2);
    NSInteger hour = [[str substringWithRange:hourRange] integerValue];
    NSRange minRange = NSMakeRange(14, 2);
    NSInteger min = [[str substringWithRange:minRange] integerValue];
    NSRange secRange = NSMakeRange(17, 2);
    NSInteger  sec = [[str substringWithRange:secRange] integerValue];
    [timesArr addObject:[NSString stringWithFormat:@"%ld",(long)year]];
    [timesArr addObject:[NSString stringWithFormat:@"%ld",(long)month]];
    [timesArr addObject:[NSString stringWithFormat:@"%ld",(long)day]];
    [timesArr addObject:[NSString stringWithFormat:@"%ld",(long)hour]];
    [timesArr addObject:[NSString stringWithFormat:@"%ld",(long)min]];
    [timesArr addObject:[NSString stringWithFormat:@"%ld",(long)sec]];
    return timesArr;
}
@end
