#!/usr/bin/env python3

import os
import sys
import sh
import fabric
import uuid


def main():
    if os.getcwd() == os.path.expanduser('~'):
        print('NO')
        exit(1)
    addr = sys.argv[1]
    del sys.argv[1]
    path = '/tmp/{}'.format(uuid.uuid4())
    env = []
    while '=' in sys.argv[1]:
        env.append(sys.argv[1].split('='))
        del sys.argv[1]
    env = dict(env)

    print(sh.rsync('-a', '-v', '-z', '{}/'.format(os.getcwd()), '{}:{}'.format(addr, path)))

    cmd = 'cd {} && {}'.format(path, ' '.join(sys.argv[1:]))

    fabric.Connection(addr, inline_ssh_env=True).run(cmd, env=env)
    exit(1)

    sh.rsync('-a', '-v', '-z', '{}:{}/logs/'.format(addr, path), os.getcwd() + '/logs')


if __name__ == '__main__':
    main()
