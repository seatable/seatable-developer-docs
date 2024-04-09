# # UpdateGeneralSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_title** | **string** | The title of your SeaTable web interface, like appeared on the browser tab. Optional. Default value is &#x60;SeaTable Private&#x60;. | [optional]
**site_name** | **string** | The name of your site, like appeared in the notification emails. Optional. Default value is &#x60;SeaTable&#x60;. | [optional]
**enable_branding_css** | **int** | If a custom CSS should be used. Optional, &#x60;0&#x60; by default. If set to &#x60;1&#x60;, paste your CSS into the param &#x60;CUSTOM_CSS&#x60;. | [optional]
**custom_css** | **string** | The content of your custom CSS. Optional. Empty by default. | [optional]
**activate_after_registration** | **int** | If users should be automatically activated after the registration. Optional, &#x60;1&#x60; by default. If &#x60;0&#x60;, then the user need to be activated by the administrator or via the activation email. | [optional]
**registration_send_mail** | **int** | If an activation email should be sent after the user has registered. Optional, &#x60;0&#x60; by default. | [optional]
**login_remember_days** | **int** | How many default days a user could be kept signed in. Optional, &#x60;7&#x60; by default. | [optional]
**login_attempt_limit** | **int** | The maximum number of failed login attempts before showing CAPTCHA. Optional, &#x60;5&#x60; by default. | [optional]
**freeze_user_on_login_failed** | **int** | If the user&#39;s account should be frozen when they exceed the login attempts limit. Optional, &#x60;0&#x60; by default. | [optional]
**user_strong_password_required** | **int** | Force the users to use a strong password when signing up or changing password. Optional, &#x60;0&#x60; by default. | [optional]
**force_password_change** | **int** | Force newly added users to change their password, or when the admin resets their password. Optional, &#x60;1&#x60; by default. | [optional]
**user_password_min_length** | **int** | The minimum length of user passwords. Optional, &#x60;6&#x60; by default. | [optional]
**user_password_strength_level** | **int** | The level (&#x60;1&#x60;-&#x60;4&#x60;) of a password&#39;s strength. For example, &#x60;3&#x60; means password must have at least 3 of the following: a number, an upper letter, a lower letter and a special symbol. Optional, &#x60;3&#x60; by default. | [optional]
**enable_two_factor_auth** | **int** | If two factor authentication should be activated for the system. Optional, &#x60;0&#x60; by default. | [optional]
**enable_signup** | **int** | If registration on the web interface is allowed. Optional, &#x60;0&#x60; by default. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
