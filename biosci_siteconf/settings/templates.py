import os

settings_root = os.path.normpath(os.path.dirname(__file__))
site_package_root = os.path.split(settings_root)[0]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(site_package_root, "templates").replace("\\", "/")],
        #         'APP_DIRS': True,  # not needed when specifying app_directories Loader
        "OPTIONS": {
            "context_processors": [
                # Default::
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                # Custom adds::
                "django.template.context_processors.request",
                "swingtime.context_processors.current_datetime",
                "graduate_students.context_processors.upcoming_graduates",
                "shouts.context_processors.all_shouts",
                "uofm.context_processors.unitbranding",
            ],
            "loaders": [
                # DO NOT specified the cached.Loader -- this is done later.
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    }
]
