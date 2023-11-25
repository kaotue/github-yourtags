import awsgi
import create_tags
import create_wordcloud

def get_tags(user):
    print(f'{user=}')
    tags = create_tags.run(user)
    if not tags:
        return 'not found'
    return create_wordcloud.run(tags)

if __name__ == '__main__':
    ret =  get_tags('kaotue')
    print(ret)