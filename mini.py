#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 mini.py
Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.
Version: 1.0.0
TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com
Created: 2017/12/31
Device: MacBook Pro (Retina, 13-inch, Mid 2015)
OS: macOS Serria version 10.12.6
IDE: PyCharm Community Edition 2017.2.4
Python: 3.6.1
"""

# --- References ---
# --- notes ---
# --- Information ---
# --- Circumstances ---

# === import ===========================================================================================================

""" Standard library """
""" Third party library """
""" Local library """

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================

# ======================================================================================================================


class ReadEnteredTextStandAloneImpl:
    """ If user display_input, drop filesPath then return files, exit then return None """
    # -- variables --
    __display_input_text = '> '
    __display_output_text = '>> Read: '

    # reader = ReadEnteredTextStandAloneImpl()
    # while True:
    #     print()
    #     print('Enter the characters...')
    #     text = reader.read()
    #     if text is None:
    #         # exit
    #         break

    def read(self) -> str or None:
        entered_str = input(self.__display_input_text)
        if self.__decision_exit(entered_str):
            # if user display_inputs exit meaning then exit
            return None
        else:
            print('{0}{1}'.format(self.__display_output_text, entered_str))
            return entered_str

    def __decision_exit(self, text) -> bool:
        # -- constants --
        EXIT_TEXTS = ['e', '-e', 'exit', 'exit()', 'Exit', 'Exit()']
        # decision match strings argument and EXIT_TEXTS
        for exit_text in EXIT_TEXTS:
            if text == exit_text:
                return True
        return False


# ======================================================================================================================

class JumboMini:
    def drawing(self, text: str) -> int:
        num = int(text)
        Mini50000000 = [52117905, 48151439, 29162080, 5186502, 38182778, 24133131, 85154734]
        for n in Mini50000000:
            # 5000万円
            if num == n:
                print('1等: 5000万円当選 - {0}'.format(text))
                return 50000000
            # 1000万円
            if (num == n + 1) or (num == n - 1):
                print('前後賞: 1000万円当選 - {0}'.format(text))
                return 10000000
        Mini10000000 = 129592
        # 1000万円
        if (num - Mini10000000) % 10000000 == 0:
            print('2等: 1000万円当選 - {0}'.format(text))
            return 10000000
        Mini1000000 = 147945
        # 100万円
        if (num - Mini1000000) % 1000000 == 0:
            print('3等: 100万円当選 - {0}'.format(text))
            return 1000000
        Mini100000 = 3741
        # 10万円
        if (num - Mini100000) % 10000 == 0:
            print('4等: 10万円当選 - {0}'.format(text))
            return 100000
        Mini10000 = 527
        # 1万円
        if (num - Mini10000) % 1000 == 0:
            print('5等: 1万円当選 - {0}'.format(text))
            return 10000
        Mini3000 = 87
        # 3000円
        if (num - Mini3000) % 100 == 0:
            print('6等: 3000円当選 - {0}'.format(text))
            return 3000
        Mini300 = 2
        # 300円
        if (num - Mini300) % 10 == 0:
            print('7等: 300円当選 - {0}'.format(text))
            return 300
        # はずれ
        print('はずれ - {0}'.format(text))
        return 0


# ======================================================================================================================


class Main:
    print('mini.py')
    print(' - 第732回 年末ジャンボミニ 2017年12月31日')
    print(' - 抽選番号参照: http://www.hpfree.com/engeki/shinohara19.html')
    print('(本プログラム使用を持ちまして，使用者は本プログラム使用による損害等に製作者は一切の責任を負わないことについて同意したものとします。)')
    money = 0
    reader = ReadEnteredTextStandAloneImpl()
    lottery = JumboMini()
    while True:
        print()
        print('組と番号をひと続きで8桁入力')
        text = reader.read()
        if text is None:
            # exit
            break
        else:
            if len(text) != 8:
                print('入力桁が誤っています。もう一度入力してください。')
            else:
                money += lottery.drawing(text)


# ======================================================================================================================


if __name__ == '__main__':
    main = Main()
