@@ -47,8 +47,8 @@ def model_or_deployment_name(self):

    @model_or_deployment_name.setter
    def model_or_deployment_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected model_or_deployment_name to be a string")
        if not isinstance(value, (str, type(None))):
            raise TypeError("Expected model_or_deployment_name to be a string or None")
        self._model_or_deployment_name = value

    @property
@@ -57,8 +57,8 @@ def api_key(self):

    @api_key.setter
    def api_key(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected api_key to be a string")
        if not isinstance(value, (str, type(None))):
            raise TypeError("Expected api_key to be a string or None")
        self._api_key = value

    @property
@@ -372,7 +372,7 @@ def escape_username(username: str) -> str:
    encryption_key = enc_key
    model_repository = ModelRepository()
    model_repository.load()
    if env_vars.env_model_alias:
    if env_vars.env_model_alias and env_vars.env_api_type != env_vars.ApiTypeOptions.EMPTY:
        model_repository.add_env(env_vars.env_model_alias, env_vars.env_model_name, env_vars.env_api_key,
                                 env_vars.env_api_type, env_vars.env_api_version,
                                 env_vars.env_api_base, env_vars.env_temperature)
