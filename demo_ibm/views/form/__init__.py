from flask_wtf import FlaskForm as Form


class Base(Form):
    def data_with_csrf(self):
        data = self.data

        data.pop('csrf_token')

        ''' 默认去除空值项 '''
        keys = list(data.keys())
        for k in keys:
            if data[k] == '':
                print(k)
                data.pop(k)

        return data