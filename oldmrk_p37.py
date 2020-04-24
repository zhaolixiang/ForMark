if __name__ == '__main__':
    res = {}
    with open('oldmark_before.txt') as f:
        txt = f.read()
        for line in txt.split():
            # print(line)
            key, _, value = line.partition('==')
            # print('key', key)
            # print('value', value)
            res.update({
                key: value
            })
    new_res = {}
    with open('oldmark_after.txt') as f:
        txt = f.read()
        for line in txt.split():
            # print(line)
            key, _, value = line.partition('==')
            # print('key', key)
            # print('value', value)
            if key not in res.keys():
                new_res.update({
                    key: value
                })
                print("有新的",key,value)
            else:
                print("已经存在：", key, value)

        # print(txt)
    with open('oldmark_before.txt', 'a') as f:
        for line in new_res:
            f.write('\n%s==%s' % (line, new_res[line]))
