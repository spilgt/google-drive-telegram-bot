class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**你好呀 {}.**\n__我是Google云端硬盘上载程序Bot.您可以使用我从直接链接或电报文件将任何文件/视频上传到Google云端硬盘.__\n__您可以从/ help中了解更多信息. /help.__"

    HELP_MSG = [
        ".",
        "**Google云端硬盘上传器**\n__我可以将文件从直接链接或电报文件上传到您的Google云端硬盘.我需要做的就是对我的Google云端硬盘帐户进行身份验证.然后发送直接下载链接或电报文件.__\n\n我具有更多功能...想知道吗?只需遍历本教程并仔细阅读消息即可.",
        
        f"**验证Google云端硬盘**\n__发送 /{BotCommands.Authorize[0]} 注意,您将收到一个URL,访问URL并按照步骤操作,并在此处发送收到的代码.使用 /{BotCommands.Revoke[0]} 撤销您当前登录的Google云端硬盘帐户.__\n\n**请注意: 在您授权我之前,不会听任何命令或消息 (except /{BotCommands.Authorize[0]} command) 授权命令除外.\n所以, 授权是强制性的 !**",
        
        f"**下载链接**\n__向我发送文件的直接下载链接,我会将其下载到我的服务器上,并将其上传到您的Google Drive帐户. 您可以在上传文件到GDrive帐户之前重命名文件. 只需将URL发送给我和分隔符 ' | '.__\n\n**__例如:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | 新的文件名.mkv```\n\n**Telegram 文件**\n__要在您的Google云端硬盘帐户中上传电报文件,只需将文件发送给我,我就会下载并将其上传到您的Google云端硬盘帐户.. 注意：电报文件下载速度较慢，大文件可能需要更长的时间。.__\n\n**YouTube-DL 支持**\n__下载YouTube文件使用youtube-dl.\nUse /{BotCommands.YtDl[0]} (YouTube 链接/YouTube-DL Supported site link)__",
        
        f"**要上传的自定义文件夹**\n__要在自定义文件夹或者在__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) 来设置自定义上传文件夹.\n所有文件上传到该文件夹中.__",
        
        f"**删除Google云端硬盘文件**\n__删除谷歌驱动器文件。使用 /{BotCommands.Delete[0]} (文件/文件夹URL) 删除文件或回复 /{BotCommands.Delete[0]} to bot message.\nYou can also empty trash files use /{BotCommands.EmptyTrash[0]}\nNote: Files are deleted permanently. This process cannot be undone.\n\n**Copy Google Drive Files**\n__Yes, Clone or Copy Google Drive Files.\n__Use /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.__",
        
        "**Rules & Precautions**\n__1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links @transload it first.\n4. Don't misuse, overload or abuse this free service.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @viperadnan**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **超过限速.**\n__24小时后超出用户速率限制.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **找不到文件/文件夹.**\n__File id - {} 未找到。 确保它是 存在并且可以由登录的帐户访问.__"
    
    INVALID_GDRIVE_URL = "❗ **无效的Google云端硬盘网址**\n确保Google云端硬盘网址的格式正确."
    
    COPIED_SUCCESSFULLY = "✅ **复制成功.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **您尚未认证我可以上传到任何帐户.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **上传文件中...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **上传成功.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**下载失败**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **下载文件...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **已授权您的Google云端硬盘帐户.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"❗ **无效的代码**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **成功授权Google云端硬盘帐户.**'
    
    INVALID_AUTH_CODE = '❗ **无效的代码**\n__您发送的代码无效或之前已经使用过。通过授权URL生成新的__'
    
    AUTH_TEXT = "⛓️ **要授权您的Google云端硬盘帐户，请访问此 [URL]({}) 并在此处发送生成的代码.**\n__访问URL>允许权限>您将获得一个代码>复制它>在此处发送__"
    
    DOWNLOAD_TG_FILE = "📥 **下载文件...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **自定义文件夹链接设置成功.**\n__您的自定义文件夹ID - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **自定义文件夹ID已成功清除.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **您当前的自定义文件夹ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
