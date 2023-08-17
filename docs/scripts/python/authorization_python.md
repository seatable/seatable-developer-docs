# Authorization

You can use two methods to obtain authorization to read and write a base. One way is to use the api token of the base, the token can be directly generated on the web side. Read directly from context.api_token in the cloud environment.

Another method is to use the account name and password to initialize an Account object, and then call the Account interface to get a base object. The first method is more secure.