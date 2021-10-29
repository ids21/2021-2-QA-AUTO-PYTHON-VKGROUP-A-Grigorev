class DashboardLocators:
    USER_PROFILE = "//div[contains(@class,'right-module-rightButton')]"
    FIELD_LOG_OFF = (
        "//a[contains(@href,'logout')]"
    )
    MODULE_SEGMENTS = "//a[contains(@class,'center-module-segments')]"
    MODULE_BILLINGS = "//a[contains(@class,'center-module-billing')]"
    MODULE_STATISTICS = "//a[contains(@class,'center-module-statistics')]"
    MODULE_PROFILE = "//a[contains(@class,'center-module-profile')]"
    MODULE_CAMPAIGN = "//a[contains(@class,'center-module-campaigns')]"
    MODULE_AUDIENCE = "//a[contains(@class,'center-module-segments')]"
    
class BillingLocator:
    TABLE_DEPOSIT = "//div[contains(@class,'billing-page__deposit')]"

class ProfileLocators:
    INPUT_FIO = "//div[@data-name='fio']//input"
    BUTTON_SAVE = "//button[contains(@class,'button_submit')]"

class CampaignLocator:
    BUTTON_CREATE = "//a[contains(@href,'campaign/new')]"
    INPUT_LINK = "//input[contains(@class,'mainUrl-module')]"
    FIELD_BANNER = "//span[text()='Images']/ancestor::div[contains(@id,'patterns_banner')]"
    INPUT_IMAGE = "//input[@data-test='image_240x400']"
    DATE_TO = "//div[contains(@class,'date-to')]//input"
    DATE_FROM = "//div[contains(@class,'date-from')]//input"
    BUDGET_PER_DAY = "//input[@data-test='budget-per_day']"
    BUDGET_TOTAL = "//input[@data-test='budget-total']"
    LABEL_BUDGET = "//label[@class='budget-setting__item-label']"
    BUTTON_CREATE = "//div[contains(@class,'save')]//button[@class='button button_submit']"
    RECORD_CAMPAIGN = "//div[contains(@class,'campaignNameCell')]"
    SELECT_RECORD = "//div[contains(@class,'campaignNameCell')]//input"
    DROP_ACTIONS = "//div[contains(@class,'tableControls-module')]//div[contains(@class,'select-module-arrow')]"
    DELETE_RECORD = "//li[@Title='Delete']"
    REFRESH_TABLE = "//div[@class='icon-refresh']"
    DROP_VIEW_RECORDS = "//div[contains(@class,'statusFilter-module')]//div[contains(@class,'select-module-arrow')]"
    VIEW_RECORDS_DELETED = "//li[@Title='Deleted campaigns']"
    ACTIVE_RECORDS = "//li[@Title='Active campaigns']"
    BUTTON_CREATE_CAMPAIGN  = "//div[contains(@class,'createButton')]"
    DELETED_STATUS = "//span[contains(@class,'translation-module-deleted')]"
    REACH_BUTTON = "//div[contains(@class,'column-list-item _reach')]"
    FIELD_UPLOAD_IMAGE = "//div[contains(@class,'module-uploadButton')]"
    BUDGET_BLOCK = "//div[@class='budget-setting']"

class AudienceLocator:
    CREATE_SEGMENT = "//a[contains(@href,'segments/segments_list/new')]"
    CREATE_SEGMENT_BUTTON = "//div[contains(@class,'create-button')]/button"
    CHECK_BOX = "//input[contains(@class,'adding-segments-source')]"
    BUTTON_ADD = "//div[contains(@class,'add-button')]/button"
    BUTTON_SUBMIT_CREATE = "//div[contains(@class,'create-segment')]/button"
    FIELD_REMOVE = "//div[contains(@data-test,'remove')]"
    CONFIRM_DELETE = "//button[contains(@class,'button_confirm-remove')]"
    RECORD_SEGEMTS = "//div[@role='rowgroup']//div[contains(@class,'cells')]"
