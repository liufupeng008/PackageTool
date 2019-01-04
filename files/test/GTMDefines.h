#import <UIKit/UIKit.h>
#import "BaseView.h"
#import "PrimeLoginViewModel.h"
typedef NS_ENUM(NSInteger,ClickType) {
    ClickTypeLogin = 0,
    ClickTypeFindBack,
    ClickTypeBackButtonOnclick
};
@protocol FMCEmailLoginViewDelegate <NSObject>
@optional
- (void)FMCEmailLoginViewGetActionType:(ClickType)type  andTheView:(UIView *)theHost;
@end
@interface FMCEmailLoginView : BaseView
@property (nonatomic,weak) id<FMCEmailLoginViewDelegate>delegate;
@property(nonatomic,strong)id userInfo;
@end