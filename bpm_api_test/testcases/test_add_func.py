#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2024/9/5
import allure

from bpm_api_test.bpm_api.func_add import add


class TestFunc:

    @allure.feature('测试加法')
    def test_add_func(self):
        assert 3 == add(1, 2)
