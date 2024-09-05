#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2024/9/5
import allure

from oa_api_test.oa_api.reduce_func import reduce


class TestFunc:

    @allure.feature("测试减法")
    def test_reduce_func(self):
        assert 3 == reduce(7, 4)