@@ -10,6 +10,7 @@ Your private chat UI for OpenaAI/Azure APIs. Deploy anywhere, fill in API Key et
- **Token counter**: get number of tokens in the dialog and in the prompt being typed
  - Can be seen at the top right corner, counts dialog length + the number of tokens in the promnpt being typed
- **Azure and OpenAI**: Connect to OpenAI APIs either directly (via API key) or via models deployed in Microsoft Azure
- **Can be deployed as a single container:** no dependencies on Progress, all data is stored in local files and encrypted
- **Response srtreaming**: see how OpneAI is typing back
- **Model Customization**: Users can add, update, and delete AI models with custom settings in UI OR have a mode defined in ENV variables
- **Single and Multi user**: Anonymous authentication (single user) with not lock screen OR user authentication against a local user DBin a YAML file (pairs of usernames/password hashes).
@@ -27,17 +28,18 @@ You can configure the app either via setting environment variables or puttin val
| Environment Variable | Description | Default Value |
|----------------------|-------------|---------------|
| `OPENAI_API_KEY`     | The API key for OpenAI or Azure | None |
| `API_TYPE`           | The type of API to use (OpenAI, Azure, Fake) | None |
| `API_TYPE`           | The type of API to use (OpenAI, Azure, Fake, Empty) | Fake |
| `API_VERSION`        | The version of the API | None |
| `OPENAI_API_BASE`    | The base URL for the OpenAI API | None |
| `ALIAS`              | The alias for the model | None |
| `MODEL`              | The name of the model | None |
| `TEMPERATURE`        | The temperature setting for the AI model | 0.0 |
| `DATA_DIR`           | The directory where data will be stored | ".data" |
| `DISABLE_AUTH`       | Whether to disable user authentication | "False" |
| `DISBLE_USER_REG`     | Whether to disable user registration | "False" |

**Remarks, notes:**
- If `API_TYPE` is set to `Fake` all message will get a static reply, no call to API will be made. For demonstration purposes
- If `API_TYPE` is set to `Fake` all message will get a static reply, no call to API will be made. For demonstration purposes. If `Empty` is provided than no model is expected in the environment variables
- Providing  Azure/OpenAI model credentials (API key, deployment URL, etc.) via environment variables is not the only option. Users can also add their credentials in the Web UI, those creds will be encrypted and stored in `models.dat` file
- `DATA_DIR` - that's where all conversations and model settings will be saved. Each user will have a `$username` subfolder.
- `DISABLE_AUTH` - if set to [True], no login page will be shown, and all data will be stored under `$DATA_DIR/default_user`.