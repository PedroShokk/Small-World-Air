import unittest
import entertainment
import alerts

# Write your code below: 
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  def test_maximum_display_brightness(self):
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)

  def test_device_temperature(self):
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)


class SystemAlertTests(unittest.TestCase):
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError,alerts.power_outage_detected, True) 

  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, )



unittest.main()
