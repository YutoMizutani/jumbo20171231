#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 jumbo.py
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

class Jumbo:
    def drawing(self, text: str) -> int:
        num = int(text)
        Jumbo700000000 = 165186859
        # 7億円
        if num == Jumbo700000000:
            print('1等: 7億円当選 - {0}'.format(text))
            return 700000000
        # 1.5億円
        if (num == Jumbo700000000 + 1) or (num == Jumbo700000000 - 1):
            print('前後賞: 1.5億円当選 - {0}'.format(text))
            return 150000000
        # 30万円
        if (num - (Jumbo700000000 % 1000000)) % 1000000 == 0:
            print('組違い賞: 30万円当選 - {0}'.format(text))
            return 300000
        Jumbo10000000 = 4133153
        # 1000万円
        if (num - Jumbo10000000) % 10000000 == 0:
            print('2等: 1000万円当選 - {0}'.format(text))
            return 10000000
        Jumbo1000000 = 194314
        # 100万円
        if (num - Jumbo1000000) % 1000000 == 0:
            print('3等: 100万円当選 - {0}'.format(text))
            return 1000000
        Jumbo100000 = [184793, 152618, 144606, 145961, 100987, 188864, 193880]
        for n in Jumbo100000:
            # 10万円
            if (num - n) % 10000 == 0:
                print('4等: 10万円当選 - {0}'.format(text))
                return 100000
        Jumbo10000 = 973
        # 1万円
        if (num - Jumbo10000) % 1000 == 0:
            print('5等: 1万円当選 - {0}'.format(text))
            return 10000
        Jumbo3000 = 57
        # 3000円
        if (num - Jumbo3000) % 100 == 0:
            print('6等: 3000円当選 - {0}'.format(text))
            return 3000
        Jumbo300 = 5
        # 300円
        if (num - Jumbo300) % 10 == 0:
            print('7等: 300円当選 - {0}'.format(text))
            return 300
        # はずれ
        print('はずれ - {0}'.format(text))
        return 0


# ======================================================================================================================


class Main:
    print('jumbo.py')
    print(' - 第731回 年末ジャンボ 2017年12月31日')
    print(' - 抽選番号参照: http://www.hpfree.com/engeki/')
    print('(本プログラム使用を持ちまして，使用者は本プログラム使用による損害等に製作者は一切の責任を負わないことについて同意したものとします。)')
    num = 0
    money = 0
    reader = ReadEnteredTextStandAloneImpl()
    lottery = Jumbo()
    while True:
        print()
        print('{0}枚，合計当選金額: {1}'.format(num, money))
        print('組と番号をひと続きで9または8桁入力')
        text = reader.read()
        if text is None:
            # exit
            break
        else:
            if len(text) < 8:
                print('入力桁が誤っています。もう一度入力してください。')
            else:
                num += 1
                money += lottery.drawing(text)


# ======================================================================================================================


if __name__ == '__main__':
    main = Main()
