from filestack import Client

client= Client('')

new_filelink = client.upload(filepath='')
print(new_filelink.url)