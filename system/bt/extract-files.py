#!/usr/bin/env -S PYTHONPATH=../../:../../../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-FileCopyrightText: Paranoid Android
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import blob_fixup, blob_fixups_user_type
from extract_utils.main import ExtractUtils

from extract_utils_qti.module import ExtractUtilsQTIModule, QTIComponentType

blob_fixups: blob_fixups_user_type = {
    'system_ext/app/aptxacu/aptxacu.apk': blob_fixup()
        .apktool_patch('blob-patches/aptxacu', sdk_framework=True),
}  # fmt: skip

module = ExtractUtilsQTIModule(
    'bt',
    QTIComponentType.SYSTEM,
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
