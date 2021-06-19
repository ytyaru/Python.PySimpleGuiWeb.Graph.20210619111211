#!/usr/bin/env python3
# coding: utf8
import PySimpleGUIWeb as sg
print(dir(sg))
print(sg.theme_list())

sg.theme('DarkGreen')

graph = sg.Graph((800, 600),
          graph_bottom_left=(0,0),
          graph_top_right=(800,600),
          background_color='white',
          key='graph')

layout = [
    [graph],
    [sg.Text('PySimpleGUIWeb テスト')],
    [sg.Text('名前', size=(15, 1)), sg.InputText('山田太郎')],
    [sg.Text('年齢', size=(15, 1)), sg.Spin(None, initial_value=20)],
    [sg.Text('趣味', size=(15, 1)), sg.Combo(['料理','読書','映画'])],
    [sg.Submit(button_text='実行')]
]

window = sg.Window('PySimpleGUIWeb テスト', layout)

while True:
    event, values = window.read()
    if event is None:
        print('exit')
        break
    if event == '実行':
        show_message = "名前：" + values[0] + '\n'
        show_message += "年齢：" + values[1] + '\n'
        show_message += "趣味：" + values[2] + 'が入力されました。'
        print(show_message)
        sg.popup(show_message)

    graph.erase()
    graph.draw_line((0,0), (100,100), color='blue', width=5)
    graph.draw_text('ABC', (50,50), color='black', font=('VL ゴシック', 20))
    graph.draw_text('XYZ', (40,70))
    graph.draw_text('aaaaa', (200,200))
    graph.draw_text('日本語', (300,300))
    graph.draw_text('aaaaa', (-200,200))
    graph.draw_circle((20,20), 20, fill_color='green', line_color='yellow', line_width=2)

window.close()

