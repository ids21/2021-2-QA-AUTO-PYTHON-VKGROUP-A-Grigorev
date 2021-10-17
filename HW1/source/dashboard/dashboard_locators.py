class DashboardLocators:
    USER_PROFILE = "//div[contains(@class,'right-module-rightButton')]"
    FIELD_LOG_OFF = (
        "(//li[contains(@class,'rightMenu-module-rightMenuItem')]/a)[last()]"
    )
    MODULE_SEGMENTS = "//a[contains(@class,'center-module-segments')]"
    MODULE_BILLINGS = "//a[contains(@class,'center-module-billing')]"
    MODULE_STATISTICS = "//a[contains(@class,'center-module-statistics')]"
    MODULE_PROFILE = "//a[contains(@class,'center-module-profile')]"
    
class BillingLocator:
    TABLE_DEPOSIT = "//div[contains(@class,'billing-page__deposit')]"

class ProfileLocators:
    INPUT_FIO = "//div[@data-name='fio']//input"
    BUTTON_SAVE = "//button[contains(@class,'button_submit')]"
