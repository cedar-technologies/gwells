# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-07 17:58
from __future__ import unicode_literals

from django.db import migrations
from django.core.management.sql import emit_post_migrate_signal

GWELLS_ADMIN = 'gwells_admin'
REGISTRIES_ADJUDICATOR = 'registries_adjudicator'
REGISTRIES_STATUTORY_AUTHORITY = 'registries_statutory_authority'
REGISTRIES_VIEWER = 'registries_viewer'
WELLS_VIEWER = 'wells_viewer'
WELLS_EDIT = 'wells_edit'

KEYCLOAK_ROLE = [GWELLS_ADMIN, REGISTRIES_ADJUDICATOR, REGISTRIES_STATUTORY_AUTHORITY,
                 REGISTRIES_VIEWER, WELLS_VIEWER, WELLS_EDIT]


def revert_groups(apps, schema_editor):
    # We leave everything as is!
    pass


def update_groups(apps, schema_editor):
    # Prior to loading permissions, we need to ensure that the post_migrate has run. There is a post_migrate
    # task that populates ther required permissions.
    db_alias = schema_editor.connection.alias
    emit_post_migrate_signal(2, False, 'default')

    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Default permissions for registry (Adjudicator and Statutory Authority roles)
    REGISTRY_PERMISSIONS = [x for x in
                            Permission.objects.filter(codename__in=['add_person',
                                                                    'change_person',
                                                                    'delete_person',
                                                                    'add_organization',
                                                                    'change_organization',
                                                                    'delete_organization',
                                                                    'add_registriesapplication',
                                                                    'change_registriesapplication',
                                                                    'delete_registriesapplication',
                                                                    'add_register',
                                                                    'change_register',
                                                                    'delete_register',
                                                                    'add_personnote',
                                                                    'change_personnote',
                                                                    'delete_personnote',
                                                                    'add_organizationnote',
                                                                    'change_organizationnote',
                                                                    'delete_organizationnote',
                                                                    'add_activitysubmission',
                                                                    'change_activitysubmission',
                                                                    'delete_activitysubmission', ])
                            ]

    # Default permissions for well editors
    WELLS_EDIT_PERMISSIONS = [x for x in
                              Permission.objects.filter(codename__in=['add_activitysubmission',
                                                                      'change_activitysubmission',
                                                                      'delete_activitysubmission', ])
                              ]

    # Create the role->permission lookup that we're going to iterate through and re-produce in Django.
    ROLE_PERMISSION_MAP = {
        GWELLS_ADMIN: REGISTRY_PERMISSIONS + WELLS_EDIT_PERMISSIONS,
        REGISTRIES_ADJUDICATOR: REGISTRY_PERMISSIONS,
        REGISTRIES_STATUTORY_AUTHORITY: REGISTRY_PERMISSIONS,
        REGISTRIES_VIEWER: [],
        WELLS_VIEWER: [],
        WELLS_EDIT: WELLS_EDIT_PERMISSIONS
    }

    # We create a group corresponding to each keycloak role
    for role in KEYCLOAK_ROLE:
        group, created = Group.objects.get_or_create(name=role)
        group.permissions.set(ROLE_PERMISSION_MAP.get(role))


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0007_auto_20180726_1909'),
    ]

    operations = [
        migrations.RunPython(update_groups, revert_groups),
    ]
