from github import Github
from db import db, CVElist, Rat, session 
import webbrowser
import time 


github_home = 'https://www.github.com/'
token = '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'
gh = Github(token)


def gh_api_search_for_cves():

    repos = gh.search_repositories(query='CVE-2021*', sort='updated')

    print('Requested info will be written to db. The program will exit upon completion...')
    for idx, repo in enumerate(repos[:10], start=1):
        print(f' {idx}  Repo Name: {repo.full_name}  Repo Description: {repo.description}  Created: {repo.created_at}  Stars: {repo.stargazers_count}')
  
        time.sleep(1)

        cve_list = CVElist(
            repo = repo.full_name,
            about = repo.description,
            created_date = repo.created_at,
            gh_stars = repo.stargazers_count 
        )

        session.add(cve_list)
        session.commit()
        session.close()
    db.dispose()
    print('\n')

    learn_more = int(input('To view the repo in your browser, select one of the index numbers above: '))
    if 0 < int(learn_more) <= idx:
        print()
        print(f"Repo {learn_more} was selected")
        print()
        webbrowser.open(github_home+repo.full_name, new=2)
    else:
        print('Didnt understand your selection, program exiting...')



def gh_api_search_for_rats():
    repos = gh.search_repositories(query='remote access tool', sort='updated')

    print('Requested info will be written to db. The program will exit upon completion...')
    for idx, repo in enumerate(repos[:10], start=1):
        print(f' {idx}  Repo Name: {repo.full_name}  Repo Description: {repo.description}  Created: {repo.created_at}  Stars: {repo.stargazers_count}')
  
        time.sleep(1)

        cve_list = Rat(
            repo = repo.full_name,
            about = repo.description,
            created_date = repo.created_at,
            gh_stars = repo.stargazers_count 
        )

        session.add(cve_list)
        session.commit()
        session.close()
    db.dispose()

    learn_more = int(input('To view the repo in your browser, select one of the index numbers above: '))
    if 0 < int(learn_more) <= idx:
        print()
        print(f"Repo {learn_more} was selected")
        print()
        webbrowser.open(github_home+repo.full_name, new=2)
    else:
        print('Didnt understand your selection, program exiting...')

