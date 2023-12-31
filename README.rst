.. raw:: html

   <!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->

|Pre-commit Status| |Build Status| |codecov|

.. raw:: html

   <!-- /!\ do not modify above this line -->

Patient Medical Files
=====================

Patient files, mdn nomenclature, selling of medical devices …

.. raw:: html

   <!-- /!\ do not modify below this line -->

.. raw:: html

   <!-- prettier-ignore-start -->

Available addons
----------------

+-----------------+-----------------+-----------------+-----------------+
| addon           | version         | maintainers     | summary         |
+=================+=================+=================+=================+
| `hospital       | 16.0.1.0.0      |                 | Patient data    |
|  <hospital/>`__ |                 |                 | and used        |
|                 |                 |                 | medical         |
|                 |                 |                 | devices.        |
+-----------------+-----------------+-----------------+-----------------+
| `hospital_      | 16.0.1.0.0      |                 | Add rure for    |
| loyalty <hospit |                 |                 | doctor loyalty  |
| al_loyalty/>`__ |                 |                 | program         |
+-----------------+-----------------+-----------------+-----------------+
| `produc         | 16.0.1.0.0      |                 | Added support   |
| t_properties_md |                 |                 | for medical     |
| n <product_prop |                 |                 | device          |
| erties_mdn/>`__ |                 |                 | nomenclature    |
|                 |                 |                 | base on product |
|                 |                 |                 | properties      |
|                 |                 |                 | module          |
+-----------------+-----------------+-----------------+-----------------+
| `product        | 16.0.1.0.0      |                 | Add mdn data in |
| _set_mdn <produ |                 |                 | product set     |
| ct_set_mdn/>`__ |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. raw:: html

   <!-- prettier-ignore-end -->

Licenses
--------

This repository is licensed under `AGPL-3.0 <LICENSE>`__.

However, each module can have a totally different license, as long as
they adhere to Odoo Community Association (OCA) policy. Consult each
module’s ``__manifest__.py`` file, which contains a ``license`` key that
explains its license.

--------------

.. raw:: html

   <!-- /!\ Non OCA Context : Set here the full description of your organization. -->

.. |Pre-commit Status| image:: https://github.com/rosenvladimirov/medical/actions/workflows/pre-commit.yml/badge.svg?branch=16.0
   :target: https://github.com/rosenvladimirov/medical/actions/workflows/pre-commit.yml?query=branch%3A16.0
.. |Build Status| image:: https://github.com/rosenvladimirov/medical/actions/workflows/test.yml/badge.svg?branch=16.0
   :target: https://github.com/rosenvladimirov/medical/actions/workflows/test.yml?query=branch%3A16.0
.. |codecov| image:: https://codecov.io/gh/rosenvladimirov/medical/branch/16.0/graph/badge.svg
   :target: https://codecov.io/gh/rosenvladimirov/medical
