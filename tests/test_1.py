import sys
sys.path.append("..")
import waybackpy
import pytest

user_agent = "Mozilla/5.0 (Windows NT 6.2; rv:20.0) Gecko/20121202 Firefox/20.0"

def test_clean_url():
    test_url = " https://en.wikipedia.org/wiki/Network security "
    answer = "https://en.wikipedia.org/wiki/Network_security"
    target = waybackpy.Url(test_url, user_agent)
    test_result = target.clean_url()
    assert answer == test_result

def test_url_check():
    broken_url = "http://wwwgooglecom/"
    with pytest.raises(Exception) as e_info:
        waybackpy.Url(broken_url, user_agent)

def test_save():
    # Test for urls that exist and can be archived.
    url1="https://github.com/akamhy/waybackpy"
    target = waybackpy.Url(url1, user_agent)
    archived_url1 = target.save()
    assert url1 in archived_url1

    # Test for urls that are incorrect.
    with pytest.raises(Exception) as e_info:
        url2 = "ha ha ha ha"
        waybackpy.Url(url2, user_agent)

    # Test for urls not allowed to archive by robot.txt.
    with pytest.raises(Exception) as e_info:
        url3 = "http://www.archive.is/faq.html"
        target = waybackpy.Url(url3, user_agent)
        target.save()

    # Non existent urls, test
    with pytest.raises(Exception) as e_info:
        url4 = "https://githfgdhshajagjstgeths537agajaajgsagudadhuss8762346887adsiugujsdgahub.us"
        target = waybackpy.Url(url3, user_agent)
        target.save()

def test_near():
    url = "google.com"
    target = waybackpy.Url(url, user_agent)
    archive_near_year = target.near(year=2010)
    assert "2010" in archive_near_year

    archive_near_month_year = target.near( year=2015, month=2)
    assert ("201502" in archive_near_month_year) or ("201501" in archive_near_month_year) or ("201503" in archive_near_month_year)

    archive_near_day_month_year = target.near(year=2006, month=11, day=15)
    assert ("20061114" in archive_near_day_month_year) or ("20061115" in archive_near_day_month_year) or ("2006116" in archive_near_day_month_year)

    target = waybackpy.Url("www.python.org", user_agent)
    archive_near_hour_day_month_year = target.near(year=2008, month=5, day=9, hour=15)
    assert ("2008050915" in archive_near_hour_day_month_year) or ("2008050914" in archive_near_hour_day_month_year) or ("2008050913" in archive_near_hour_day_month_year)

    with pytest.raises(Exception) as e_info:
        NeverArchivedUrl = "https://ee_3n.wrihkeipef4edia.org/rwti5r_ki/Nertr6w_rork_rse7c_urity"
        target = waybackpy.Url(NeverArchivedUrl, user_agent)
        target.near(year=2010)

def test_oldest():
    url = "github.com/akamhy/waybackpy"
    target = waybackpy.Url(url, user_agent)
    assert "20200504141153" in target.oldest()

def test_newest():
    url = "github.com/akamhy/waybackpy"
    target = waybackpy.Url(url, user_agent)
    assert url in target.newest()

def test_get():
    target = waybackpy.Url("google.com", user_agent)
    assert "Welcome to Google" in target.get(target.oldest())

def test_total_archives():

    target = waybackpy.Url(" https://google.com ", user_agent)
    assert target.total_archives() > 500000

    target = waybackpy.Url(" https://gaha.e4i3n.m5iai3kip6ied.cima/gahh2718gs/ahkst63t7gad8 ", user_agent)
    assert target.total_archives() == 0

if __name__ == "__main__":
    test_clean_url()
    print(".")
    test_url_check()
    print(".")
    test_get()
    print(".")
    test_near()
    print(".")
    test_newest()
    print(".")
    test_save()
    print(".")
    test_oldest()
    print(".")
    test_total_archives()
    print(".")
    print("OK")
