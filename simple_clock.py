import PySimpleGUI as sg
from datetime import datetime


param: dict = {'text_size': 200}
weekday_jp: list = ['月', '火', '水', '木', '金', '土', '日']


def format_date(now: datetime) -> str:
    time: str = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
    date: str = datetime.strftime(now, '%Y-%m-%d %a')
    return dict(time=time, date=date)


def main():
    current_time = format_date(datetime.now())['time']
    today_date = format_date(datetime.now())['date']

    sg_layout = [
        # [sg.MenuBar([['メニュー', ['設定']]], key='menu')],
        [sg.Text(today_date, font=('Arial', int(param['text_size'] / 4)), key='today_date')],
        [sg.Text(current_time, font=('Arial', param['text_size']), key='current_time_text')]
    ]

    window = sg.Window(
        "Clock",
        layout=sg_layout,
        resizable=True,
        text_justification='center',
        element_justification='center',
    )

    while True:
        event, values = window.read(timeout=200, timeout_key='-timeout-')
        if event == sg.WIN_CLOSED:
            break
        else:
            current_time_update = format_date(datetime.now())['time']
            today_date_update = format_date(datetime.now())['date']
            if current_time != current_time_update:
                current_time = current_time_update
                window['current_time_text'].update(current_time_update)
            if today_date != today_date_update:
                today_date = today_date_update
                window['today_date'].update(today_date_update)
            # if values['menu'] == '設定':
            #     print(event)
            #     print(values)
            #     param['text_size'] = 400
            #     window['current_time_text'].update(font=('Arial', param['text_size']))

    window.close()


if __name__ == '__main__':
    main()

