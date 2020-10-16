# -*- coding: utf-8 -*-
import sys
import os
import pytest
import argparse

sys.path.append("..")
import waybackpy.cli as cli  # noqa: E402
from waybackpy.wrapper import  Url  # noqa: E402
from waybackpy.__version__ import __version__

codecov_python = False
if sys.version_info > (3, 7):
    codecov_python = True

# Namespace(day=None, get=None, hour=None, minute=None, month=None, near=False,
# newest=False, oldest=False, save=False, total=False, url=None, user_agent=None, version=False, year=None)

if codecov_python:
    def test_save():
        args = argparse.Namespace(user_agent=None, url="https://pypi.org/user/akamhy/", total=False, version=False,
        oldest=False, save=True,  json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get=None)
        reply = cli.args_handler(args)
        assert "pypi.org/user/akamhy" in str(reply)

def test_json():
    args = argparse.Namespace(user_agent=None, url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=True, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get=None)
    reply = cli.args_handler(args)
    assert "archived_snapshots" in str(reply)

def test_archive_url():
    args = argparse.Namespace(user_agent=None, url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=True, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get=None)
    reply = cli.args_handler(args)
    assert "https://web.archive.org/web/" in str(reply)

def test_oldest():
    args = argparse.Namespace(user_agent=None, url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=True, save=False, json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get=None)
    reply = cli.args_handler(args)
    assert "pypi.org/user/akamhy" in str(reply)

def test_newest():
    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=True, near=False, alive=False, subdomain=False, known_urls=False, get=None)
    reply = cli.args_handler(args)
    assert "pypi.org/user/akamhy" in str(reply)

def test_total_archives():
    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=True, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get=None)
    reply = cli.args_handler(args)
    assert isinstance(reply, int)

def test_known_urls():
    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://akamhy.github.io", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=False, near=False, alive=True, subdomain=True, known_urls=True, get=None)
    reply = cli.args_handler(args)
    assert "github" in str(reply)

def test_near():
    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=False, near=True, alive=False, subdomain=False, known_urls=False, get=None, year=2020, month=7, day=15, hour=1, minute=1)
    reply = cli.args_handler(args)
    assert "202007" in str(reply)

def test_get():
    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get="url")
    reply = cli.args_handler(args)
    assert "waybackpy" in str(reply)

    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get="oldest")
    reply = cli.args_handler(args)
    assert "waybackpy" in str(reply)

    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get="newest")
    reply = cli.args_handler(args)
    assert "waybackpy" in str(reply)

    if codecov_python:
        args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
        (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=False, version=False,
        oldest=False, save=False, json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get="save")
        reply = cli.args_handler(args)
        assert "waybackpy" in str(reply)

    args = argparse.Namespace(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 \
    (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", url="https://pypi.org/user/akamhy/", total=False, version=False,
    oldest=False, save=False, json=False, archive_url=False, newest=False, near=False, alive=False, subdomain=False, known_urls=False, get="BullShit")
    reply = cli.args_handler(args)
    assert "get the source code of the" in str(reply)

def test_args_handler():
    args = argparse.Namespace(version=True)
    reply = cli.args_handler(args)
    assert ("waybackpy version %s" % (__version__)) == reply

    args = argparse.Namespace(url=None, version=False)
    reply = cli.args_handler(args)
    assert ("waybackpy %s" % (__version__)) in str(reply)

def test_main():
    # This also tests the parse_args method in cli.py
    cli.main(['temp.py', '--version'])
