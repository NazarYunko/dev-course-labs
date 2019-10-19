#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import unittest
from app import *


class TestClass(unittest.TestCase):
    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'
	self.pm_time = '22:22:22 PM'
	self.am_time = '10:22:12 AM'
	self.wrong_time = 'asdasdfsdjdskfjijagerfsf'

    def test_date_work_successfully(self):
        # Перевіряєм чи функція відправювала до кінця і повернулі True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряєм чи у функцію не було передано жодної URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана направильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work(self):
        self.assertTrue(home_work(self.pm_time) == True)
	self.assertTrue(home_work(self.am_time) == True)
	self.assertTrue(home_work(self.wrong_time) == False)
