=======================
Cobertura Report Merger
=======================

Cobertura Report Merger is an app to merge cobertura coverage reports for django.

Quick start
-----------

1. Add "cobertura_report_merger" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'cobertura_report_merger',
    ]

2. Run `python manage.py merge_coverage_files <coveragefile1_name> <coveragefile2_name>` to merge the reports.


Testing
-------

In order to run tests, you need to run `pip install django mock pytest` and then
`py.test` from the `django-cobertura-report-merger` directory
