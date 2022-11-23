from data import read_data

from ages import get_all_ages, get_the_oldest_age, get_the_youngest_age
from cities import get_all_cities
from countries import get_all_countries
from emails import get_all_emails
from nats import get_all_nats
from phone_numbers import get_all_numbers
from pictures import get_all_pictures_url
from streets import get_all_streets

data = read_data('Data/randomusers.json')
# print(data)
def main():
    ages = get_all_ages(data)
    # print(ages)
    oldest = get_the_oldest_age(ages)
    # print(oldest)
    youngest = get_the_youngest_age(ages)
    # print(youngest)
    cities = get_all_cities(data)
    # print(cities)
    countries = get_all_countries(data)
    # print(countries)
    emails = get_all_emails(data)
    # print(emails)
    n = get_all_nats(data)
    # print(n)
    phone_numbers = get_all_numbers(data)
    # print(phone_numbers)
    pictures = get_all_pictures_url(data)
    # print(pictures)
    streets = get_all_streets(data)
    print(streets)
main()