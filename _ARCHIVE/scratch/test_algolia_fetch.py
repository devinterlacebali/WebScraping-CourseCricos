import sys
sys.path.append('Flinders University')
from flinders import fetch_courses

def main():
    courses = fetch_courses()
    print("Total Algolia courses returned:", len(courses))
    for idx, c in enumerate(courses[:15], 1):
        print(f"{idx}. {c['title']} - {c['url']}")

if __name__ == '__main__':
    main()
