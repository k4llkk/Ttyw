@l313l.ar_cmd(
    pattern="رفع مشرف(?:\s|$)([\s\S]*)",
    command=("رفع مشرف", plugin_category),
    info={
        "الامر": "᯽︙ لرفع الشخص مشرف مع صلاحيات",
        "الشرح": "᯽︙ لرفع الشخص مشرف بالمجموعه قم بالرد على الشخص\
            \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر",
        "الاستخدام": [
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه>",
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه> ",
        ],
    },
    groups_only=True,
    require_admin=True,
)#admin plugin for  l313l
async def promote(event):
    "᯽︙ لـرفع مستـخدم مشـرف في الـكروب"
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "Admin"
    if not user:
        return
    catevent = await edit_or_reply(event, "**يـتم الرفـع**")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await catevent.edit(NO_PERM)
    await catevent.edit("**تم رفعه مشرف بالمجموعه بنجاح ✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الـرفـع\
            \nالـمستخـدم: [{user.first_name}](tg://user?id={user.id})\
            \nالـدردشـة: {event.chat.title} (`{event.chat_id}`)",
        )


@l313l.ar_cmd(
    pattern="تنزيل الكل(?:\s|$)([\s\S]*)",
    command=("تنزيل الكل", plugin_category),
    info={
        "الامر": "᯽︙ لتنزيل الشخص كن الاشراف",
        "الشرح": "᯽︙ يقوم هذا الامر بحذف جميع صلاحيات المشرف\
            \n᯽︙ ملاحظه :**لازم تكون انت الشخص الي رفعه او تكون مالك المجموعه حتى تنزله**",
        "الاستخدام": [
            "{tr}تك <الايدي/المعرف/بالرد عليه>",
            "{tr}تك <الايدي/المعرف/بالرد عليه>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def demote(event):
    "᯽︙ لـتنزيـل شـخص من الأشـراف"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    catevent = await edit_or_reply(event, "**᯽︙ يـتم التنزيل من الاشراف**")
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    rank = "admin"
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        return await catevent.edit(NO_PERM)
    await catevent.edit("**᯽︙ تـم تنزيله من قائمه الادمنيه بنجاح ✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#تنزيل_مشرف\
            \nالمعرف: [{user.first_name}](tg://user?id={user.id})\
            \nالدردشه: {event.chat.title}(`{event.chat_id}`)",
        )
@l313l.ar_cmd(
    pattern="طرد(?:\s|$)([\s\S]*)",
    command=("طرد", plugin_category),
    info={
        "᯽︙ الأسـتخدام": "لـطرد شـخض من الـكروب",
        "᯽︙ الشـرح": "لـطرد شخص من المـجموعة يستطيع الأنضـمام مرة اخـرى.\
        \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر.",
        "᯽︙ الأمـر": [
            "{tr}طرد <الايدي/المعرف/بالرد عليه>",
            "{tr}طرد <الايدي/المعرف/بالرد عليه> <السبب> ",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def endmute(event):
    "لـطرد شـخض من الـكروب"
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id == 705475246:
        return await edit_delete(event, "**- لا يمڪنني حظر مطـوري دي لك**")
    catevent = await edit_or_reply(event, "᯽︙ يـتم طـرد الـمستخدم أنتـظر")
    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except Exception as e:
        return await catevent.edit(NO_PERM + f"\n{str(e)}")
    if reason:
        await catevent.edit(
            f"᯽︙ الـمستخدم [{user.first_name}](tg://user?id={user.id})\n ᯽︙ تـم طرده بنجاح ✅ \n᯽︙ السـبب : {reason}"
        )
    else:
        await catevent.edit(f"᯽︙ الـمستخدم [{user.first_name}](tg://user?id={user.id})\n ᯽︙ تـم طرده بنجاح ✅ ")
@l313l.ar_cmd(
    pattern="حظر(?:\s|$)([\s\S]*)",
    command=("حظر", plugin_category),
    info={
        "᯽︙ الاستخدام": "يقـوم بـحظر شخـص في الـكروب الذي تـم اسـتخدام الأمر فيـه.",
        "᯽︙ الشرح": "لحـظر شخـص من الكـروب ومـنعه من الأنـضمام مجـددا. تـحتاج الصلاحـيات لـهذا الأمـر.",
        "᯽︙ الامر": [
            "{tr}حظر <الايدي/المعرف/بالرد عليه>",
            "{tr}حظر <الايدي/المعرف/بالرد عليه> <السبب>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def jokerban(event):
    "᯽︙ لحـظر شخص في كـروب مـعين"
    await event.delete()
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id == 705475246:
        return await edit_delete(event, "**- لا يمڪنني حظر مطـوري دي لك**")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await edit_or_reply(event, NO_PERM)
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await edit_or_reply(event, "᯽︙ ليـس لـدي جـميع الصـلاحيـات لكـن سيـبقى محـظور")
    if reason:
        await event.client.send_file(
            event.chat_id,
            joker_ban,
            caption=f"᯽︙ المسـتخدم {_format.mentionuser(user.first_name, user.id)} \n ᯽︙ تـم حـظره بنـجاح !!\n**⌔︙السبب : **`{reason}`"
        )
    else:
        await event.client.send_file(
            event.chat_id,
            joker_ban,
            caption=f"᯽︙ المسـتخدم {_format.mentionuser(user.first_name, user.id)} \n ᯽︙ تـم حـظره بنـجاح ✅"
        )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"᯽︙ الحـظر\
                \nالمسـتخدم: [{user.first_name}](tg://user?id={user.id})\
                \nالـدردشـة: {event.chat.title}\
                \nايدي الكروب(`{event.chat_id}`)\
                \nالسبـب : {reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"᯽︙ الحـظر\
                \nالمسـتخدم: [{user.first_name}](tg://user?id={user.id})\
                \nالـدردشـة: {event.chat.title}\
                \n ايـدي الكـروب: (`{event.chat_id}`)",
            )


@l313l.ar_cmd(
    pattern="الغاء حظر(?:\s|$)([\s\S]*)",
    command=("الغاء حظر", plugin_category),
    info={
        "᯽︙ الأسـتخدام": "يقـوم بـالغاء حـظر الشـخص في الـكروب الذي اسـتخدمت فيـه الامر.",
        "᯽︙ الشرح": "لألـغاء حـظر شخـص من الكـروب والسـماح له من الأنـضمام مجـددا\
            \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر.",
        "᯽︙ الأمـر": [
            "{tr}الغاء حظر <الايدي/المعرف/بالرد عليه>",
            "{tr}الغاء حظر <الايدي/المعرف/بالرد عليه> <السبب> ",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def nothanos(event):
    "᯽︙ لألـغاء الـحظر لـشخص في كـروب مـعين"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    catevent = await edit_or_reply(event, "᯽︙ جـار الـغاء الـحظر أنتـظر رجـاءا")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await catevent.edit(
            f"᯽︙ الـمستخدم {_format.mentionuser(user.first_name ,user.id)}\n ᯽︙ تـم الـغاء حـظره بنـجاح "
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "᯽︙ الـغاء الـحظر \n"
                f"الـمستخدم: [{user.first_name}](tg://user?id={user.id})\n"
                f"الـدردشـة: {event.chat.title}(`{event.chat_id}`)",
            )
    except UserIdInvalidError:
        await catevent.edit("᯽︙ يـبدو أن هذه الـعمليـة تم إلغاؤهـا")
    except Exception as e:
        await catevent.edit(f"**خـطأ :**\n`{e}`")


@l313l.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))
