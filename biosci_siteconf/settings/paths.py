import os

settings_root = os.path.normpath(os.path.dirname(__file__))
site_package_root = os.path.split(settings_root)[0]
bundle_root = os.path.split(site_package_root)[0]
storage_root = os.path.join(bundle_root, "__storage")
